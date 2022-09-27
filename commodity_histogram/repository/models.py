from sqlalchemy import Column, Numeric, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Projection(Base):
    __tablename__   =   'projection'
    id              =   Column(Integer,             primary_key=True)
    Attribute       =   Column('attribute',         String(255))
    Commodity       =   Column('commodity',         String(255))
    CommodityType   =   Column('commodity_type',    String(255))
    Units           =   Column('Units',             String(255))
    YearType        =   Column('year_type',         String(255))
    Year            =   Column(Numeric)
    Value           =   Column(Float)
