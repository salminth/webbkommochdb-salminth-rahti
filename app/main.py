from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return { "msg": "Hello dev docker!", "v": "0.2" }




@app.get("/api/ip")
def ip():
    return { "ip": "Morjens ip"}

