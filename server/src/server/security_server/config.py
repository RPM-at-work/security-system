from pydantic import BaseModel


class SecurityServerConfig(BaseModel):
    pass


class STMAPIConfig(BaseModel):
    pass


class DBServerConfig(BaseModel):
    dialect: str
    database: str


class DBServerConfigPostgres(DBServerConfig):
    host: str
    port: int
    user: str
    password: str


class CameraConfig(BaseModel):
    pass


class BackendConfig(BaseModel):
    host: str
    port: int


class GRPCConfig(BaseModel):
    host: str
    port: int
