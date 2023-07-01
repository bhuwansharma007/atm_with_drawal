"""Provides ability to invoke APIs"""
from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware
import json 
from api.views import internal as views_internal

APP = FastAPI(swagger_ui_parameters={"syntaxHighlight": False})
# router = APIRouter( prefix = "/api/v1", tags = ['ATM'])
router = APIRouter()

APP.include_router(router)
APP.include_router(views_internal)


#  to reslove CORS issues.
origins = ["*"]
APP.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def kickstart_app(fast_app):
    """Initalizes the fast api application"""
    configure_api(fast_app)


def configure_api(fast_app):
    """Configures fast api """
    with open("users.json") as users_db:
        data = json.load(users_db)



@router.get("/")
async def root():
    return {"message": "API are working fine"}



kickstart_app(APP)

if __name__ =="__main__":
    import uvicorn
    uvicorn.run(APP, host="0.0.0.0", port=8000)










# @APP.after_request
# def _after_request(respone):
#     return {"message": "I am after request"}
    
#     pass