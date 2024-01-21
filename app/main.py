import databases
import uvicorn

from fastapi import FastAPI, APIRouter
from os import environ

# ~~~~~~~~~~~~~~~~~~~~~~~~
from fastapi_pagination import add_pagination

from app.config.settigns import settings, cookies_settings

from app.routers.api import api_router
from app.routers.docs_metadata import tags_metadata

# ~~~~~~~~~~~~~~~~~~~~~~~~



# берем параметры БД из переменных окружения
user = environ.get("user", "123")
password = environ.get("password", "123")
host = environ.get("host", "localhost")
port = environ.get("port", "5432")
db = environ.get("db", "123")


SQLALCHEMY_DATABASE_URL = (
f"postgresql://123:123@localhost:5432/123"
    # f"postgresql://{user}:{password}@{host}:5432/{db}"
)
database = databases.Database(SQLALCHEMY_DATABASE_URL)

app = FastAPI(
    debug=True,
    title=settings.PROJECT_NAME,
    version=settings.PROJECT_VERSION,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    openapi_tags=tags_metadata,
)
router = APIRouter()



app.include_router(api_router, prefix=settings.API_V1_STR)
add_pagination(app)


def run():
    uvicorn.run("main:app")



if __name__ == "__main__":
    run()
