from fastapi import FastAPI

app = FastAPI()


@app.post('/summarize')
async def get_sum():
    return {"Hello": "World"}