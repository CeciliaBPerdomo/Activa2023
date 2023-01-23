from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return f'<User {self.email}>'

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

#####################################################################################
#####################################################################################
###                                                                               ###
###                     USUARIOS                                                  ###
###                                                                               ###
#####################################################################################
#####################################################################################
class Usuarios(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cedula = db.Column(db.Integer, unique=True, nullable=False)
    nombre = db.Column(db.String(50), unique=False, nullable=False)
    apellido = db.Column(db.String(50), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    fechanacimiento = db.Column(db.Date, unique=False)
    condicionesmedicas = db.Column(db.String(200))
    medicacion = db.Column(db.String(200))
    emergencias = db.Column(db.String(15))
    password = db.Column(db.String(20), unique=False, nullable=False)
    rol = db.Column(db.String(15))
    motivoentrenamiento = db.Column(db.String(200))
    observaciones = db.Column(db.String(500))
    foto = db.Column(db.String(500))
    celular = db.Column(db.String(15))
    peso = db.Column(db.Double)
    altura = db.Column(db.Double)
    fechaingreso  =  db.Column(db.Date, unique=False)
    activo  = db.Column(db.Boolean(), unique=False, nullable=False)
    
    # FK
    cuota = db.Column(db.Integer, db.ForeignKey("cuota.id"))
    mutualista = db.Column(db.Integer, db.ForeignKey("mutualista.id"))

    mensualidades = db.relationship('Mensualidades', backref="mensualidades", cascade="all, delete-orphan", lazy=True)

    def __repr__(self):
        return f'<Usuario {self.cedula}>'

    def serialize(self):
        return {
            "id": self.id,
            "cedula": self.cedula,
            "nombre": self.nombre,
            "apellido": self.apellido, 
            "email": self.email,
            "fechanacimiento": self.fechanacimiento,
            "condicionesmedicas": self.condicionesmedicas, 
            "medicacion": self.medicacion, 
            "emergencias": self.emergencias, 
            "rol": self.rol,
            "motivoentrenamiento": self.motivoentrenamiento, 
            "observaciones": self.observaciones, 
            "foto": self.foto,
            "celular": self.celular,
            "peso": self.peso,
            "altura": self.altura,
            "fechaingreso": self.fechaingreso,
            "activo": self.activo,
            "cuota": self.cuota,
            "mutualista": self.mutualista,
        }

    def serializeCuotas(self):
        results = Cuota.query.filter_by(id = self.id).first()
        return {
            "cuotasInfo": results.serialize(),
        }

    def serializeMutualista(self):
        results = Mutualista.query.filter_by(id = self.id).first()
        return {
            "mutualistaInfo": results.serialize(),
        }

#####################################################################################
#####################################################################################
###                                                                               ###
###                     FACTURACION                                               ###
###                                                                               ###
#####################################################################################
#####################################################################################

## Cuota: segun el tipo de entrenamiento, el valor de la cuota
class Cuota(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    descripcion = db.Column(db.String(150), unique=False, nullable=False)
    precio = db.Column(db.Double)

    # FK 
    cuota = db.relationship('Cuota', backref="cuota", cascade="all, delete-orphan", lazy=True)

    def __repr__(self):
        return f'<Cuota {self.id}>'

    def serialize(self):
        return {
            "id": self.id,
            "descripcion": self.descripcion,
            "precio": self.precio
        }

## Mensualidades: pago mensual de los alumnos
class Mensualidades(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fechapago = db.Column(db.Date)
    monto = db.Column(db.Double)
    factura = db.Column(db.Integer)
    observaciones = db.Column(db.String(250))

    # FK 
    idusuario = db.Column(db.Integer, db.ForeignKey("usuarios.id"))
    idmetodo = db.Column(db.Integer, db.ForeignKey("metodopago.id"))

    def __repr__(self):
        return f'<Mensualidades {self.id}>'

    def serialize(self):
        return {
            "id": self.id,
            "fechapago": self.fechapago,
            "monto": self.monto,
            "factura": self.factura,
            "observaciones": self.observaciones, 
            "idusuario": self.idusuario,
            "idmetodo": self.idmetodo
        }
    
    def serializeMetodo(self):
        results = MetodosPago.query.filter_by(id = self.id).first()
        return {
            "metodosInfo": results.serialize(),
        }

# Metodos de pago: Efectivo, pos, transferencia bancaria
class MetodosPago(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String(50), unique=False, nullable=False)
    observaciones = db.Column(db.String(100), unique=False)

    # FK 
    metodospago = db.relationship('MetodosPago', backref="metodospago", cascade="all, delete-orphan", lazy=True)

    def __repr__(self):
        return f'<MetodosPago {self.tipo}>'

    def serialize(self):
        return {
            "id": self.id,
            "tipo": self.tipo,
            "observaciones": self.observaciones
        }

## Mutualista: mutualistas a las cuales pueden pertenecer
class Mutualista(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), unique=False, nullable=False)
    direccion = db.Column(db.String(120), unique=False)
    telefono = db.Column(db.String(50), unique=False)

    # FK 
    mutualista = db.relationship('Mutualista', backref="mutualista", cascade="all, delete-orphan", lazy=True)

    def __repr__(self):
        return f'<Mutualista {self.tipo}>'

    def serialize(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "direccion": self.direccion,
            "telefono": self.telefono
        }