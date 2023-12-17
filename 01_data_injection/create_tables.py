from typing import NewType
import psycopg2

PostgresCursor = NewType("PostgresCursor", psycopg2.extensions.cursor)
PostgresConn = NewType("PostgresConn", psycopg2.extensions.connection)

table_drop_DividendsHistorical    = "DROP TABLE IF EXISTS DividendsHistorical;"
table_drop_DelistedCompanies     = "DROP TABLE IF EXISTS DelistedCompanies;"

table_create_DividendsHistorical = """
CREATE TABLE IF NOT EXISTS DividendsHistorical (
                symbol VARCHAR(100) NOT NULL,
                date DATE NOT NULL,
                label VARCHAR(100),
                adjDividend FLOAT,
                dividend FLOAT,
                recordDate DATE,
                paymentDate DATE,
                declarationDate DATE,
                PRIMARY KEY (symbol, date)
);
"""
table_create_DelistedCompanies = """
CREATE TABLE IF NOT EXISTS DelistedCompanies (
                symbol VARCHAR(50) NOT NULL,
                companyName VARCHAR(200),
                exchange VARCHAR(100),
                ipoDate DATE,
                delistedDate DATE,
                PRIMARY KEY (symbol)
);
"""

drop_table_queries   = [table_drop_DividendsHistorical, table_drop_DelistedCompanies]
create_table_queries = [table_create_DividendsHistorical, table_create_DelistedCompanies]


def drop_tables(cur: PostgresCursor, conn: PostgresConn) -> None:
    """
    Drops each table using the queries in `drop_table_queries` list.
    """
    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()

def create_tables(cur: PostgresCursor, conn: PostgresConn) -> None:
    """
    Creates each table using the queries in `create_table_queries` list.
    """
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()


def main():
    """
    - Drops (if exists) and Creates the sparkify database.
    - Establishes connection with the sparkify database and gets
    cursor to it.
    - Drops all the tables.
    - Creates all tables needed.
    - Finally, closes the connection.
    """
    conn = psycopg2.connect(
        "host=127.0.0.1 dbname=postgres user=postgres password=postgres"
    )
    cur = conn.cursor()

    drop_tables(cur, conn)
    create_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()
