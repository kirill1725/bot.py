from dataclasses import dataclass
import os
import dotenv

dotenv.load_dotenv()


@dataclass
class TgBot:
    token: str  # Токен для доступа к телеграм-боту


@dataclass
class LogSettings:
    level: str
    format: str


@dataclass
class Config:
    bot: TgBot
    log: LogSettings


def load_config(path: str | None = None) -> Config:
    token=os.getenv('BOT_TOKEN')
    return Config(
        bot=TgBot(token=token),
        log=LogSettings(level=os.getenv("LOG_LEVEL"), format=os.getenv("LOG_FORMAT")),
    )