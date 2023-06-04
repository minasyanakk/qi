# coding: utf-8
from sqlalchemy import Column, MetaData, Table
from sqlalchemy.sql.sqltypes import NullType

metadata = MetaData()


t_catalog_catalog = Table(
    'catalog_catalog', metadata,
    Column('AUTHOR', NullType),
    Column('BORN-DIED', NullType),
    Column('TITLE', NullType),
    Column('DATE', NullType),
    Column('TECHNIQUE', NullType),
    Column('LOCATION', NullType),
    Column('URL', NullType),
    Column('FORM', NullType),
    Column('TYPE', NullType),
    Column('SCHOOL', NullType),
    Column('TIMEFRAME', NullType)
)
