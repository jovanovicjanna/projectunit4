import sqlite3


class database_worker:
    def __init__(self, name):
        # Initialize the database worker by connecting to the specified database
        self.connection = sqlite3.connect(name)
        self.cursor = self.connection.cursor()

    def search(self, query):
        # Execute the search query and retrieve all results
        result = self.cursor.execute(query).fetchall()  # gets a list
        return result

    def get(self, query):
        # Execute the query and retrieve the first result
        result = self.cursor.execute(query).fetchone()  # get only one result(the first)
        return result

    def run_save(self, query):
        # Execute the query and save the changes to the database
        self.cursor.execute(query)
        self.connection.commit()

    def close(self):
        # Close the database connection
        self.connection.close()


from passlib.context import CryptContext

pwd_config = CryptContext(schemes=["pbkdf2_sha256"],
                          default="pbkdf2_sha256",
                          pbkdf2_sha256__default_rounds=30000
                          )


def encrypt_password(user_password):
    """ This function receives the plain text password from the user and returns the hash salted
    """
    return pwd_config.encrypt(user_password)


def check_password(user_password, hashed):
    return pwd_config.verify(user_password, hashed)
