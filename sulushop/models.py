from sulushop import db
from sqlalchemy.orm import relationship

db.Model.metadata.reflect(db.engine)


class Usuario(db.Model):
    __table__ = db.Model.metadata.tables['usuario']


class Carro(db.Model):
    __table__ = db.Model.metadata.tables['carro']


class Foto(db.Model):
    __table__ = db.Model.metadata.tables['foto']


class Producto(db.Model):
    __table__ = db.Model.metadata.tables['producto']


class FotoProducto(db.Model):
    __table__ = db.Model.metadata.tables['foto_producto']


class Lista(db.Model):
    __table__ = db.Model.metadata.tables['lista']
