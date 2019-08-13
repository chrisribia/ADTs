from abc import (ABC, abstractmethod)
import psycopg2


class Postgres(ABC):
   
    @abstractmethod
    def connect(self,user, password, host, port, database):
        conn = psycopg2.connect(host,database,user,password)
        return conn

    @abstractmethod
    def session(self):
        autocommit = True
        return self.connect.commit()

    @abstractmethod
    def create_database(self,url):
          try:
            query = """CREATE DATABASE db_name='{0}';""".format(database_name)

            cursor = self.cursor()
            cursor.execute(query)
            self.connect(url).commit()

        except (Exception, p.Error)as e:
            print("failed to create databse" + e)

        finally:

            if self.connect(DATABASE_URL):
                self.close() 

    @abstractmethod
    def status(self):
        pass

    @abstractmethod
    def cursor(self,query):
        return self.session.cursor(query)

    @abstractmethod
    def select_table(self,query):
        pass

    @abstractmethod
    def create_table(self,query):             
        try:
            for query in queries:
                cursor.execute(query)
            self.session            
            print('Creating Tables.....Done')
        except:
            print("Failed to Create tables")   

    @abstractmethod
    def insert_rows(self,query):
        conn = psycopg2.connect(query)
        cur = conn.cursor()
        self.session  

    @abstractmethod
    def show_table(self,query):
        pass

    @abstractmethod
    def drop_table(self,query):
        conn = connection(DATABASE_URL)
        cursor = conn.cursor()        
        try:        
            self.cursor(query)
            self.session                
        except:
            print("Failed to Destroy tables")

    @abstractmethod
    def close(self):
        pass
