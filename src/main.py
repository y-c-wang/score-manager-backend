from fastapi import FastAPI

app = FastAPI(title="Scoreboard Manager API Server")


@app.get("/")
async def read_root():
    return {"ping": "pong"}
