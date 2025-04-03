import os

import pandas as pd
from sqlalchemy.engine import URL, create_engine


def create_snowflake_connection():
    """
    Creates a connection to Snowflake using the credentials stored in the environment variables.
    """
    connection_url = URL.create(
        "snowflake",
        username=os.getenv("SNOWFLAKE_USERNAME"),
        password=os.getenv("SNOWFLAKE_PASSWORD"),
        host=os.getenv("SNOWFLAKE_ACCOUNT"),
    )
    engine = create_engine(connection_url)
    return engine


def execute_snowflake_query(query: str) -> pd.DataFrame:
    """
    Given a SQL query, executes the query on Snowflake and returns the results as a pandas DataFrame.
    """
    engine = create_snowflake_connection()
    df = pd.read_sql_query(query, con=engine)
    return df
