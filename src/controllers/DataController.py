from .BaseController import BaseController
from fastapi import UploadFile, Depends
class DataController(BaseController):

    def __init__(self):
        super().__init__()
    def validate_file(self,file: UploadFile):
        if (file.content_type not in self.app_settings.FILE_ALLOWED_EXTENSIONS):
            raise ValueError(f'{file} Is Invalid file type')
        if(file.size>self.app_settings.FILE_MAX_SIZE*1024*1024):
            raise ValueError(f'{file} Is too large, max size is {self.app_settings.FILE_MAX_SIZE} MB')
        return "File is valid"

    



