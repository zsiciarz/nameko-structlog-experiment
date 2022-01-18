import structlog
from nameko.extensions import DependencyProvider

logger = structlog.get_logger(__name__)


class GreatOldOneProvider(DependencyProvider):
    def setup(self):
        logger.info("Setting up", provider_class=self.__class__.__name__)

    def get_dependency(self, worker_ctx):
        logger.info("Indexing the Necronomicon")
        return ["Atlach-Nacha", "Cthulhu", "Tsathoggua", "Yig"]


class OuterGodProvider(DependencyProvider):
    def setup(self):
        logger.info("Setting up", provider_class=self.__class__.__name__)

    def get_dependency(self, worker_ctx):
        logger.info("Mindlessly piping")
        return ["Azatoth", "Nyarlathothep", "Shub-Niggurath", "Yog-Sototh"]
