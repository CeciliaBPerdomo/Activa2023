import React, { useContext, useEffect, useState } from "react";
import { Context } from "../../store/appContext";
import { Link, useNavigate } from "react-router-dom";
import { toast, ToastContainer } from "react-toastify";
import "react-toastify/dist/ReactToastify.css";

export const CrearPagoProveedor = () => {
  const { store, actions } = useContext(Context);

  const [busqueda, setBusqueda] = useState("");
  const [proveedor, setProveedor] = useState("");
  const [fechaPago, setFechaPago] = useState("");
  const [factura, setFactura] = useState("");
  const [monto, setMonto] = useState("");
  const [idmetodo, setIdMetodo] = useState("");

  useEffect(() => {
    actions.obtenerProveedores();
    actions.obtenerMetodos();
  }, []);

  return (
    <>
      <div className="container">
        <div className="input-group mb-3 w-25 float-end">
          <input
            type="text"
            className="form-control "
            placeholder="🔎 Buscar pago de proveedor..."
            onChange={(e) => setBusqueda(e.target.value)}
            value={busqueda}
          />
          <button
            className="btn btn-outline-danger"
            type="button"
            id="button-addon2"
            // onClick={(e) => buscar(busqueda)}
          >
            Buscar
          </button>
        </div>

        <h3 style={{ marginBottom: "25px" }}>Ingresar pago de proveedores</h3>
        <hr />
        <br />

        <form>
          <div className="row">
            {/* Proveedor */}
            <div className="col">
              <label htmlFor="idProvedor" style={{ marginBottom: "10px" }}>
                Id de Proveedor:
              </label>
              <select
                className="form-select"
                aria-label="Default select example"
                value={proveedor}
                onChange={(e) => setProveedor(e.target.value)}
              >
                <option selected>Proveedor</option>
                {store.proveedores.map((item, id) => (
                  <option key={id} value={item.id}>{item.nombre}</option>
                ))}
              </select>
              {
                /* <input
                type="text"
                className="form-control"
                placeholder="Descripción"
                //value={descripcion}
                //onChange={(e) => setDescripcion(e.target.value)}
              /> */
              }
            </div>

            {/* Fecha de pago */}
            <div className="col">
              <label htmlFor="fecha" style={{ marginBottom: "10px" }}>
                Fecha de pago:
              </label>
              <input
                type="date"
                className="form-control"
                placeholder="Fecha de pago"
                value={fechaPago}
                onChange={(e) => setFechaPago(e.target.value)}
              />
            </div>

            {/* Numero de factura */}
            <div className="col">
              <label htmlFor="factura" style={{ marginBottom: "10px" }}>
                Factura:
              </label>
              <input
                type="text"
                className="form-control"
                placeholder="Número de factura"
                value={factura}
                onChange={(e) => setFactura(e.target.value)}
              />
            </div>
          </div>

          <br />
          <div className="row">
            {/* Monto */}
            <div className="col">
              <label htmlFor="monto" style={{ marginBottom: "10px" }}>
                Monto:
              </label>
              <input
                type="text"
                className="form-control"
                placeholder="Monto de la factura"
                value={monto}
                onChange={(e) => setMonto(e.target.value)}
              />
            </div>

            {/* Metodo de pago */}
            <div className="col">
              <label htmlFor="metodo" style={{ marginBottom: "10px" }}>
                Método de pago:
              </label>
              <select
                className="form-select"
                value={idmetodo}
                onChange={(e) => setIdMetodo(e.target.value)}
              >
                <option selected>Método de pago</option>
                {store.metodos.map((item, id) => (
                  <option key={id} value={item.id}>{item.tipo}</option>
                ))}
              </select>
            </div>
          </div>
          <br />

          
        </form>
      </div>
      <ToastContainer />
      <br />
    </>
  );
};
