from my_app import app
from config import DevelopmentConfig

# print(app.default_config)
app.config.from_object("config.DevelopmentConfig")
# print(app.config)


if __name__ == "__main__":
#    app.run(port=DevelopmentConfig.PORT)
    app.run()