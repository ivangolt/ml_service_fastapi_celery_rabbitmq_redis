from loguru import logger

from src.connections.broker import celery_app
from src.services.model import TextToneClassifier


@celery_app.task(name="predict", bind=True, serializer="json")
def predict_tonality(self, text: str):
    """Predict tonality of text

    Args:
        text (str): input text
    """

    try:
        logger.info(f"Start prediction task: {self.request.id}")
        result = TextToneClassifier.predict_text_tone(text)
        return result.tolist()
    except Exception as exc:
        logger.error([exc])
        return None
