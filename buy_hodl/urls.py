from fastapi import FastAPI, APIRouter

from buy_hodl.api.v1 import health_router, core_router

from buy_hodl.api.v1.endpoints import users, login, asset_type, asset


def configure_routes(app: FastAPI) -> FastAPI:
    v1 = APIRouter(prefix='/api/v1')
    v1.include_router(users.router)
    v1.include_router(login.router)
    v1.include_router(asset.router)
    v1.include_router(asset_type.router)

    app.include_router(v1)


    return app
