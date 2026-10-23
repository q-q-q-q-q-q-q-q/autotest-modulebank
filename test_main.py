
def test_connection(db_conn):
    #тест самого подключения
    assert db_conn.closed is False


def test_simple_query(db_conn):
    with db_conn.cursor() as cur:
        cur.execute("select now();")
        result = cur.fetchone()

    assert result is not None, "Запрос не вернул ни одной строки"
    assert result[0] is not None, "Значение now() пустое"
    print(f"\nТекущее время сервера: {result[0]}")


