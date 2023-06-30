from sqlalchemy import create_engine, MetaData, event
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

# Charger les variables d'environnement à partir du fichier .env
load_dotenv()

# Récupérer la variable d'environnement pour le type de connexion à la base de données
db_connection = os.getenv("DB_CONNECTION")

# Récupérer les autres variables d'environnement pour la connexion à la base de données
db_user = os.getenv("DB_USERNAME")
db_password = os.getenv("DB_PASSWORD")
db_host = os.getenv("DB_HOST")
db_port = os.getenv("DB_PORT")
db_name = os.getenv("DB_DATABASE")

# Construire l'URL de connexion à la base de données en fonction du type de connexion
if db_connection == "mysql":
    SQLALCHEMY_DATABASE_URL = f"mysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
elif db_connection == "postgresql":
    SQLALCHEMY_DATABASE_URL = f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
else:
    raise ValueError("Type de connexion de base de données non pris en charge")


engine = create_engine(SQLALCHEMY_DATABASE_URL)

Base = declarative_base()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()