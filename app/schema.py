import uuid
from pydantic import BaseModel, Field


class Metadata(BaseModel):
    parentResourceId: str


class LogSchema(BaseModel):
    level: str
    message: str
    resourceId: str
    timestamp: str
    traceId: str
    spanId: str
    commit: str
    metadata: Metadata
