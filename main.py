# main.py
from fastapi import FastAPI
app = FastAPI()
@app.get("/")
async def root():
 return {"greeting":"40 year of happy life"}
