from sqlalchemy import Column, Integer, String

from cpa.adapter import Base


class Provincias(Base):
    __tablename__ = 'provincias'

    codprov = Column(Integer, primary_key=True)
    provincia =  Column(String(50))


class Partidos(Base):
    __tablename__ = 'partidos'

    codpart = Column(Integer, primary_key=True)
    partido =  Column(String(50))
    provincia = Column(String(50))


class Localidad(Base):
    __tablename__ = 'localidad'

    codloc = Column(Integer, primary_key=True)
    localidad =  Column(String(50))
    codpostal =  Column(String(50))
    partido =  Column(String(50))
    provincia = Column(String(50))
    codpart = Column(Integer)


class Calles(Base):
    __tablename__ = 'calles'

    codcalle = Column(Integer, primary_key=True)
    tipocalle =  Column(String(50))
    nombrecalle =  Column(String(50))
    barrio =  Column(String(50))
    referencia =  Column(String(50))
    nombrealt = Column(String(50))
    codloc = Column(Integer)

class Alturas(Base):
    __tablename__ = 'alturas'

    id = Column(Integer, primary_key=True)
    codcalle = Column(Integer)
    desde = Column(Integer)
    hasta = Column(Integer)
    codpostal = Column(String(50))
