import uvicorn
from pydantic import BaseModel

from fastapi import FastAPI


class Locus(BaseModel):
    id: str


app = FastAPI()


@app.post("/")
async def root(locus: Locus):
    print(locus.id)
    return {"status": True}


if __name__ == "__main__":
    uvicorn.run("server:app", host="0.0.0.0", port=5000)
