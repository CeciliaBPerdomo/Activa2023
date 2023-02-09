import React, { useContext, useEffect, useState } from "react";
import { Context } from "../../store/appContext";
import { Link, useNavigate } from "react-router-dom";
import { toast, ToastContainer } from "react-toastify";
import "react-toastify/dist/ReactToastify.css";

export const CrearMensualidad = () => {
    const { store, actions } = useContext(Context);
    let navegacion = useNavigate();

    useEffect(() => {
        actions.obtenerAlumnos();
        actions.obtenerMetodos()
      }, []);

      return (
        <>
          <div className="container">
            <h3 style={{ marginBottom: "25px" }}>Ingresar nuevo pago de mensualidad</h3>
            <hr />
            <br />

            <form>
                <div className="row">
                    {/* Alumno */}
                    <div className="col">
                    <label htmlFor="alumno" style={{ marginBottom: "10px" }}>
                        Alumno:
                    </label>
                    <select className="form-select" aria-label="Default select example">
                        <option selected>Alumno</option>
                        {store.alumnos.map((item,id) => (
                        <option key={id} value={item.id}>{item.nombre} {item.apellido}</option>
                        ))}
                    </select>
                    </div>

                    {/* Fecha de pago */}
                    <div className="col">
                    <label htmlFor="fecha" style={{ marginBottom: "10px" }}>
                        Fecha de pago:
                    </label>
                    <input
                        type="date"
                        className="form-control"
                        //defaultValue={store.alumno[0]?.fechanacimiento}
                        //onChange={(e) => setFechaNacimiento(e.target.value)}
                    />
                    </div>
                </div>

                <br /> 
                <div className="row">
                    {/* Monto */}
                    <div className="col">
                        <label htmlFor="Monto" style={{ marginBottom: "10px" }}>
                            Monto:
                        </label>
                        <input
                            type="text"
                            className="form-control"
                            placeholder="Monto"
                            //defaultValue={store.alumno[0]?.peso}
                            //onChange={(e) => setPeso(e.target.value)}
                        />
                    </div>

                    {/* Factura */}
                    <div className="col">
                        <label htmlFor="Monto" style={{ marginBottom: "10px" }}>
                            Factura No.:
                        </label>
                        <input
                            type="text"
                            className="form-control"
                            placeholder="Número de factura"
                            //defaultValue={store.alumno[0]?.peso}
                            //onChange={(e) => setPeso(e.target.value)}
                        />
                    </div>

                    {/* Alumno */}
                    <div className="col">
                    <label htmlFor="alumno" style={{ marginBottom: "10px" }}>
                        Metodo de pago:
                    </label>
                    <select className="form-select" aria-label="Default select example">
                        <option selected>Metodo</option>
                        {store.metodos.map((item,id) => (
                        <option key={id} value={item.id}>{item.tipo}</option>
                        ))}
                    </select>
                    </div>
                </div>

                <br />
                <div className="row">
                     {/* Observaciones */}
                    <div className="col">
                        <label htmlFor="observaciones" style={{ marginBottom: "10px" }}>
                            Observaciones:
                        </label>
                        <input
                            type="text"
                            className="form-control"
                            placeholder="Observaciones"
                            //defaultValue={store.alumno[0]?.observaciones}
                            //onChange={(e) => setObservaciones(e.target.value)}
                        />
                    </div>
                </div>

                <br />
                <div style={{ marginTop: "15px"}}>
                    <button
                    type="submit"
                    className="btn btn-outline-danger float-end w-25"
                    // onClick={(e) => modificar(e)}
                    >
                    Guardar
                    </button>
                </div>
            </form>

            <ToastContainer />
      </div>
    </>
  );
};