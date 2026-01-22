import logging

_LOG_LEVEL_TO_ONNX = {
    logging.NOTSET: 4,
    logging.DEBUG: 4,
    logging.INFO: 4,
    logging.WARNING: 4,
    logging.ERROR: 3,
    logging.CRITICAL: 3,
}


def translate_log_level(level: int) -> int:
    """Translate Python debugg level to ONNX runtime error level
    since blank pages error are shown at level 3 that should be the
    exception, and 4 the normal behavior"""
    return _LOG_LEVEL_TO_ONNX.get(level, 0)


logger = logging.getLogger("unstructured_inference")

logger_onnx = logging.getLogger("unstructured_inference_onnxruntime")
logger_onnx.setLevel(translate_log_level(logger.getEffectiveLevel()))
