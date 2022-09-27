from sqlalchemy import create_engine, Column, Numeric, Integer, String, Boolean, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Projection(Base):
    __tablename__   =   'projection'
    id              =   Column(Integer,             primary_key=True)
    attribute       =   Column('attribute',         String(255))
    commodity       =   Column('commodity',         String(255))
    commodity_type  =   Column('commodity_type',    String(255))
    units           =   Column('Units',             String(255))
    year_type       =   Column('year_type',         String(255))
    year            =   Column(Numeric)
    value           =   Column(Float)
