from langchain_qdrant import QdrantVectorStore
from psycopg2.extensions import connection
from qdrant_client import QdrantClient
from typing_extensions import Annotated, Dict, List, TypedDict, Union

from agent_framework.states.pg_states import TableState


class PostgresQdrantState(TypedDict):
    # ---------------------------
    recursion_limit: int
    similarity_doc_number: int
    # ---------------------------
    postgres_connection_info: Dict[str, Union[int, str]]
    # ---------------------------
    database: connection
    database_is_connected: bool
    tables: Dict[str, TableState]
    # ---------------------------
    qdrant_connection_info: Dict[str, str]
    vector_store_is_connected: bool
    collection: str
    # ---------------------------
    qdrant_client: QdrantClient
    vector_store: QdrantVectorStore
    # ---------------------------
    question: str
    joined_related_documents: str
    sql_code: str
    # ---------------------------
    debug: bool
