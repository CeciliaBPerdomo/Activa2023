"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint

from api.models import db, Usuarios, Cuota, Mensualidades, Metodospago, Mutualista, Proveedores, Pagoproveedores
from api.models import Productos, Compras, Ventas, CajaDiaria, CajaMensual, CajaAnual, Tipoejercicio, Ejercicio
from api.models import Rutina, RutinasAux, Carrito, Ventasonline

from api.utils import generate_sitemap, APIException
import json

api = Blueprint('api', __name__)

@api.route('/hello', methods=['POST', 'GET'])
def handle_hello():

    response_body = {
        "message": "Hello! I'm a message that came from the backend, check the network tab on the google inspector and you will see the GET request"
    }

    return jsonify(response_body), 200

#####################################################################################
#####################################################################################
###                                                                               ###
###                        CUOTAS                                                 ###
###                                                                               ###
#####################################################################################
#####################################################################################

# Muestra todas las cuotas
@api.route('/cuota', methods=['GET'])
def getCuota():
    
    cuotas = Cuota.query.all()
    results = list(map(lambda x: x.serialize(), cuotas))
    return jsonify(results), 200

# Alta de un cuota
@api.route('/cuota', methods=['POST'])
def addCuota():
    body = json.loads(request.data)

    queryNewCuota = Cuota.query.filter_by(descripcion=body["descripcion"]).first()
    if queryNewCuota is None:
        new_cuota = Cuota(descripcion=body["descripcion"],
        precio=body["precio"])

        db.session.add(new_cuota)
        db.session.commit()

        return jsonify(new_cuota.serialize()), 200
    
    response_body = {"msg": "Usuario ya creado"}
    return jsonify(response_body), 400

# Eliminacion de una cuota
@api.route('/cuota/<int:cuota_id>', methods=['DELETE'])
def deleteCuota(cuota_id):
    cuotaId = Cuota.query.filter_by(id=cuota_id).first()
  
    if cuotaId is None: 
        response_body = {"msg": "Id de cuota no encontrada"}
        return jsonify(response_body), 400

    db.session.delete(cuotaId)
    db.session.commit()
    response_body = {"msg": "Cuota borrada"}
    return jsonify(response_body), 200 

# Modifica una cuota por id
@api.route('/cuota/<int:cuota_id>', methods=['PUT'])
def modificarCuota(cuota_id):
    cuota = Cuota.query.filter_by(id=cuota_id).first()
    body = json.loads(request.data)

    if cuota is None:
        response_body = {"msg": "No existe la cuota"}
        return jsonify(response_body), 400    

    if "descripcion" in body:
        cuota.descripcion =  body["descripcion"]

    if "precio" in body:
        cuota.precio = body["precio"]
    
    db.session.commit()
    response_body = {"msg": "Cuota modificada"}
    return jsonify(response_body), 200

# Muestra la cuota por id
@api.route('/cuota/<int:cuota_id>', methods=['GET'])
def get_cuota(cuota_id):
    id = Cuota.query.filter_by(id=cuota_id).first()

    if id is None: 
        response_body = {"msg": "Cuota no encontrado"}
        return jsonify(response_body), 400

    cuota = id.serialize()
    return jsonify(cuota), 200

#####################################################################################
#####################################################################################
###                                                                               ###
###                     METODOS DE PAGO                                           ###
###                                                                               ###
#####################################################################################
#####################################################################################

# Muestra todos los metodos de pagos
@api.route('/metodos', methods=['GET'])
def getMetodos():
    metodos = Metodospago.query.all()
    results = list(map(lambda x: x.serialize(), metodos))
    return jsonify(results), 200

# Alta de un metodos de pago
@api.route('/metodos', methods=['POST'])
def addMetodo():
    body = json.loads(request.data)

    queryNewMetodo = Metodospago.query.filter_by(tipo=body["tipo"]).first()
    if queryNewMetodo is None:
        new_metodo = Metodospago(tipo=body["tipo"],
        observaciones=body["observaciones"])

        db.session.add(new_metodo)
        db.session.commit()

        return jsonify(new_metodo.serialize()), 200
    
    response_body = {"msg": "Metodo de pago ya creado"}
    return jsonify(response_body), 400

# Eliminacion de un metodo de pago
@api.route('/metodos/<int:metodos_id>', methods=['DELETE'])
def deleteMetodos(metodos_id):
    MetodosId = Metodospago.query.filter_by(id=metodos_id).first()
  
    if MetodosId is None: 
        response_body = {"msg": "Id de metodo de pago no encontrada"}
        return jsonify(response_body), 400

    db.session.delete(MetodosId)
    db.session.commit()
    response_body = {"msg": "Metodo de pago borrado"}
    return jsonify(response_body), 200 

# Modifica un metodo de pago por id
@api.route('/metodos/<int:metodos_id>', methods=['PUT'])
def modificarMetodos(metodos_id):
    metodos = Metodospago.query.filter_by(id=metodos_id).first()
    body = json.loads(request.data)

    if metodos is None:
        response_body = {"msg": "No existe el metodo de pago"}
        return jsonify(response_body), 400    

    if "tipo" in body:
        metodos.tipo =  body["tipo"]

    if "observaciones" in body:
        metodos.observaciones = body["observaciones"]
    
    db.session.commit()
    response_body = {"msg": "Metodo de pago modificado"}
    return jsonify(response_body), 200

# Muestra el metodo de pago por id
@api.route('/metodos/<int:metodo_id>', methods=['GET'])
def get_metodo(metodo_id):
    id = Metodospago.query.filter_by(id=metodo_id).first()

    if id is None: 
        response_body = {"msg": "Metodo de pago no encontrado"}
        return jsonify(response_body), 400

    metodo = id.serialize()
    return jsonify(metodo), 200

#####################################################################################
#####################################################################################
###                                                                               ###
###                     MUTUALISTAS                                               ###
###                                                                               ###
#####################################################################################
#####################################################################################

# Muestra todos las mutualistas
@api.route('/mutualistas', methods=['GET'])
def getMutualistas():
    mutualista = Mutualista.query.all()
    results = list(map(lambda x: x.serialize(), mutualista))
    return jsonify(results), 200

# Alta de una mutualista
@api.route('/mutualistas', methods=['POST'])
def addMutualista():
    body = json.loads(request.data)

    queryNewMutualista = Mutualista.query.filter_by(nombre=body["nombre"]).first()
    
    if queryNewMutualista is None:
        new_mutualista = Mutualista(nombre=body["nombre"],
        direccion=body["direccion"],
        telefono=body["telefono"])

        db.session.add(new_mutualista)
        db.session.commit()

        return jsonify(new_mutualista.serialize()), 200
    
    response_body = {"msg": "Mutualista existente"}
    return jsonify(response_body), 400

# Eliminacion de una mutualista
@api.route('/mutualistas/<int:mutualista_id>', methods=['DELETE'])
def deleteMutualista(mutualista_id):
    id = Mutualista.query.filter_by(id=mutualista_id).first()
  
    if id is None: 
        response_body = {"msg": "Id de mutualista no encontrada"}
        return jsonify(response_body), 400

    db.session.delete(id)
    db.session.commit()
    response_body = {"msg": "Mutualista borrada"}
    return jsonify(response_body), 200 

# Modifica una mutualista
@api.route('/mutualistas/<int:mutualista_id>', methods=['PUT'])
def modificarMutualista(mutualista_id):
    mutualista = Mutualista.query.filter_by(id=mutualista_id).first()
    body = json.loads(request.data)

    if mutualista is None:
        response_body = {"msg": "No existe la mutualista"}
        return jsonify(response_body), 400    

    if "nombre" in body:
        mutualista.nombre =  body["nombre"]

    if "direccion" in body:
        mutualista.direccion = body["direccion"]

    if "telefono" in body:
        mutualista.telefono = body["telefono"]
    
    db.session.commit()
    response_body = {"msg": "Mutualista modificada"}
    return jsonify(response_body), 200

# Muestra la mutualista por id
@api.route('/mutualistas/<int:mutualista_id>', methods=['GET'])
def get_mutualista(mutualista_id):
    id = Mutualista.query.filter_by(id=mutualista_id).first()

    if id is None: 
        response_body = {"msg": "Mutualista no encontrada"}
        return jsonify(response_body), 400

    return jsonify(id.serialize()), 200

#####################################################################################
#####################################################################################
###                                                                               ###
###                     ALUMNOS                                                   ###
###                                                                               ###
#####################################################################################
#####################################################################################

# Muestra todos los alumnos
@api.route('/alumnos', methods=['GET'])
def getAlumos():
    alumnos = Usuarios.query.all()
    results = list(map(lambda x: {**x.serializeCuotas(), **x.serialize()}, alumnos))
    return jsonify(results), 200

# Alta de un alumno 
@api.route('/alumnos', methods=['POST'])
def addAlumnos():
    body = json.loads(request.data)

    queryNewAlumno = Usuarios.query.filter_by(cedula=body["cedula"]).first()
    
    if queryNewAlumno is None:
        new_alumno = Usuarios(
        cedula=body["cedula"],
        nombre=body["nombre"],
        apellido=body["apellido"],
        direccion=body["direccion"],
        celular=body["celular"],
        fechanacimiento=body["fechanacimiento"],
        peso=body["peso"],
        altura=body["altura"], 
        fechaingreso=body["fechaingreso"],
        password=body["cedula"], 
        email=body["email"], 
        idmutualista=body["idmutualista"],
        condicionesmedicas=body["condicionesmedicas"], 
        medicacion=body["medicacion"],
        emergencias=body["emergencias"], 
        motivoentrenamiento=body["motivoentrenamiento"],
        idcuota=body["idcuota"],
        rol=body["rol"],
        activo=body["activo"],
        observaciones=body["observaciones"],
        )

        db.session.add(new_alumno)
        db.session.commit()

        return jsonify(new_alumno.serialize()), 200
    
    response_body = {"msg": "Este usuario ya existente"}
    return jsonify(response_body), 400

# Elimina un alumno
@api.route('/alumnos/<int:alumno_id>', methods=['DELETE'])
def deleteAlumno(alumno_id):
    id = Usuarios.query.filter_by(id=alumno_id).first()
  
    if id is None: 
        response_body = {"msg": "Id de alumno no encontrado"}
        return jsonify(response_body), 400

    db.session.delete(id)
    db.session.commit()

    response_body = {"msg": "Alumno borrado"}
    return jsonify(response_body), 200 

# Muestra el alumno por id
@api.route('/alumnos/<int:alumno_id>', methods=['GET'])
def get_alumnoind(alumno_id):
    alumno = Usuarios.query.filter_by(id=alumno_id).all()
    results = list(map(lambda x: {**x.serializeCuotas(), **x.serialize()}, alumno))

    if results is None: 
        response_body = {"msg": "Usuario no encontrado"}
        return jsonify(response_body), 400

    return jsonify(results), 200

# Modifica un usuario por id
@api.route('/alumnos/<int:user_id>', methods=['PUT'])
def usersModif_porId(user_id):
    usuario = Usuarios.query.filter_by(id=user_id).first()
    body = json.loads(request.data)

    if usuario is None:
        response_body = {"msg": "No existe el usuario"}
        return jsonify(response_body), 400    

    if "cedula" in body:
        usuario.cedula =  body["cedula"]
       # usuario.password = body["cedula"]

    if "nombre" in body: 
        usuario.nombre = body["nombre"]

    if "apellido" in body:
        usuario.apellido = body["apellido"]

    if "direccion" in body: 
        usuario.direccion = body["direccion"]
    
    if "celular" in body:
        usuario.celular = body["celular"]

    if "fechanamiento" in body:
        usuario.fechanacimiento = body["fechanacimiento"]
    
    if "peso" in body: 
        usuario.peso = body["peso"]
    
    if "altura" in body:
        usuario.altura = body["altura"]

    if "fechaingreso" in body:
        usuario.fechaingreso = body["fechaingreso"]
    
    if "email" in body:
        usuario.email = body["email"]

    if "idmutualista" in body: 
        usuario.idmutualista = body["idmutualista"]
    
    if "condicionesmedicas" in body:
        usuario.condicionesmedicas=body["condicionesmedicas"]
    
    if "medicacion" in body:
        usuario.medicacion = body["medicacion"]
    
    if "emergencias" in body:
        usuario.emergencias = body["emergencias"]
    
    if "motivoentrenamiento" in body:
        usuario.motivoentrenamiento = body["motivoentrenamiento"]
    
    if "idcuota" in body:
        usuario.idcuota = body["idcuota"]
    
    if "rol"in body:
        usuario.rol = body["rol"]
    
    if "activo" in body:
        usuario.activo = body["activo"]
    
    if "observaciones" in body:
        usuario.observaciones = body["observaciones"]

    db.session.commit()

    response_body = {"msg": "Usuario modificado"}
    return jsonify(response_body), 200

#####################################################################################
#####################################################################################
###                                                                               ###
###                   PAGO DE MENSUALIDADES                                       ###
###                                                                               ###
#####################################################################################
#####################################################################################
# Muestra todos los pagos
@api.route('/mensualidades', methods=['GET'])
def getMensualidades():
    mensualidades = Mensualidades.query.all()
    results = list(map(lambda x: {**x.serializeAlumnos(), **x.serialize()}, mensualidades))
    return jsonify(results), 200

# Alta de un pago
@api.route('/mensualidades', methods=['POST'])
def addMensualidades():
    body = json.loads(request.data)

    queryNewMensulidades = Mensualidades.query.filter_by(factura=body["factura"]).first()
    if queryNewMensulidades is None:
        new_mensualidad = Mensualidades(fechapago=body["fechapago"],
        monto=body["monto"],
        factura=body["factura"],
        observaciones=body["observaciones"],
        idusuario=body["idusuario"],
        idmetodo=body["idmetodo"])

        db.session.add(new_mensualidad)
        db.session.commit()

        return jsonify(new_mensualidad.serialize()), 200
    
    response_body = {"msg": "factura ya ingresada cabezita!"}
    return jsonify(response_body), 400

# Elimina un pago
@api.route('/mensualidades/<int:mensualidad_id>', methods=['DELETE'])
def deleteMensualidad(mensualidad_id):
    pago = Mensualidades.query.filter_by(id=mensualidad_id).first()
  
    if pago is None: 
        response_body = {"msg": "Pago no encontrado"}
        return jsonify(response_body), 400

    db.session.delete(pago)
    db.session.commit()

    response_body = {"msg": "Pago borrado"}
    return jsonify(response_body), 200 

# Modifica un pago id
@api.route('/mensualidades/<int:mensualidad_id>', methods=['PUT'])
def mensualidadModif_porId(mensualidad_id):
    pago = Mensualidades.query.filter_by(id=mensualidad_id).first()
    body = json.loads(request.data)

    if pago is None:
        response_body = {"msg": "No existe el pago"}
        return jsonify(response_body), 400    

    if "fechapago" in body:
        pago.fechapago = body["fechapago"]
    
    if "monto" in body:
        pago.monto = body["monto"]
    
    if "factura" in body:
        pago.factura = body["factura"]
    
    if "observaciones" in body:
        pago.observaciones = body["observaciones"]
    
    if "idusuario" in body:
        pago.idusuario = body["idusuario"]
    
    if "idmetodo" in body: 
        pago.idmetodo=body["idmetodo"]
    
    db.session.commit()

    response_body = {"msg": "Pago de mensualidad modificado"}
    return jsonify(response_body), 200

# Muestra el pago de la mensualidad por id de pago
@api.route('/mensualidades/<int:mensualidad_id>', methods=['GET'])
def get_mensualidadid(mensualidad_id):
    pago = Mensualidades.query.filter_by(id=mensualidad_id).all()
    results = list(map(lambda x: {**x.serializeAlumnos(), **x.serialize()}, pago))

    if results is None: 
        response_body = {"msg": "Mensualidad no encontrada"}
        return jsonify(response_body), 400

    return jsonify(results), 200

# Muestra el pago de la mensualidad por id de usuario
@api.route('/mensualidadesAlumno/<int:idusuario>', methods=['GET'])
def pago_mensualidad_id(idusuario):
    pago = Mensualidades.query.filter_by(idusuario=idusuario).all()
    results = list(map(lambda x: {**x.serializeMetodo(), **x.serialize()}, pago))

    if results is None: 
        response_body = {"msg": "Mensualidad no encontrada"}
        return jsonify(response_body), 400

    return jsonify(results), 200


#####################################################################################
#####################################################################################
###                                                                               ###
###                   PRODUCTOS                                                   ###
###                                                                               ###
#####################################################################################
#####################################################################################
# Muestra todos los productos
@api.route('/productos', methods=['GET'])
def getProductos():
    products = Productos.query.all()
    results = list(map(lambda x: {**x.serializeProveedor(), **x.serialize()}, products))
    return jsonify(results), 200

# Alta de un producto
@api.route('/productos', methods=['POST'])
def addProductos():
    body = json.loads(request.data)

    new_producto = Productos(
    nombre = body ["nombre"], 
    cantidad = body["cantidad"],
    precioventa = body["precioventa"],
    observaciones = body["observaciones"], 
    foto = body["foto"],
    video  = body["video"],
    proveedorid =  body["proveedorid"])

    db.session.add(new_producto)
    db.session.commit()

    return jsonify(new_producto.serialize()), 200

# Elimina un producto
@api.route('/productos/<int:productos_id>', methods=['DELETE'])
def deleteProducto(productos_id):
    producto = Productos.query.filter_by(id=productos_id).first()
  
    if producto is None: 
        response_body = {"msg": "Producto no encontrado"}
        return jsonify(response_body), 400

    db.session.delete(producto)
    db.session.commit()

    response_body = {"msg": "Producto borrado"}
    return jsonify(response_body), 200 

# Modifica un producto por id
@api.route('/productos/<int:producto_id>', methods=['PUT'])
def productoModif_porId(producto_id):
    producto = Productos.query.filter_by(id=producto_id).first()
    body = json.loads(request.data)

    if producto is None:
        response_body = {"msg": "No existe el producto"}
        return jsonify(response_body), 400    

    if "nombre" in body: 
        producto.nombre = body["nombre"]

    if "cantidad" in body: 
        producto.cantidad = body["cantidad"]
    
    if "precioventa" in body: 
        producto.precioventa = body["precioventa"]
    
    if "observaciones" in body:
        producto.observaciones = body["observaciones"]
    
    if "foto" in body:
        producto.foto = body["foto"]
    
    if "video" in body:
        producto.video  = body["video"]
    
    if "proveedorid" in body:
        producto.proveedorid =  body["proveedorid"]

    db.session.commit()

    response_body = {"msg": "Producto modificado"}
    return jsonify(response_body), 200

# Muestra el producto por id
@api.route('/productos/<int:producto_id>', methods=['GET'])
def get_productoid(producto_id):
    products = Productos.query.filter_by(id=producto_id).all()
    results = list(map(lambda x: {**x.serializeProveedor(), **x.serialize()}, products))

    if results is None: 
        response_body = {"msg": "Producto no encontrado"}
        return jsonify(response_body), 400

    return jsonify(results), 200

#####################################################################################
#####################################################################################
###                                                                               ###
###                   PROVEEDORES                                                 ###
###                                                                               ###
#####################################################################################
#####################################################################################
# Muestra todos los proveedores
@api.route('/proveedores', methods=['GET'])
def getProveedores():
    proveedores = Proveedores.query.all()
    results = list(map(lambda x: x.serialize(), proveedores))
    return jsonify(results), 200

# Alta de un proveedor
@api.route('/proveedores', methods=['POST'])
def addProveedores():
    body = json.loads(request.data)

    new_proveedor = Proveedores(
    nombre = body ["nombre"], 
    rut = body["rut"],
    direccion = body["direccion"],
    telefono = body["telefono"],
    mail  = body["mail"],
    observaciones = body["observaciones"])

    db.session.add(new_proveedor)
    db.session.commit()

    return jsonify(new_proveedor.serialize()), 200

# Elimina un proveedor
@api.route('/proveedores/<int:proveedor_id>', methods=['DELETE'])
def deleteProveedor(proveedor_id):
    proveedor = Proveedores.query.filter_by(id=proveedor_id).first()
  
    if proveedor is None: 
        response_body = {"msg": "Proveedor no encontrado"}
        return jsonify(response_body), 400

    db.session.delete(proveedor)
    db.session.commit()

    response_body = {"msg": "Proveedor borrado"}
    return jsonify(response_body), 200 


# Modifica un proveedor por id
@api.route('/proveedores/<int:proveedores_id>', methods=['PUT'])
def proveedorModif_porId(proveedores_id):
    proveedor = Proveedores.query.filter_by(id=proveedores_id).first()
    body = json.loads(request.data)

    if proveedor is None:
        response_body = {"msg": "No existe el proveedor."}
        return jsonify(response_body), 400    

    if "nombre" in body: 
        proveedor.nombre = body["nombre"]

    if "rut" in body: 
        proveedor.rut = body["rut"]
    
    if "direccion" in body: 
        proveedor.direccion = body["direccion"]
    
    if "telefono" in body:
        proveedor.telefono = body["telefono"]
    
    if "mail" in body:
        proveedor.mail  = body["mail"]
    
    if "observaciones" in body:
        proveedor.observaciones = body["observaciones"]

    db.session.commit()

    response_body = {"msg": "Proveedor modificado"}
    return jsonify(response_body), 200

# Muestra el proveedor por id
@api.route('/proveedores/<int:proveedor_id>', methods=['GET'])
def get_proveedorid(proveedor_id):
    proveedor = Proveedores.query.filter_by(id=proveedor_id).all()
    results = list(map(lambda x: x.serialize(), proveedor))

    if results is None: 
        response_body = {"msg": "Proveedor no encontrado"}
        return jsonify(response_body), 400

    return jsonify(results), 200

#####################################################################################
#####################################################################################
###                                                                               ###
###                   PAGO PROVEEDORES                                            ###
###                                                                               ###
#####################################################################################
#####################################################################################
# Alta de un pago de proveedor
@api.route('/pagoproveedores', methods=['POST'])
def addPagoProveedores():
    body = json.loads(request.data)

    new_pagoproveedor = Pagoproveedores(
    fechapago = body ["fechapago"], 
    numfactura = body["numfactura"],
    monto = body["monto"],
    observaciones = body["observaciones"],
    idproveedor = body["idproveedor"],
    idmetodo  = body["idmetodo"])

    db.session.add(new_pagoproveedor)
    db.session.commit()

    return jsonify(new_pagoproveedor.serialize()), 200