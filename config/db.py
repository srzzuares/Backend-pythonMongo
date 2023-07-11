from sqlalchemy import create_engine,MetaData
from dotenv import load_dotenv

load_dotenv()

engine = create_engine(meta_data)
meta=MetaData()