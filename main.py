import uvicorn
import os
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class PredictionRequest(BaseModel):
    inputs: str

@app.get('/')
def root():
    return {"message": "Welcome to the centre for Testing Cloud Run stuff"}

@app.post('/predict')
def predict(request: PredictionRequest):
    pred = request.inputs + ' inputs processed'
    return {"message": {"inputs": request.inputs, "predictions": pred}}

if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=int(os.environ.get('PORT', '8080')))
