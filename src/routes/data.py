from fastapi import FastAPI, APIRouter,Depends,UploadFile
import os
from helper.config import get_settings, Settings
from src.controllers.DataController import DataController

Data_Router = APIRouter(prefix="/data", tags=["data"])

@Data_Router.post("/upload/{project_id}")
async def upload_data(
    project_id: str,
    file: UploadFile,
    app_settings: Settings= Depends(get_settings)
    ):

    Isvalid = DataController().validate_file(file=file)
    return Isvalid

    # Here you would handle the file upload logic and criteria
    # We will make it in the data controller
