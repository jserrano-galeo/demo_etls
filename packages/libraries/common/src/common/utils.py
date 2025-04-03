import sqlparse


def format_query(query: str) -> str:
    """
    Given a SQL query, formats the query using sqlparse to make it more readable.
    """
    return sqlparse.format(
        query, reindent=True, keyword_case="upper", strip_comments=True
    )
