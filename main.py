import uvicorn
from fastapi import FastAPI

from contas_a_pagar_e_receber.routers import contas_a_pagar_e_receber_router

app = FastAPI()


@app.get('/')
def home():
    return {'1': "FastAPI", '2': "FastAPI", '3': "FastAPI", '4': "FastAPI"}


app.include_router(contas_a_pagar_e_receber_router.router)

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8001)
