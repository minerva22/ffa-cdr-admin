
import pymssql

class MfManager:
  def __init__(self, host: str=None, port: str=None, user: str=None, password: str=None, db:str=None):
    self.server   = host      #or "localhost"
    self.port     = port        #or "6200"
    self.user     = user     #or "root"
    self.password = password # or ""
    self.db = db 
#    self.db1 = db1   
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
      where CLI_TTU_COD=1
    """)
    res = cursor.fetchall()
    return res[0]['n']

  def superidsList(self):
    cursor = self._execute("""

      SELECT CLI_SUPERID, CLI_COD, CLI_NOM_PRE       
      FROM CLIENT
      where CLI_TTU_COD=1
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
        SELECT Ctry_Code, Ctry_Desc1
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
      SELECT DEV_COD,DEV_SYM_LGE1, DEV_LIB_LGE1
        
      FROM DEVISE
      
    """)
    return cursor

  def ledgerCount(self):

    cursor = self._execute("""
       Use MarketflowAcc
       SELECT
          count(*) as n
          FROM TABL
                   
       """)
    res = cursor.fetchall()
    return res[0]['n']


  def ledgersList(self):
      cursor = self._execute("""
        Use MarketflowAcc
        SELECT TaKey,Tadesc
          FROM TABL
          where len(TaKey)=4
        """)
      return cursor

  def entityCount(self):
    cursor = self._execute("""
      Use MArketflow
      SELECT
        count(*) as n
      FROM CLIENT_ENTITY

    """)
    res = cursor.fetchall()
    return res[0]['n']

  def entityList(self):
    cursor = self._execute("""
      Use Marketflow
      SELECT ENT_COD, ENT_FULL_NAME       
      FROM CLIENT_ENTITY
      
      order by ENT_COD asc
    """)
    return cursor


