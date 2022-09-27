from typing import List

from sqlalchemy import create_engine
from sqlalchemy import insert
from sqlalchemy.orm import Session

import config
from repository.models import Projection

DATABASE_URI = 'postgresql+psycopg2://%s:%s@%s:%s/%s' % (config.SQL_DB_USERNAME,
                                                        config.SQL_DB_PASSWORD,
                                                        config.SQL_DB_HOSTNAME,
                                                        config.SQL_DB_PORT,
                                                        config.SQL_DB_DBNAME)

db_engine = create_engine(DATABASE_URI, echo = True)
db_connection = db_engine.connect()


def create_tables_if_not_exist():
    if not db_engine.dialect.has_table(db_connection, Projection.__table__):
        Projection.__table__.create(db_engine)

def insert_projections(projections: List[Projection]):

    with Session(db_engine) as session:

        for projection in projections:
            session.add(projection)

        session.commit()

create_tables_if_not_exist()
