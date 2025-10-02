from pydantic import BaseModel


class UrlParams(BaseModel):
    currency: int
    item_nameid: int
