from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from ninja import Router
from .models import URL
from .schemas import URLSchema, URLCreateSchema
from .views import generate_short_code

router = Router()


@router.post("/create", response=URLSchema)
def create_url(request, payload: URLCreateSchema):
    """Continuously generate a shortened url until it is unique."""
    while True:
        short_code = generate_short_code()
        try:
            created = URL.objects.create(
                original_url=payload.original_url,
                expires_at=payload.expires_at,
                short_code=short_code,
            )
            # Retrieve the created object because the expiration date might be in the past.
            url = get_object_or_404(URL, pk=created.pk)
            return url  # Exit the loop if creation is successful
        except IntegrityError:
            continue  # Retry if there is an IntegrityError due to the unique constraint


@router.get("/{short_code}")
def visit_url(request, short_code: str) -> HttpResponseRedirect:
    url = get_object_or_404(URL, short_code=short_code)
    # We could check here if the original_url actually works and if not return an error.
    return HttpResponseRedirect(url.original_url)
