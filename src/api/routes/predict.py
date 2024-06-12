"""
Модуль, содержащий роут для предсказаний модели.
"""

from fastapi import APIRouter, BackgroundTasks

from src.models.requests import PredictionResult, TextRequest
from src.services.utils import print_logger_info
from src.worker.predict_worker import celery_app

router = APIRouter()


@router.post("/predict/", response_model=PredictionResult, name="requests")
async def predict_text_tone(
    text_request: TextRequest, background_tasks: BackgroundTasks
):
    """Predict tonality of text

    Args:
        text_request (TextRequest): text request

    Returns:
        dict: result of prediction in format of dictionary


    """
    task = celery_app.send_task("predict", args=[text_request.text])
    result = task.get(timeout=30)

    background_tasks.add_task(
        print_logger_info,
        text_request.text,
        result,
    )

    return result
