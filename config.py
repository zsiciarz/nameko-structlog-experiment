import logging.config
import structlog


class Config:
    IS_LOCAL = True

    LOGGING = {
        "version": 1,
        "disable_existing_loggers": True,
        "formatters": {"structlog": {"format": "%(asctime)s %(message)s"}},
        "handlers": {
            "console": {
                "level": "DEBUG",
                "class": "logging.StreamHandler",
                "formatter": "structlog",
            },
        },
        "loggers": {
            "nameko": {"handlers": ["console"], "level": "WARNING"},
            "dependencies": {"handlers": ["console"], "level": "INFO"},
            "example_service": {"handlers": ["console"], "level": "INFO"},
        },
    }

    STRUCTLOG = {
        "processors": [
            structlog.stdlib.filter_by_level,
            structlog.stdlib.add_logger_name,
            structlog.stdlib.add_log_level,
            structlog.stdlib.PositionalArgumentsFormatter(),
            structlog.processors.StackInfoRenderer(),
            structlog.processors.format_exc_info,
            structlog.processors.UnicodeDecoder(),
            structlog.dev.ConsoleRenderer()
            if IS_LOCAL
            else structlog.processors.LogfmtRenderer(),
        ],
        "context_class": structlog.threadlocal.wrap_dict(dict),
        "logger_factory": structlog.stdlib.LoggerFactory(),
        "wrapper_class": structlog.stdlib.BoundLogger,
        "cache_logger_on_first_use": True,
    }


logging.getLogger().handlers = []
logging.config.dictConfig(Config.LOGGING)

structlog.configure(**Config.STRUCTLOG)  # type: ignore
