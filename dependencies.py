import structlog
from nameko.extensions import DependencyProvider

from utils import OuterGodRepository

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
        self.repo = OuterGodRepository()

    def get_dependency(self, worker_ctx):
        return self.repo.list_gods()
