import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import  CORSMiddleware
from fastapi_crudrouter import OrmarCRUDRouter

from Server.Models.Contracts import Contracts

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(OrmarCRUDRouter(schema=Contracts, paginate=99))

if __name__ == '__main__':
    uvicorn.run("__main__:app", port=8000, log_level="info")