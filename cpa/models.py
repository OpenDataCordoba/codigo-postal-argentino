from sqlalchemy import Column, Integer, String, ForeignKey

from cpa.adapter import Base


class Provincias(Base):
    __tablename__ = 'provincias'

    id = Column(Integer, primary_key=True)
    codprov = Column(String(50), unique=True)
    provincia =  Column(String(50))


class Partidos(Base):
    __tablename__ = 'partidos'

    id = Column(Integer, primary_key=True)
    codpart = Column(Integer, unique=True)
    partido =  Column(String(50))
    codprov = Column(String(1), ForeignKey('provincias.codprov'))


class Localidad(Base):
    __tablename__ = 'localidad'

    id = Column(Integer, primary_key=True)
    codloc = Column(Integer, unique=True)
    localidad =  Column(String(50))
    codpostal =  Column(String(50))

    manzana = Column(String(3))
    codprov = Column(String(1), ForeignKey('provincias.codprov'))
    cp = Column(Integer)

    codpart = Column(Integer, ForeignKey('partidos.codpart'))


class Calles(Base):
    __tablename__ = 'calles'

    id = Column(Integer, primary_key=True)
    codcalle = Column(Integer)
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
    manzana = Column(String(3))
    codprov = Column(String(1), ForeignKey('provincias.codprov'))
    cp = Column(Integer)
