import structlog

logger = structlog.get_logger(__name__)


class OuterGodRepository:
    def __init__(self):
        logger.info("Connecting to database")

    def list_gods(self):
        logger.info("Mindlessly piping")
        return ["Azatoth", "Nyarlathothep", "Shub-Niggurath", "Yog-Sototh"]
