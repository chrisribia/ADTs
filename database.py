from abc import (ABC, abstractmethod)
import psycopg2 as pg


class Postgres(ABC):
   
    @abstractmethod
    def connect(self,user, password, host, port, database):
        conn = pg.connect(host,database,user,password)
        return conn

    @abstractmethod
    def session(self):
        autocommit = True
        return self.connect.self.commit()
   
     @abstractmethod
    def cursor(self,query,url):
        conn = self.connect(url)
        cursor = conn.cursor()
        return cursor
      

    @abstractmethod
    def create_database(self,query,url):
          try:               
            cursor = self.cursor()
            cursor.execute(query)
             self.connect(url).self.commit()
           

          except (Exception, p.Error)as error:
            print("failed to create databse" + error)

           finally:

               if self.connect(url):
                   self.close() 

    @abstractmethod
    def status(self):
        pass

  
      
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
            print('Success')
        except:
            print("Failed")   

    @abstractmethod
    def insert_rows(self,query,url):
        try:
            cursor = self.cursor()
            cursor.execute(query)
            self.connect(url).self.commit()

        except (Exception, p.Error)as e:
            print(e)

        finally:

            if self.connect(url):
                self.close() 

    @abstractmethod
    def show_table(self,query):
         try:
            cursor = self.cursor()
            cursor.execute(query)
            self.session            
         
        except:
            print(" table not found")  

    @abstractmethod
    def drop_table(self,query,url):
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
