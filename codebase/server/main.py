from fastapi import FastAPI
from pydantic import BaseModel
from pathlib import Path
from typing import Optional, Any

app = FastAPI()


class PredictRequest(BaseModel):
    data: Optional[Any] = None


WEIGHTS_PATH = Path(__file__).resolve().parent.parent / "model" / "weights" / "model_weights.txt"


def load_weights() -> Optional[str]:
    try:
        return WEIGHTS_PATH.read_text()
    except Exception:
        return None


@app.get("/")
async def root():
    return {"status": "ok"}


@app.post("/predict")
async def predict(req: PredictRequest):
    weights = load_weights()
    if weights is None:
        return {"status": "error", "detail": "weights not found"}
    # simulate using weights for prediction
    return {"status": "ok"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("server.main:app", host="0.0.0.0", port=8000)
