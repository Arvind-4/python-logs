from fastapi import FastAPI

from app.es import ESConnection
from app.schema import LogSchema
from app.utils import generate_id

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello World"}


@app.post("/api/v1/insert")
def insert_method(log: LogSchema):
    client = ESConnection()
    inserted, _ = client.insert_document(
        index_name="test", id=generate_id(), document=log.model_dump()
    )
    if not inserted:
        return {"message": "Error"}
    return {"message": "Inserted"}


@app.get("/api/v1/get")
def get():
    client = ESConnection()
    data = client.get_all_data(
        index_name="test",
    )
    return {"data": data}
