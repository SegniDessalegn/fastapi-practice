from pydantic import BaseModel
from typing import Optional

class Blog(BaseModel):
    title: str
    body: Optional[str] = None
    published: Optional[bool] = False
