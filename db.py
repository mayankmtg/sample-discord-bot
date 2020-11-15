##   Primary Author: Mayank Mohindra <github.com/mayankmtg>
##
##   Description: File contains logic to handle with database layer
##
import sqlite3
from os import path

class Connection:
    """
    Class to function as a wrapper on the database
    All db interactions should go through here
    """
    def __init__(self, db_name: str = 'db.sqlite3') -> None:
        """
        Method initialisation.
        Create db if not exists. Else use the existing db instance

        Args:
            db_name: The name for the sqlite3 file that creates the database
        
        Returns:
            None
        """
        self.conn = None
        if not(path.isfile(db_name)):
            self.conn = sqlite3.connect(db_name)
            self.conn.execute("CREATE TABLE HARDCACHE (USERID INT, QUERY CHAR(70));")
        else:
            self.conn = sqlite3.connect(db_name)

    def execute(self, statement: str):
        """
        Method to execute any sql statement

        Args:
            statement: The sql statement string
        
        Returns:
            cursor object poining to the result set for the sql statement
        """
        cursor = self.conn.execute(statement)
        self.conn.commit()
        return cursor

    def shutdown(self) -> None:
        """
        Method to terminate the open sqlite3 connection

        Returns:
            None
        """
        self.conn.close()
