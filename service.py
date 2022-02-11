import random
import time

from nameko.rpc import rpc
from nameko_structlog import StructlogDependency

from config import Config  # noqa
from dependencies import GreatOldOneProvider, OuterGodProvider


class ExampleService:
    name = "example_service"
    log = StructlogDependency()
    great_old_ones = GreatOldOneProvider()
    outer_gods = OuterGodProvider()

    @rpc
    def summon(self) -> str:
        entity = random.choice(self.great_old_ones + self.outer_gods)
        log = self.log.bind(operation="summon", entity=entity)
        if entity in self.outer_gods:
            log = log.bind(danger_level="high")
        time.sleep(1.5)
        log.info("Summoning", entity=entity)
        return entity

    @rpc
    def is_sane(self) -> str:
        log = self.log.bind(operation="sanity_check")
        sanity_level = random.randint(0, 100)
        log.info("Checking sanity", sanity_level=sanity_level)
        return sanity_level > 75
