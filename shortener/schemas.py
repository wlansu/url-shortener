import datetime
from typing import Annotated

from ninja import Schema
from pydantic import HttpUrl
from pydantic.functional_validators import AfterValidator


class URLCreateSchema(Schema):
    """AnyHttpUrl is not considered a string which causes serialization issues,
        therefore we need to use Annotated with AfterValidator to convert it to a string.
    """
    original_url: Annotated[HttpUrl, AfterValidator(str)]
    expires_at: datetime.datetime | None = None


class URLSchema(URLCreateSchema):
    short_code: str
    created_at: datetime.datetime
