from elasticsearch import Elasticsearch

from app.constants import get_settings

settings = get_settings()


class ESConnection:
    def __init__(self) -> None:
        self.esClient: Elasticsearch = None
        self.connect()

    def connect(self):
        host = settings.elasticSearchHost
        port = settings.elasticSearchPort
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

    def get_all_data(self, index_name, size=10) -> dict or None:
        try:
            return self.esClient.search(
                index=index_name, body={"query": {"match_all": {}}}, size=size
            )
        except Exception as e:
            print(e)
            return None
