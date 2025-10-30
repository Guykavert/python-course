class Config:
    BASE_URL = "https://ru.yougile.com"
    API_VERSION = "api-v2"
    API_TOKEN = "YOUR_API_TOKEN_HERE"

    @classmethod
    def get_base_url(cls):
        return f"{cls.BASE_URL}/{cls.API_VERSION}"
