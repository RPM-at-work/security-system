from pydantic import BaseModel


class SecurityServerConfig(BaseModel):
    pass


class STMAPIConfig(BaseModel):
    pass


class DBServerConfig(BaseModel):
    dialect: str
    database: str


class CameraConfig(BaseModel):
    pass


class BackendConfig(BaseModel):
    pass


class GRPCConfig(BaseModel):
    host: str
    port: int
