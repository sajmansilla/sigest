from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relation, sessionmaker
from sqlalchemy import exc
import sys

Base = declarative_base()

class Articulo(Base):
    __tablename__ = 'articulos'

    engine = create_engine('postgresql://sebastian:sebas@localhost/sigest')
    Base.metadata.create_all(engine)

    # Inicio la Session para usar en las transacciones
    Session = sessionmaker(bind = engine)
    session = Session()

    id = Column(String(13),primary_key = True)
    descripcion = Column(String(60), nullable = False)
    alto = Column(Float)
    ancho = Column(Float)
    largo = Column(Float)
    texto = Column(String(200))

    def __init__(self):
        pass

    def __repr__(self):
        return 'Articulo(%r, %r)'%(self.id, self.descripcion)

    def find(self, id):
        try:
            artxid = self.session.query(Articulo).filter(Articulo.id == id).one()
        except:
            artxid = 'No se encontro'
        finally:
            self.session.close()
            return artxid

    def save(self):
        try:
            self.session.add(self)
            self.session.commit()
            salida = 'El Articulo se inserto correctamente.'
        except:
            self.session.rollback()
            salida = 'Hubo un error en la insercion.'
        finally:
            self.session.close()
            return salida

    def dlt(self):
        try:
            self.session.delete(self)
            self.session.commit()
            salida = 'El Articulo se elimino correctamente.'
        except:
            self.session.rollback()
            salida = 'Error eliminando.'
        finally:
            self.session.close()
            return salida

class Deposito(Base):
    __tablename__ = 'depositos'

    engine = create_engine('postgresql://sebastian:sebas@localhost/sigest')
    Base.metadata.create_all(engine)

    # Inicio la Session para usar en las transacciones
    Session = sessionmaker(bind = engine)
    session = Session()

    id = Column(String(13), primary_key = True)
    descripcion = Column(String(50), nullable = False)
    texto = Column(String(200))

    def __init__(self):
        pass

    def __repr__(self):
        return "Deposito(%r,%r)"%(self.id, self.descripcion)

    def find(self, id):
        try:
            depxid = self.session.query(Deposito).filter(Deposito.id == id).one()
        except:
            depxid = 'No se encontro el deposito'
        finally:
            self.session.close()
            return depxid

    def save(self):
        try:
            self.session.add(self)
            self.session.commit()
            salida = 'El Deposito se inserto correctamente.'
        except:
            self.session.rollback()
            salida = 'Error insertando el Deposito.'
        finally:
            self.session.close()
            return salida

    def dlt(self):
        try:
            self.session.delete(self)
            self.session.commit()
            salida = 'El Deposito se elimino correctamente.'
        except:
            self.session.rollback()
            salida = ('Error eliminando el Deposito.')
        finally:
            self.session.close()
            return salida

class Stock(Base):
    __tablename__ = 'stock'

    engine = create_engine('postgresql://sebastian:sebas@localhost/sigest')
    Base.metadata.create_all(engine)

    # Inicio la Session para usar en las transacciones
    Session = sessionmaker(bind = engine)
    session = Session()

    idArt = Column(String(13), ForeignKey('articulos.id'), primary_key = True)
    idDep = Column(String(13), ForeignKey('depositos.id'), primary_key = True)
    stock = Column(Float)

    def __init__(self, idArt, idDep, cantid): # Si se agrega un registro, debe
        self.idArt = idArt                    # estar completo.
        self.idDep = idDep
        self.stock = cantid

    def __repr__(self):
        return 'Stock del Articulo(%r) en Deposito(%r):'%(self.idArt, self.idDep)

    def save(self):
        try:
            self.session.add(self)
            self.session.commit()
            salida = 'El stock se grabo correctamente.'
        except exc.IntegrityError: # as e:
#           self.session.rollback()
#           print(e)
#           salida = e
#           exc_type, exc_value, exc_traceback = sys.exc_info()
#           salida = exc_value
            salida = 'Error registrando el stock. Excepcion de integridad.'
        finally:
            self.session.close()
            return salida

    def find(self, idArt, idDep):
        if (idArt == ''):
            salida = findDepId(idDep)
        elif (idDep == ''):
            salida = findArtId(idArt)
        else:
            try:
                salida = self.session.query(Deposito).filter(
                    Deposito.id == id).one()
            except:
                salida = 'No existe stock del articulo %r en el deposito %r'%(
                    idArt, idDep)
            finally:
                self.session.close()
        return salida
