from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/")
async def get(request: Request):
    return "Hello World!"

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=9000, reload=True)
