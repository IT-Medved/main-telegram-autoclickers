from pydantic_settings import BaseSettings, SettingsConfigDict
import os
import sys
import importlib.util
parent_dir = os.path.abspath(os.path.join(os.getcwd(), ".."))
file_path = os.path.join(parent_dir, "global_data", "global_config.py")
spec = importlib.util.spec_from_file_location("global_config", file_path)
modu = importlib.util.module_from_spec(spec)
sys.modules["global_config"] = modu
spec.loader.exec_module(modu)
import global_config

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_ignore_empty=True)

    API_ID: int = global_config.API_ID
    API_HASH: str = global_config.API_HASH

    USE_TG_BOT: bool = global_config.USE_TG_BOT
    BOT_TOKEN: str = global_config.MUSKEMPIRE_BOT_TOKEN
    CHAT_ID: str = global_config.CHAT_ID

    SKILLS_MODE: str = 'profitness'
    REF_CODE: str = global_config.REF_CODE

    TAPS_ENABLED: bool = True
    TAPS_PER_SECOND: list[int] = [10, 30] # tested with 4 fingers
    PVP_ENABLED: bool = False
    PVP_LEAGUE: str = 'auto'
    PVP_UPGRADE_LEAGUE: bool = False
    PVP_STRATEGY: str = 'random'
    PVP_COUNT: int = 3
    SKILLS_COUNT: int = 8
    IGNORED_SKILLS: list[str] = []
    MINING_SKILLS_LEVEL: int = 10
    PROTECTED_BALANCE: int = 3000000
    BIG_SLEEP: list[int] = global_config.BIG_SLEEP

    DEBUG_MODE: bool = False
    SLEEP_BETWEEN_START: list[int] = global_config.ACC_DELAY
    ERRORS_BEFORE_STOP: int = 5
    USE_PROXY_FROM_FILE: bool = global_config.USE_PROXY


config = Settings()
