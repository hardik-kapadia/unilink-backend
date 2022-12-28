from pydantic import BaseSettings, Field

class Settings(BaseSettings):
    client_id: str = "Awesome API"
    redirect_uri: str = "https://"
    bearer_token: str = Field(...,env='BEARER_TOKEN')