##   Primary Author: Mayank Mohindra <github.com/mayankmtg>
##
##   Description: File contains logic to handle search queries
##
from googlesearch import search

def perform_search(query: str) -> list:
    """
    Method to perform the google search on the query and return result

    Args:
        query: the query string which we want to search for

    Returns:
        list: the list of the top links corresponding to the query
    """
    # TODO (mayankmohindra06@gmail.com) Make these parameters configurable
    return search(query, tld="com", num=5, stop=5, pause=2)