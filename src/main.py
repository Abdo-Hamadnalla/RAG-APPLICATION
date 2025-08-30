from fastapi import FastAPI
# from dotenv import load_dotenv
# # Load environment variables from .env file
# load_dotenv(".env")
from routes import base,data 
app = FastAPI()
app.include_router(base.Base_Router)
app.include_router(data.Data_Router)