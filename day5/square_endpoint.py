from fastapi import FastAPI
app1=FastAPI()
@app1.get("/square/{n}")
def func_sqare(n:int):
    return {"input":n,"Result":n*n}
