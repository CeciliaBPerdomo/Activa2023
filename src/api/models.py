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
    peso = db.Column(db.String(10))
    altura = db.Column(db.String(10))
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
    precio = db.Column(db.String(10))

    # FK 
#    cuota = db.relationship('Cuota', backref="cuota", cascade="all, delete-orphan", lazy=True)

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
    monto = db.Column(db.String(10))
    factura = db.Column(db.Integer)
    observaciones = db.Column(db.String(250))

    # FK 
    idusuario = db.Column(db.Integer, db.ForeignKey("usuarios.id"))
    idmetodo = db.Column(db.Integer, db.ForeignKey("metodospago.id"))

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
        results = Metodospago.query.filter_by(id = self.id).first()
        return {
            "metodosInfo": results.serialize(),
        }

# Metodos de pago: Efectivo, pos, transferencia bancaria
class Metodospago(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String(50), unique=False, nullable=False)
    observaciones = db.Column(db.String(100), unique=False)

    # FK 
    # metodospago = db.relationship('MetodosPago', backref="metodospago", cascade="all, delete-orphan", lazy=True)

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
    # mutualista = db.relationship('Mutualista', backref="mutualista", cascade="all, delete-orphan", lazy=True)

    def __repr__(self):
        return f'<Mutualista {self.tipo}>'

    def serialize(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "direccion": self.direccion,
            "telefono": self.telefono
        }

#####################################################################################
#####################################################################################
###                                                                               ###
###                PROVEEDORES Y PRODUCTOS                                        ###
###                                                                               ###
#####################################################################################
#####################################################################################

# Proveedores
class Proveedores(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), unique=False, nullable=False)
    rut = db.Column(db.String(12), unique=True, nullable=True)
    direccion = db.Column(db.String(120), unique=False)
    telefono = db.Column(db.String(50), unique=False)
    mail = db.Column(db.String(120), unique=False)
    observaciones = db.Column(db.String(120), unique=False)

    # FK 
   # proveedores = db.relationship('Proveedores', backref="proveedores", cascade="all, delete-orphan", lazy=True)

    def __repr__(self):
        return f'<Proveedores {self.nombre}>'

    def serialize(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "rut": self.rut,
            "direccion": self.direccion,
            "telefono": self.telefono, 
            "mail": self.mail,
            "observaciones": self.observaciones, 
        }


# Pago a proveedores
class Pagoproveedores(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fechapago = db.Column(db.Date)
    numfactura = db.Column(db.Integer)
    monto = db.Column(db.String(10))
    observaciones = db.Column(db.String(120), unique=False)

    # FK 
    idproveedor = db.Column(db.Integer, db.ForeignKey("proveedores.id"))
    idmetodo = db.Column(db.Integer, db.ForeignKey("metodospago.id"))

    def __repr__(self):
        return f'<Pagoproveedores {self.id}>'

    def serialize(self):
        return {
            "id": self.id,
            "fechapago": self.fechapago,
            "numfactura": self.numfactura,
            "monto": self.monto,
            "observaciones": self.observaciones, 
            "idproveedor": self.idproveedor, 
            "idmetodo": self.idmetodo,
        }

    def serializeMetodo(self):
        results = MetodosPago.query.filter_by(id = self.id).first()
        return {
            "metodosInfo": results.serialize(),
        }
    
    def serializeProveedor(self):
        results = Proveedores.query.filter_by(id = self.id).first()
        return {
            "proveedorInfo": results.serialize(),
        }

# Productos
class Productos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(120), nullable=False)
    cantidad = db.Column(db.Integer, nullable=False)
    precioventa = db.Column(db.String(10))
    foto = db.Column(db.String(500), unique=False)
    video = db.Column(db.String(500), unique=False)
    observaciones = db.Column(db.String(500), unique=False)

    # FK 
    # productos = db.relationship('Productos', backref="productos", cascade="all, delete-orphan", lazy=True)    

    def __repr__(self):
        return f'<Productos {self.nombre}>'

    def serialize(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "cantidad": self.cantidad,
            "precioventa": self.precioventa,
            "observaciones": self.observaciones, 
            "foto": self.foto, 
            "video": self.video,
        }

# Compras
class Compras(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    preciocompra = db.Column(db.String(10))
    fecha = db.Column(db.Date)
    cantidad = db.Column(db.Integer, nullable=False)
    observaciones = db.Column(db.String(500), unique=False)

    # FK 
    idproducto = db.Column(db.Integer, db.ForeignKey("productos.id"))
    idproveedor = db.Column(db.Integer, db.ForeignKey("proveedores.id"))
    idmetodo = db.Column(db.Integer, db.ForeignKey("metodospago.id"))

    def __repr__(self):
        return f'<Compras {self.id}>'

    def serialize(self):
        return {
            "id": self.id,
            "preciocompra": self.preciocompra,
            "fecha": self.fecha,
            "cantidad": self.cantidad,
            "observaciones": self.observaciones, 
            "idproducto": self.idproducto, 
            "idproveedor": self.idproveedor,
            "idmetodo": self.idmetodo,
        }

    def serializeMetodo(self):
        results = Metodospago.query.filter_by(id = self.id).first()
        return {
            "metodosInfo": results.serialize(),
        }
    
    def serializeProveedor(self):
        results = Proveedores.query.filter_by(id = self.id).first()
        return {
            "proveedorInfo": results.serialize(),
        }

# Ventas
class Ventas(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fechacompra = db.Column(db.Date)
    cantidad = db.Column(db.Integer, nullable=False)
    preciounitario = db.Column(db.String(10))
    observaciones = db.Column(db.String(250), unique=False)
    fechapago  = db.Column(db.Date)

    # FK 
    idproducto = db.Column(db.Integer, db.ForeignKey("productos.id"))
    idmetodo = db.Column(db.Integer, db.ForeignKey("metodospago.id"))
    idusuario = db.Column(db.Integer, db.ForeignKey("usuarios.id"))

    def __repr__(self):
        return f'<Ventas {self.id}>'

    def serialize(self):
        return {
            "id": self.id,
            "fechacompra": self.fechacompra,
            "cantidad": self.cantidad,
            "preciounitario": self.preciounitario,
            "observaciones": self.observaciones, 
            "fechapago": self.fechapago,
            "idproducto": self.idproducto, 
            "idusuario": self.idusuario,
            "idmetodo": self.idmetodo,
        }

    def serializeMetodo(self):
        results = Metodospago.query.filter_by(id = self.id).first()
        return {
            "metodosInfo": results.serialize(),
        }
    
    def serializeProveedor(self):
        results = Proveedores.query.filter_by(id = self.id).first()
        return {
            "proveedorInfo": results.serialize(),
        }

    def serializeUsuario(self):
        results = Usuarios.query.filter_by(id = self.id).first()
        return {
            "usuariosInfo": results.serialize(),
        }

#####################################################################################
#####################################################################################
###                                                                               ###
###                CAJAS                                                          ###
###                                                                               ###
#####################################################################################
#####################################################################################

# CajaDiaria
class CajaDiaria(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.Date)
    totalmensualidades = db.Column(db.Integer, nullable=False)
    cantidadalumnos = db.Column(db.Integer)
    totalventas = db.Column(db.Integer)
    totalpagoprov  = db.Column(db.Integer)
    observaciones = db.Column(db.String(250), unique=False)

    def __repr__(self):
        return f'<CajaDiaria {self.id}>'

    def serialize(self):
        return {
            "id": self.id,
            "fecha": self.fecha,
            "totalmensualidades": self.totalmensualidades,
            "cantidadalumnos": self.cantidadalumnos,
            "observaciones": self.observaciones, 
            "totalventas": self.totalventas,
            "totalpagoprov": self.totalpagoprov, 
        }

# Caja Mensual
class CajaMensual(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.Date)
    totalmensualidades = db.Column(db.Integer, nullable=False)
    cantidadalumnos = db.Column(db.Integer)
    totalventas = db.Column(db.Integer)
    totalpagoprov  = db.Column(db.Integer)
    observaciones = db.Column(db.String(250), unique=False)

    def __repr__(self):
        return f'<CajaMensual {self.id}>'

    def serialize(self):
        return {
            "id": self.id,
            "fecha": self.fecha,
            "totalmensualidades": self.totalmensualidades,
            "cantidadalumnos": self.cantidadalumnos,
            "observaciones": self.observaciones, 
            "totalventas": self.totalventas,
            "totalpagoprov": self.totalpagoprov, 
        }

# Caja Anual
class CajaAnual(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.Date)
    totalmensualidades = db.Column(db.Integer, nullable=False)
    cantidadalumnos = db.Column(db.Integer)
    totalventas = db.Column(db.Integer)
    totalpagoprov  = db.Column(db.Integer)
    observaciones = db.Column(db.String(250), unique=False)

    def __repr__(self):
        return f'<CajaAnual {self.id}>'

    def serialize(self):
        return {
            "id": self.id,
            "fecha": self.year,
            "totalmensualidades": self.totalmensualidades,
            "cantidadalumnos": self.cantidadalumnos,
            "observaciones": self.observaciones, 
            "totalventas": self.totalventas,
            "totalpagoprov": self.totalpagoprov, 
        }

#####################################################################################
#####################################################################################
###                                                                               ###
###                EJERCICIOS Y RUTINAS                                           ###
###                                                                               ###
#####################################################################################
#####################################################################################

#Tipo de Ejercicios
class Tipoejercicio(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    descripcion = db.Column(db.String(250))

    def __repr__(self):
        return f'<Tipoejercicio {self.id}>'

    def serialize(self):
        return {
            "id": self.id,
            "descripcion": self.descripcion,
        }

# Ejercicios
class Ejercicio(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))
    descripcion = db.Column(db.String(1000))
    foto = db.Column(db.String(250))
    video = db.Column(db.String(250))

    #FK 
    tipo = db.Column(db.Integer, db.ForeignKey("tipoejercicio.id"))

    def __repr__(self):
        return f'<Ejercicio {self.id}>'

    def serialize(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "descripcion": self.descripcion,
            "tipo": self.tipo,
            "foto": self.foto, 
            "video": self.video,
        }

    def serializeTipoEjercicio(self):
        results = Tipoejercicio.query.filter_by(id = self.id).first()
        return {
            "tipoEjerciciosInfo": results.serialize(),
        }

# Rutinas
class Rutina(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fechacomienzo = db.Column(db.Date)
    fechafinalizacion = db.Column(db.Date)

    #FK
    idusuario = db.Column(db.Integer, db.ForeignKey("usuarios.id"))
    
    def __repr__(self):
        return f'<Rutina {self.id}>'

    def serialize(self):
        return {
            "id": self.id,
            "idusuario": self.idusuario,
            "fechacomienzo": self.fechacomienzo,
            "fechafinalizacion": self.fechafinalizacion,
        }

    def serializeUsuario(self):
        results = Usuarios.query.filter_by(id = self.id).first()
        return {
            "UsuariosInfo": results.serialize(),
        }

# Rutinas Auxiliar
class RutinasAux(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    serie = db.Column(db.Integer)
    carga = db.Column(db.Integer)
    repeticiones = db.Column(db.Integer)
    semana = db.Column(db.Integer)

    #FK 
    idrutina = db.Column(db.Integer, db.ForeignKey("rutina.id"))
    idejercicio = db.Column(db.Integer, db.ForeignKey("ejercicio.id"))

    def __repr__(self):
        return f'<RutinasAux {self.idrutina}>'

    def serialize(self):
        return {
            "id": self.id,
            "idrutina": self.idrutina,
            "idejercicio": self.idejercicio,
            "serie": self.serie,
            "carga": self.carga,
            "repeticiones": self.repeticiones,
            "semana": self.semana,
        }

    def serializeEjercicio(self):
        results = Ejercicio.query.filter_by(id = self.id).first()
        return {
            "EjerciciosInfo": results.serialize(),
        }

#####################################################################################
#####################################################################################
###                                                                               ###
###                         VENTAS ONLINE                                         ###
###                                                                               ###
#####################################################################################
#####################################################################################

# Carrito
class Carrito(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    idcarrito = db.Column(db.Integer)
    cantidad = db.Column(db.Integer)
    estado = db.Column(db.String(15))

    #FK
    idusuario = db.Column(db.Integer, db.ForeignKey("usuarios.id"))
    idproductos = db.Column(db.Integer, db.ForeignKey("productos.id"))
    
    def __repr__(self):
        return f'<Carrito {self.id}>'

    def serialize(self):
        return {
            "id": self.id,
            "idcarrito": self.idcarrito,
            "cantidad": self.cantidad,
            "estado": self.estado,
            "idusuario": self.idusuario,
            "idproductos": self.idproductos,
        }

    def serializeUsuario(self):
        results = Usuarios.query.filter_by(id = self.id).first()
        return {
            "UsuariosInfo": results.serialize(),
        }

    def serializeProductos(self):
        results = Productos.query.filter_by(id = self.id).first()
        return {
            "ProductoInfo": results.serialize(),
        }

# Ventas On-Line
class Ventasonline(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fechapago = db.Column(db.Date)
    observaciones = db.Column(db.String(150))

    #FK
    idusuario = db.Column(db.Integer, db.ForeignKey("usuarios.id"))
    idcarrito = db.Column(db.Integer, db.ForeignKey("carrito.id"))
    idmetodo = db.Column(db.Integer, db.ForeignKey("metodospago.id"))

    
    def __repr__(self):
        return f'<Ventasonline {self.id}>'

    def serialize(self):
        return {
            "id": self.id,
            "idcarrito": self.idcarrito,
            "fechapago": self.fechapago,
            "observaciones": self.observaciones,
            "idusuario": self.idusuario,
            "idmetodo": self.idmetodo,
        }

    def serializeUsuario(self):
        results = Usuarios.query.filter_by(id = self.id).first()
        return {
            "UsuariosInfo": results.serialize(),
        }

    def serializeProductos(self):
        results = Productos.query.filter_by(id = self.id).first()
        return {
            "ProductoInfo": results.serialize(),
        }
    
    def serializeMetodo(self):
        results = Metodospago.query.filter_by(id = self.id).first()
        return {
            "metodosInfo": results.serialize(),
        }