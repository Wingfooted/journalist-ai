'''import mysql.connector
import time
import json
from mysql.connector import Error'''

import mysql.connector
from mysql.connector import pooling, Error
from datetime import date
import time
import json

#USER CLASSES
class Database:
    def __init__(self, host, user, password, database, write_publication=None):
        self.pool = pooling.MySQLConnectionPool(
            pool_name="mypool",
            pool_size=5, #pools may not be necessary for vectors. Since 1 user really. 
            pool_reset_session=True,
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.operations = DataOperations(self.pool)
            
    def create_info(self, content, summary, loc, tags, path):
        try:
            # Create a new publication in the publications table
            publication_id = self.operations.create(
                table="knowledge",
                columns=["content", "summary", "knowledge_loc", "tags", "upload_date", "util", "n", "origin"],
                values=[
                    content
                    , summary
                    , loc
                    , str(tags)
                    , date.today().strftime('%Y-%m-%d')
                    , 0
                    , 0
                    , path
                ]
            )
            """
            , content TEXT
            , summary TEXT
            , knowledge_loc VARCHAR(255)
            , tags VARCHAR(255)
            , upload_date VARCHAR(255)
            , util FLOAT
            , n INT
            """
        except Error as e:
            print("Error:", e)
    

#METHOD CLASSES
class DataOperations:
    def __init__(self, pool):
        #simple CRUD OPERATIONS
        self.pool = pool

    def create(self, table, columns, values):
        try:
            connection = self.pool.get_connection()
            if connection.is_connected():
                cursor = connection.cursor()

                columns_str = ", ".join(columns)
                placeholders = ", ".join(["%s"] * len(values))
                sql = f"INSERT INTO {table} ({columns_str}) VALUES ({placeholders})"
                
                cursor.execute(sql, values)
                connection.commit()
                
                return cursor.lastrowid  # Return the ID of the newly inserted row

            else:
                print("Failed to establish connection.")
        except Error as e:
            print("Error:", e)
        finally:
            if connection and connection.is_connected():
                cursor.close()
                connection.close()

    def update(self, table, columns, values, where_columns, where_values):
        try:
            connection = self.pool.get_connection()
            if connection.is_connected():
                cursor = connection.cursor()

                set_values = ", ".join([f"{col} = %s" for col in columns])
                where_clause = " AND ".join([f"{col} = %s" for col in where_columns])
                
                sql = f"UPDATE {table} SET {set_values} WHERE {where_clause}"
                cursor.execute(sql, values + where_values)
                
                connection.commit()
                
            else:
                print("Failed to establish connection.")
        except Error as e:
            print("Error:", e)
        finally:
            if connection and connection.is_connected():
                cursor.close()
                connection.close()

    def read(self, table, where_columns, where_values):
        try:
            connection = self.pool.get_connection()
            if connection.is_connected():
                cursor = connection.cursor(dictionary=True)

                where_clause = " AND ".join([f"{col} = %s" for col in where_columns])
                sql = f"SELECT * FROM {table} WHERE {where_clause}"
                cursor.execute(sql, where_values)
                
                result = cursor.fetchall()
                return result

            else:
                print("Failed to establish connection.")
        except Error as e:
            print("Error:", e)
        finally:
            if connection and connection.is_connected():
                cursor.close()
                connection.close()

    def destroy(self, table, where_columns, where_values):
        try:
            connection = self.pool.get_connection()
            if connection.is_connected():
                cursor = connection.cursor()

                where_clause = " AND ".join([f"{col} = %s" for col in where_columns])
                sql = f"DELETE FROM {table} WHERE {where_clause}"
                cursor.execute(sql, where_values)
                
                connection.commit()
                
            else:
                print("Failed to establish connection.")
        except Error as e:
            print("Error:", e)
        finally:
            if connection and connection.is_connected():
                cursor.close()
                connection.close()

    def get_locs(self, publication):
        try:
            connection = self.pool.get_connection()
            if connection.is_connected():
                cursor = connection.cursor(dictionary=True)

                sql = f"SELECT knowledge_loc FROM vector_db_pref WHERE publication = '{publication}'"
                cursor.execute(sql)
                
                result = cursor.fetchall()
                return result

            else:
                print("Failed to establish connection.")
        except Error as e:
            print("Error:", e)
        finally:
            if connection and connection.is_connected():
                cursor.close()
                connection.close()

    def raw(self, sql):
        try:
            connection = self.pool.get_connection()
            if connection.is_connected():
                cursor = connection.cursor(dictionary=True)
                cursor.execute(sql)
                result = cursor.fetchall()
                return result
        except Error as e:
            print("Error:", e)
        finally:
            if connection and connection.is_connected():
                cursor.close()
                connection.close()


