import React, { useContext, useEffect, useState } from "react";
import { Context } from "../../store/appContext";
import { useNavigate } from "react-router-dom";
import { useParams } from "react-router-dom";
import { toast, ToastContainer } from "react-toastify";
import "react-toastify/dist/ReactToastify.css";

export const ModificarMutualistas = () => {
  const params = useParams();
  const { store, actions } = useContext(Context);
  let navegacion = useNavigate();

  const [nombre, setNombre] = useState(store.mutualista.nombre)
  const [direccion, setDireccion] = useState(store.mutualista.direccion)
  const [telefono, setTelefono] = useState(store.mutualista.telefono)

  useEffect(() => {
    actions.obtenerMutualistaId(parseInt(params.theid));
  }, []);

  const modificar = (e) => {
    e.preventDefault();
    let id = parseInt(params.theid);

    if (actions.modificarMutualista(id, nombre, direccion, telefono)) {
      toast.success("💪 Modificación realizada con éxito", {
        position: toast.POSITION.TOP_RIGHT,
        autoClose: 3000,
        hideProgressBar: false,
        closeOnClick: true,
        pauseOnHover: true,
        draggable: true,
        progress: undefined,
        theme: "dark",
      });

      // setInterval(() => {
      //   navegacion("/Mutualista");
      // }, 5000);
    }
  };


  return (
    <>
      <div className="container">
        <h3 style={{ marginBottom: "15px" }}>
          Modificación de las Mutualistas
        </h3>
        <hr />
        <br />

        {/* Formulario de alta */}
        <form>

          <div className="row">
            <div className="col">
              <label htmlFor="Nombre:" style={{ marginBottom: "10px" }}>
                Nombre:
              </label>
              <input
                type="text"
                className="form-control"
                placeholder="Nombre"
                defaultValue={store.mutualista.nombre}
                onChange={(e) => setNombre(e.target.value)}
              />
            </div>
          </div>

          <br />
          <div className="row">
            <div className="col">
              <label htmlFor="Direccion" style={{ marginBottom: "10px" }}>
                Dirección:
              </label>
              <input
                type="text"
                className="form-control"
                placeholder="Dirección"
                defaultValue={store.mutualista.direccion}
                onChange={(e) => setDireccion(e.target.value)}
              />
            </div>
          </div>

          <br />
          <div className="row">
            <div className="col">
              <label htmlFor="Telefono" style={{ marginBottom: "10px" }}>
                Teléfono:
              </label>
              <input
                type="text"
                className="form-control"
                placeholder="Teléfono"
                defaultValue={store.mutualista.telefono}
                onChange={(e) => setTelefono(e.target.value)}
              />
            </div>
          </div>

          <br />
          <div className="row">
            <div style={{ marginTop: "15px" }}>
              <button
                type="submit"
                className="btn btn-outline-danger float-end w-25"
                onClick={(e) => modificar(e)}
              >
                Actualizar
              </button>
            </div>
          </div>
        </form>
      </div>
      <ToastContainer />
      <br />
    </>
  );
};
