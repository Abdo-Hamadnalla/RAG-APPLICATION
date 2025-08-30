from pydantic_settings import BaseSettings , SettingsConfigDict

class Settings(BaseSettings):
    # Define your configuration variables here
    APP_NAME: str 
    APP_VERSION: str 
    FILE_ALLOWED_EXTENSIONS: list
    FILE_MAX_SIZE: int
    APP_DESCRIPTION: str 
    APP_AUTHOR: str 
    APP_LICENSE: str
    class Config:
        env_file = ".env"

def get_settings():
    return Settings()
