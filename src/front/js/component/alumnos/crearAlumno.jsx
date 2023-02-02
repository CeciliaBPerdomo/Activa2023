import React, { useContext, useEffect, useState } from "react";
import { Context } from "../../store/appContext";
import { Link, useNavigate } from "react-router-dom";
import { toast, ToastContainer } from "react-toastify";
import "react-toastify/dist/ReactToastify.css";

export const CrearAlumno = () => {
  const { store, actions } = useContext(Context);
  let navegacion = useNavigate();

  useEffect(() => {
    actions.obtenerCuotas();
    actions.obtenerMutualistas();
  }, []);

  return (
    <>
      <div className="container">
        <h3 style={{ marginBottom: "25px" }}>Ingresar alumnos</h3>
        <hr />
        <br />

        <form>
          <div className="row">
            <div className="col">
              <label htmlFor="cedula" style={{ marginBottom: "10px" }}>
                Cédula:
              </label>
              <input
                type="text"
                className="form-control"
                placeholder="Cédula (sin puntos ni guiones)"
                // value={descripcion}
                // onChange={(e) => setDescripcion(e.target.value)}
              />
            </div>

            <div className="col">
              <label htmlFor="nombre" style={{ marginBottom: "10px" }}>
                Nombre:
              </label>
              <input
                type="text"
                className="form-control"
                placeholder="Nombre"
                // value={precio}
                // onChange={(e) => setPrecio(e.target.value)}
              />
            </div>

            <div className="col">
              <label htmlFor="apellido" style={{ marginBottom: "10px" }}>
                Apellido:
              </label>
              <input
                type="text"
                className="form-control"
                placeholder="Apellido"
                // value={precio}
                // onChange={(e) => setPrecio(e.target.value)}
              />
            </div>
          </div>

          <br />
          <div className="row">
            <div className="col">
              <label htmlFor="direccion" style={{ marginBottom: "10px" }}>
                Dirección:
              </label>
              <input
                type="text"
                className="form-control"
                placeholder="Dirección"
                // value={descripcion}
                // onChange={(e) => setDescripcion(e.target.value)}
              />
            </div>

            <div className="col">
              <label htmlFor="Celular" style={{ marginBottom: "10px" }}>
                Celular:
              </label>
              <input
                type="text"
                className="form-control"
                placeholder="Celular"
                // value={precio}
                // onChange={(e) => setPrecio(e.target.value)}
              />
            </div>

            <div className="col">
              <label htmlFor="fecha" style={{ marginBottom: "10px" }}>
                Fecha de nacimiento:
              </label>
              <input
                type="date"
                className="form-control"
                placeholder="Fecha de nacimiento"
                // value={descripcion}
                // onChange={(e) => setDescripcion(e.target.value)}
              />
            </div>
          </div>

          <br />
          <div className="row">
            <div className="col">
              <label htmlFor="Peso" style={{ marginBottom: "10px" }}>
                Peso:
              </label>
              <input
                type="text"
                className="form-control"
                placeholder="Peso"
                // value={precio}
                // onChange={(e) => setPrecio(e.target.value)}
              />
            </div>

            <div className="col">
              <label htmlFor="Altura" style={{ marginBottom: "10px" }}>
                Altura:
              </label>
              <input
                type="text"
                className="form-control"
                placeholder="Altura"
                // value={precio}
                // onChange={(e) => setPrecio(e.target.value)}
              />
            </div>

            <div className="col">
              <label htmlFor="fechaI" style={{ marginBottom: "10px" }}>
                Fecha de ingreso:
              </label>
              <input
                type="date"
                className="form-control"
                placeholder="Fecha de ingreso"
                // value={descripcion}
                // onChange={(e) => setDescripcion(e.target.value)}
              />
            </div>
          </div>

          <br />
          <div className="row">
            <div className="col">
              <label htmlFor="mail" style={{ marginBottom: "10px" }}>
                Correo electrónico:
              </label>
              <input
                type="text"
                className="form-control"
                placeholder="Correo electrónico"
                // value={precio}
                // onChange={(e) => setPrecio(e.target.value)}
              />
            </div>

            <div className="col">
              <label htmlFor="foto" style={{ marginBottom: "10px" }}>
                Foto:
              </label>
              <input
                type="text"
                className="form-control"
                placeholder="Foto (URL)"
                // value={precio}
                // onChange={(e) => setPrecio(e.target.value)}
              />
            </div>

            <div className="col">
              <label htmlFor="mutualista" style={{ marginBottom: "10px" }}>
                Mutualista:
              </label>
              <select
                className="form-select"
                aria-label="Default select example"
              >
                <option selected>Mutualista</option>
                {store.mutualistas.map((item, id) => (
                  <option key={id} value={item.id}>{item.nombre}</option>
                ))}
              </select>
            </div>
          </div>

          <br />
          <div className="row">
            <div className="col">
              <label htmlFor="condiciones" style={{ marginBottom: "10px" }}>
                Condiciones médicas:
              </label>
              <input
                type="text"
                className="form-control"
                placeholder="Condiciones médicas"
                // value={descripcion}
                // onChange={(e) => setDescripcion(e.target.value)}
              />
            </div>

            <div className="col">
              <label htmlFor="medicacion" style={{ marginBottom: "10px" }}>
                Medicación:
              </label>
              <input
                type="text"
                className="form-control"
                placeholder="Si toma algún médicamento"
                // value={precio}
                // onChange={(e) => setPrecio(e.target.value)}
              />
            </div>

            <div className="col">
              <label htmlFor="emergencias" style={{ marginBottom: "10px" }}>
                Emergencias:
              </label>
              <input
                type="text"
                className="form-control"
                placeholder="Telefono en caso de emergencia"
                // value={precio}
                // onChange={(e) => setPrecio(e.target.value)}
              />
            </div>
          </div>

          <br />
          <div className="row">
            <div className="col">
              <label htmlFor="motivo" style={{ marginBottom: "10px" }}>
                Motivo del entrenamiento:
              </label>
              <input
                type="text"
                className="form-control"
                placeholder="Motivo del entrenamiento"
                // value={precio}
                // onChange={(e) => setPrecio(e.target.value)}
              />
            </div>

            <div className="col">
              <label htmlFor="entrenamiento" style={{ marginBottom: "10px" }}>
                Modalidad:
              </label>
              <select
                className="form-select"
                aria-label="Default select example"
              >
                <option>Modalidad</option>
                {store.cuotas.map((item, id) => (
                  <option
                    key={id}
                    //value={item.id}
                  >
                    {item.descripcion}
                  </option>
                ))}
              </select>
            </div>

            <div className="col">
              <label htmlFor="mensualidad" style={{ marginBottom: "10px" }}>
                Mensualidad:
              </label>
              <input
                type="text"
                className="form-control"
                placeholder="Mensualidad"
                disabled
                // value={precio}
                // onChange={(e) => setPrecio(e.target.value)}
              />
            </div>
          </div>

          <br />
          <div style={{ marginTop: "15px" }}>
            <button
              type="submit"
              className="btn btn-outline-danger float-end w-25"
              //onClick={(e) => guardar(e)}
            >
              Agregar
            </button>
          </div>
        </form>

        <ToastContainer />
      </div>
    </>
  );
};
