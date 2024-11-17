import uvicorn
from fastapi import FastAPI
from api.routers import routers_v1


def create_app() -> FastAPI:
    app = FastAPI()
    app.include_router(routers_v1.router, prefix="/v1")
    return app


search_api = create_app()


if __name__ == "__main__":
    uvicorn.run(search_api, host="localhost", port=4000)
