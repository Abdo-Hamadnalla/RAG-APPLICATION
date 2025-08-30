from fastapi import FastAPI, APIRouter,Depends
import os
from helper.config import get_settings,Settings


Base_Router = APIRouter(prefix="/base", tags=["Base"])

@Base_Router.get("/")

async def Base_Route(app_settings:Settings = Depends(get_settings)):

    return {
            "message": "Welcome to the Mini RAG Application!",
            'app_name': app_settings.APP_NAME,
            "app_version": app_settings.APP_VERSION
            }
