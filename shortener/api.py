from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from ninja import Router
from .models import URL
from .schemas import URLSchema, URLCreateSchema
from .views import generate_short_code

router = Router()


@router.post("/create", response=URLSchema)
def create_url(request, payload: URLCreateSchema):
    short_code = generate_short_code()
    created = URL.objects.create(original_url=payload.original_url, expires_at=payload.expires_at, short_code=short_code)
    url = get_object_or_404(URL, pk=created.pk)
    return url


@router.get("/{short_code}")
def visit_url(request, short_code: str) -> HttpResponseRedirect:
    url = get_object_or_404(URL, short_code=short_code)
    # We could check here if the original_url actually works and if not return an error.
    return HttpResponseRedirect(url.original_url)
