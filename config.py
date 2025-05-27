import os
from pathlib import Path

BASE_DIR = Path(__file__).parent


class BaseConfig:
    # Безопасность
    SECRET_KEY = os.environ.get("SECRET_KEY", "change_me")

    # База данных
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL", f"sqlite:///{BASE_DIR / 'instance' / 'app.db'}"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Почта
    MAIL_SERVER = os.environ.get("MAIL_SERVER", "smtp.example.com")
    MAIL_PORT = int(os.environ.get("MAIL_PORT", 587))
    MAIL_USE_TLS = os.environ.get("MAIL_USE_TLS", "true").lower() in ("true", "1")
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

    # ЮKassa
    YOOKASSA_SHOP_ID = os.environ.get("YOOKASSA_SHOP_ID")
    YOOKASSA_SECRET_KEY = os.environ.get("YOOKASSA_SECRET_KEY")

    # Базовый URL сайта (для генерации внешних ссылок)
    SITE_BASE_URL = os.environ.get("SITE_BASE_URL", "http://localhost:5000")


class DevelopmentConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    DEBUG = False


class TestingConfig(BaseConfig):
    TESTING = True
    # in-memory для быстрых тестов
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
