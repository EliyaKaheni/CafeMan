import mysql.connector

class DatabaseManager:
    def __init__(self):
        self.host = 'localhost'
        self.user = 'root'
        self.password = 'HShea@yazd82'
        self.database = 'cafeman'
        self.connection = None


    def connect(self) -> bool:
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
        except Exception as e:
            print(f'Error in connecting to database: {e}')
            return False
    
    def close_connection(self):
        if self.connection:
            self.connection.close()


    def signup(self, username:str, password:str) -> bool:
        query = 'INSERT INTO users (username, password) VALUES (%s, %s)'
        try:            
            self.connect()
            cursor = self.connection.cursor()
            cursor.execute(query, (username, password))
            self.connection.commit()

            return True
            
        except Exception as e:
            print(f'Error in signup function: {e}')
            return False

        finally:
            self.close_connection()
    

    def signin(self, username:str, password:str) -> bool:
        query = "SELECT * FROM users WHERE username = %s AND password = %s"
        try:
            self.connect()
            cursor = self.connection.cursor(dictionary=True)
            cursor.execute(query, (username, password))
            user = cursor.fetchone()
            return user is not None
    
        except Exception as e:
            print(f'Error in signup function: {e}')
            return False

        finally:
            self.close_connection()


    def reset_database(self) -> bool:
        try:
            self.connect()
            cursor = self.connection.cursor()

            cursor.execute('DELETE FROM users')

            self.connection.commit()
            return True

        except Exception as e:
            print(f'Error resetting database: {e}')
            return False

        finally:
            self.close_connection()

    def user_exist(self, username:str):
        query = "SELECT * FROM users WHERE username = %s"
        try:
            self.connect()
            cursor = self.connection.cursor(dictionary=True)
            cursor.execute(query, (username,))
            user = cursor.fetchone()
            return user is not None
    
        except Exception as e:
            print(f'Error in user_exist function: {e}')
            return False

        finally:
            self.close_connection()