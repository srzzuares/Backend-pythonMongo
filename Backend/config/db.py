import os
from sqlalchemy import create_engine,MetaData
from dotenv import load_dotenv
load_dotenv()

engine = create_engine("mysql+pymysql://root:1234@localhost:3307/utxjdb")
meta=MetaData()
conn=engine.connect()