from fastapi import FastAPI
from transformers import PegasusForConditionalGeneration, PegasusTokenizer

app = FastAPI()


@app.post('/summarize')
async def get_sum():
    return {"Hello": "World"}


@app.get('/')
async def load():
    tokenizer = PegasusTokenizer.from_pretrained("google/pegasus-xsum")
    model = PegasusForConditionalGeneration.from_pretrained("google/pegasus-xsum")
    return {"Hello": "World"}