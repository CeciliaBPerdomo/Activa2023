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
###                     FACTURACION                                               ###
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