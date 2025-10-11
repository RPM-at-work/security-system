from pydantic import BaseModel


class BaseTDO(BaseModel):
    name: str
    email: str
