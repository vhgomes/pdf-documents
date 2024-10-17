from typing import List

from pydantic import BaseModel


class DocumentResponse(BaseModel):
    title: str
    tags: List[str]
    signer: str
    summary: str
    translation: str