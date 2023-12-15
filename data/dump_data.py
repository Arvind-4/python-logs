import uuid
import random
import string
import datetime
from elasticsearch import Elasticsearch


class ESConnection:
    def __init__(self) -> None:
        self.esClient: Elasticsearch = None
        self.connect()

    def connect(self):
        host = "localhost"
        port = 9200
        es = Elasticsearch(
            [
                {
                    "host": host,
                    "port": port,
                    "scheme": "http",
                }
            ]
        )
        self.esClient = es

    def insert_document(self, index_name: str, id: int, document: dict) -> (bool, str):
        try:
            self.esClient.index(body=document, index=index_name, id=id, doc_type="_doc")
            return True, "Sucessfully inserted document"
        except Exception as e:
            print(e)
            return False, "Error while inserting document"


LOG_LEVEL = ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]
MESSAGES = [
    "This is a debug message",
    "This is an info message",
    "This is a warning message",
    "This is an error message",
    "This is a critical message",
]


def generate_number() -> str:
    return str(random.randint(1000, 9999))


def generate_string() -> str:
    return "".join(random.choices(string.ascii_lowercase, k=3))


def get_resources_id() -> str:
    return "server" + "-" + generate_number()


def get_timestamp() -> str:
    return datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%fZ")


def get_trace_id() -> str:
    return generate_string() + "-" + generate_string() + "-" + generate_number()


def get_span_id() -> str:
    return "span" + "-" + generate_number()


def generate_commit() -> str:
    return "".join(random.choices(string.ascii_lowercase + string.digits, k=7))


def get_log_level() -> str:
    return str(random.choice(LOG_LEVEL)).lower()


def get_message() -> str:
    return str(random.choice(MESSAGES))


def generate_id() -> str:
    return str(uuid.uuid4())


numberOfDocuments = input("Enter the number of documents to be inserted: ")

client = ESConnection()

for i in range(int(numberOfDocuments)):
    document = {
        "level": get_log_level(),
        "message": get_message(),
        "resourceId": get_resources_id(),
        "timestamp": get_timestamp(),
        "traceId": get_trace_id(),
        "spanId": get_span_id(),
        "commit": generate_commit(),
        "metadata": {"parentResourceId": get_resources_id()},
    }
    try:
        id_ = generate_id()
        inserted, _ = client.insert_document(
            index_name="test",
            id=id_,
            document=document,
        )
        if not inserted:
            print("Error while inserting document at id: ", id_)
        else:
            print("Sucessfully inserted document at id: ", id_)
    except Exception as e:
        print(e)
        print("Error while inserting document")
