import psycopg


def test_wrong_password_must_fail():
    """тест упадет, все хорошо"""
    psycopg.connect(
        host="fake_localhost", # осознанно неверный
        port=5433,
        user="testuser",
        password="testpass",
        dbname="testdb",
        connect_timeout=5,
    )