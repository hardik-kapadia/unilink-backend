from pydantic import BaseSettings, Field

class Settings(BaseSettings):
    client_id: str = "Awesome API"
    redirect_uri: str = "https://"
    bearer_token: str = 'AAAAAAAAAAAAAAAAAAAAAPychwEAAAAAoQUXuvFAvscn8AXkW7%2BXnlJGZqI%3DM0A7Au6iJLeCuB1cpMeBLQSs8zHDjlGytSvTlWKI8De6wUwOSC'