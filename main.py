
from fastapi import FastAPI, Query
from stealth_agent import get_streaming_link

app = FastAPI()

@app.get("/get-link/")
def read_link(url: str = Query(..., description="Episode URL from animesugetv.to")):
    link = get_streaming_link(url)
    return {"streaming_link": link}
