import os
from sqlalchemy import create_engine,MetaData
from dotenv import load_dotenv
load_dotenv()

engine = create_engine("mysql+pymysql://root:cA5mkrXBoc.@localhost:3306/utxjdb")
meta=MetaData()
conn=engine.connect()