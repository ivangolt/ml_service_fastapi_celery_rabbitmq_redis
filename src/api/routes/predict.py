"""
Модуль, содержащий роут для предсказаний модели.
"""

from fastapi import APIRouter, BackgroundTasks

from src.celery.celery_init import celery
from src.models.requests import PredictionResult, TextRequest

router = APIRouter()


@router.post("/predict/", response_model=PredictionResult, name="requests")
async def predict_text_tone(
    text_request: TextRequest, background_tasks: BackgroundTasks
) -> PredictionResult:
    """Predict tonality of text

    Args:
        text_request (TextRequest): text request

    Returns:
        dict: result of prediction in format of dictionary


    """
    task = celery.send_task("analyze_tonality", args=[text_request.text])
    result = task.get(timeout=60)

    return result
