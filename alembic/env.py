from __future__ import with_statement
import os
import sys
from logging.config import fileConfig

from sqlalchemy import engine_from_config, pool
from sqlalchemy.ext.declarative import declarative_base
from alembic import context

# Ajoutez le chemin de votre application (par exemple, pour accéder à vos modèles)
sys.path.append(os.path.realpath(os.path.join(os.path.dirname(__file__), '..')))

# Importer votre modèle de base de données
from app.database import Base  # Remplacez 'app.database' par le bon chemin de votre fichier
from app.models import User  # Remplacez par vos modèles spécifiques

# Configurez le fichier de configuration
config = context.config

# Configurez le logger
fileConfig(config.config_file_name)

# Accéder à l'object MetaData
target_metadata = Base.metadata  # Base.metadata contient la MetaData de tous vos modèles

# Autres configurations par défaut pour Alembic
def run_migrations_offline():
    """Exécution des migrations en mode hors ligne"""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(url=url, target_metadata=target_metadata, literal_binds=True)
    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    """Exécution des migrations en mode en ligne"""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )
    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)
        with context.begin_transaction():
            context.run_migrations()

# Lancer les migrations
if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
