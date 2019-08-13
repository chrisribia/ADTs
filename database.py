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
    def create_database(self,query):
          try:            
            cursor = self.cursor()
            cursor.execute(query)
            self.connect(url).commit()

        except (Exception, p.Error)as e:
            print("failed to create databse" + e)

        finally:

            if self.connect(url):
                self.close() 

    @abstractmethod
    def status(self):
        pass

    @abstractmethod
    def cursor(self,query):
        conn = self.connect(url)
        cursor = conn.cursor(query)
        return cursor
      
      
    @abstractmethod
    def select_table(self,query):
        try:
            cursor.execute(query)
            self.session            
         
        except:
            print(" table not found")  

    @abstractmethod
    def create_table(self,query):             
        try:
            cursor.execute(query)
            self.session            
            print('Creating Tables.....Done')
        except:
            print("Failed to Create tables")   

    @abstractmethod
    def insert_rows(self,query):
        try:
            cursor = self.cursor()
            cursor.execute(query)
            self.connect(url).commit()

        except (Exception, p.Error)as e:
            print(e)

        finally:

            if self.connect(url):
                self.close() 

    @abstractmethod
    def show_table(self,query):
         try:
            cursor.execute(query)
            self.session            
         
        except:
            print(" table not found")  

    @abstractmethod
    def drop_table(self,query):
        conn = connection(url)
        cursor = conn.cursor()        
        try:        
            self.cursor(query)
            self.session                
        except:
            print("Failed to Destroy tables")

    @abstractmethod
    def close(self):
        pass
