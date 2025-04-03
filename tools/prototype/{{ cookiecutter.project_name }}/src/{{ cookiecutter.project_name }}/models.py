from pydantic import BaseModel, Field, HttpUrl, UrlConstraints
from pydantic_core import Url
from typing import Annotated


S3Url = Annotated[Url, UrlConstraints(max_length=2083, allowed_schemes=["s3"])]


class InputDocument(BaseModel):
    url: HttpUrl | S3Url = Field(
        ...,
        description="URL of the document to be analyzed",
        examples=["https://acount.aws/document.pdf", "s3://path/to/document.pdf"],
    )
