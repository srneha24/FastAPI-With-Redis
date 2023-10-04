import uvicorn
from fastapi import FastAPI, Request, Path
from fastapi.responses import JSONResponse

from assets.views import Redis

app = FastAPI()


@app.post("/redis")
async def create_hset(request: Request):
    data = await request.json()

    redis = Redis()
    await redis.create(data.get('name'), data.get('value'))

    return JSONResponse(content={"message": "Created"}, status_code=201)


@app.get("/redis")
async def retrieve_all_hsets(request: Request):
    name = request.query_params.get('name')

    redis = Redis()
    result = await redis.retrieve_all(name)

    return JSONResponse(content=result, status_code=302)


@app.get("/redis/{name}")
async def retrive_hset_by_key(request: Request, name: str = Path(...)):
    key = request.query_params.get('key')

    redis = Redis()
    result = await redis.retrive(name, key)

    return JSONResponse(content=result, status_code=302)


@app.post("/redis/{name}")
async def increment_field(request: Request, name: str = Path(...)):
    redis = Redis()
    result = await redis.increment_value(name)

    return JSONResponse(content=result, status_code=302)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
