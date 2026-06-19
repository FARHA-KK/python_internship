from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import time


from routers import users, tasks



app = FastAPI()



# CORS

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)




# Middleware logging

@app.middleware("http")
async def log_request(
    request,
    call_next
):

    start=time.time()


    response = await call_next(request)


    end=time.time()


    print(
        request.method,
        request.url,
        "Time:",
        end-start
    )


    return response




app.include_router(users.router)
app.include_router(tasks.router)