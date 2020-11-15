##   Primary Author: Mayank Mohindra <github.com/mayankmtg>
##
##   Description: File contains helper function to save and retrieve information from db
##
## TODO: Implement redis here to reduce db reads
from db import Connection
from error import ErrorMessage

def save_search_query(conn: Connection, userid: int, query: str) -> bool:
    """
    Method to save the search query in database

    Args:
        conn: Custom Connection object to interact with sqlite3 database
        userid: The id of the user who requested for this query
        query: The query string which the user requested

    Returns:
        bool: True if success; else False
    """
    try:
        conn.execute("INSERT INTO HARDCACHE (USERID, QUERY) VALUES ({}, '{}');".format(userid, query))
    except Exception as e:
        print (e)
        print (ErrorMessage.INSERT_DB_EXCEPTION)
        return False
    return True

def find_search_history(conn: Connection, userid: int, query: str) -> list:
    """
    Method to find from search history for the userid based on substring match

    Args:
        conn: Custom Connection object to interact with sqlite3 database
        userid: The id of the user who requested for this query
        query: The query string which the user requested

    Returns:
        list: The list of all the queries the user did containing the substring "query"
    """
    try:
        cursor = conn.execute("SELECT QUERY FROM HARDCACHE WHERE USERID = {} AND QUERY LIKE '%{}%'".format(userid, query))
        result = []
        for row in cursor:
            result.append(row[0])
        return result
    except Exception as e:
        print (e)
        print (ErrorMessage.SELECT_DB_EXCEPTION)
    return []
