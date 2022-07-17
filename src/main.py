from fastapi import FastAPI
from transformers import PegasusForConditionalGeneration, PegasusTokenizer

app = FastAPI()

# tokenizer = PegasusTokenizer.from_pretrained("google/pegasus-xsum")
# model = PegasusForConditionalGeneration.from_pretrained("google/pegasus-xsum")

# tokenizer.save_pretrained('pretrained/tokenizer')
# model.save_pretrained('pretrained/model')

tokenizer = PegasusTokenizer.from_pretrained("pretrained/tokenizer")
model = PegasusForConditionalGeneration.from_pretrained("pretrained/model")

@app.post('/summarize')
async def get_sum():
    return {"Hello": "World"}


@app.get('/')
async def load():
    return {"Hello": "Transformers!"}
