from decouple import config


user = config("PGSQL_USER")
password = config("PGSQL_PASSWORD")
host = config("PGSQL_HOST")
database = config("PGSQL_DATABASE")

SECRET_KEY = config("SECRET")

DATABASE_URI_CONNECTION = f'postgresql+psycopg2://{user}:{password}@{host}/{database}'