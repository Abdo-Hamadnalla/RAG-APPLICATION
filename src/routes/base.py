from fastapi import FastAPI, APIRouter
import os
Base_Router = APIRouter(prefix="/base", tags=["Base"])

@Base_Router.get("/")

async def Base_Route():
    return {"message": "Welcome to the Mini RAG Application!",
            "app name": os.getenv("APP-NAME"),
            "version": os.getenv("APP_VERSION")
            }