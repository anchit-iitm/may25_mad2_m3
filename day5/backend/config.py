class devConfig():
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite3'
    SECRET_KEY = 'shhh... its  a secret'

    SECURITY_LOGIN_URL = '/ERTYUJHB3456'
    SECURITY_TOKEN_AUTHENTICATION_HEADER = 'Authorization'

    CACHE_TYPE = 'RedisCache'
    CACHE_REDIS_URL = 'redis://localhost:6379/0'
    CACHE_DEFAULT_TIMEOUT = 300  # seconds
    CACHE_KEY_PREFIX = 'myapp_'

    MAIL_SERVER = 'localhost'
    MAIL_PORT = 1025
    MAIL_DEFAULT_SENDER = 'dontreply@abc.com'

class celeryConfig():
    broker_url = 'redis://localhost:6379/1'
    result_backend = 'redis://localhost:6379/2'
    timezone = 'Asia/Kolkata'