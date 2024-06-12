from loguru import logger

from src.celery.celery_init import celery
from src.services.model import TextToneClassifier


@celery.task(name="analyze_tonality", bind=True)
def predict_tonality(self, text: str):
    """Predict tonality of text

    Args:
        text (str): input text
    """

    try:
        logger.info(f"Start prediction task: {self.request.id}")

        result = TextToneClassifier.predict_text_tone(text)

        logger.info(f"Input text: {text}")
        logger.info(f"Predicted: {str(result)}")
        logger.info(f"Completing prediction task {self.request.id}")

    except Exception as exp:
        logger.exception(f"Prediction task error {self.request.id}: {exp}")

    return result
