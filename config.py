from environs import Env


env = Env()

# You can set up all your environment variables for the app to ease local development in an .env file instead of
# storing them in pycharm or using exports. See here for details: https://github.com/sloria/environs#reading-env-files
env.read_env()


def get_postgres_db_url(user: str, password: str, host: str, port: str, db_name: str = ''):
    scheme = 'postgresql://'
    return f'{scheme}{user}:{password}@{host}:{port}/{db_name}'


class AppConfig:
    DB_PORT = env.str('DB_PORT', "5432")
    DB_USER = env.str('DB_USER', 'postgres')
    DB_PASSWORD = env.str('DB_PASSWORD', 'example')
    DB_HOST = env.str('DB_HOST', 'localhost')
    DB_NAME = env.str('DB_NAME', 'k8s_workshop')
    SQLALCHEMY_DATABASE_URI = get_postgres_db_url(user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port=DB_PORT, db_name=DB_NAME)

