class Config:
    PORT = True


class ProductionConfig(Config):
    DEBUG = False
    SERVER_NAME = "0.0.0.0:8888"


class DevelopmentConfig(Config):
    DEBUG = True
    PORT = 3333


