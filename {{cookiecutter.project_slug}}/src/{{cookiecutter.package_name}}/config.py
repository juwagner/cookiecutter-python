"""Configuration."""

from typing import Literal

from pydantic_settings import BaseSettings, SettingsConfigDict

from .constants import ROOT_PATH


class Config(BaseSettings):
    """Configuration."""

    model_config = SettingsConfigDict(env_file=ROOT_PATH / ".env", env_ignore_empty=True)

    log_level: Literal["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"] = "INFO"


def get_config() -> Config:
    """Get config."""
    return Config()
