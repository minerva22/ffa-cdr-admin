
import pymssql

class MfManager:
  def __init__(self, host: str=None, port: str=None, user: str=None, password: str=None, db:str=None):
    self.server   = host      #or "localhost"
    self.port     = port        #or "6200"
    self.user     = user     #or "root"
    self.password = password # or ""
    self.db = db 
   
  # get MF names
  # http://pymssql.org/en/stable/pymssql_examples.html
  def __enter__(self):
    self.conn = pymssql.connect(self.server, self.user, self.password, self.db, port=self.port, as_dict=True, charset="latin1")
    return self

  def _execute(self, query:str):
    cursor = self.conn.cursor()
    cursor.execute(query)
    return cursor

  def __exit__(self, exc_type, exc_val, exc):
    self.conn.close()

  def superidsCount(self):
    cursor = self._execute("""
      SELECT
        count(*) as n
      FROM CLIENT
       where cli_ttu_cod=1
    """)
    res = cursor.fetchall()
    return res[0]['n']

  def superidsList(self):
    cursor = self._execute("""
      SELECT CLI_SUPERID, rtrim(ltrim(CLI_NOM_PRE)) as Main_Holder_Name
        
      FROM CLIENT
      where cli_ttu_cod=1
      order by cli_superid asc
    """)
    return cursor
   

  
  def countryCount(self):
    cursor = self._execute("""
      SELECT
          count(*) as n
      FROM COUNTRY
    
    """)
    res = cursor.fetchall()
    return res[0]['n']


        
  def countryList(self):
      cursor = self._execute("""
        SELECT  Ctry_Desc1
        FROM COUNTRY
        order by Ctry_Desc1 asc
      """)
      return cursor

  def currencyCount(self):
    cursor = self._execute("""
      SELECT
        count(*) as n
      FROM DEVISE
      
    """)
    res = cursor.fetchall()
    return res[0]['n']

  def currencyList(self):
    cursor = self._execute("""
      SELECT DEV_SYM_LGE1
        
      FROM DEVISE
      
    """)
    return cursor

