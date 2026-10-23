import psycopg
import pytest

@pytest.fixture(scope="module")
def db_conn():
    conn = psycopg.connect(
        host="localhost", port=5433,
        user="testuser", password="testpass", dbname="testdb",
        connect_timeout=5,
    )
    yield conn
    conn.close()