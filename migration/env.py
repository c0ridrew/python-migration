from logging.config import fileConfig

from alembic import context
from database import DATABASE
from models import Base
from sqlalchemy import create_engine

config = context.config
fileConfig(config.config_file_name)
target_metadata = Base.metadata


def run_migrations_online():
    connectable = create_engine(DATABASE)

    context.configure(
        url=DATABASE,
        target_metadata=target_metadata,
        compare_type=True,
    )

    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    raise Exception("No connection to DB")
else:
    run_migrations_online()
