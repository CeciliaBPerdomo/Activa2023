import React, { useContext, useEffect, useState } from "react";
import { Context } from "../../store/appContext";
import { useNavigate } from "react-router-dom";
import { useParams } from "react-router-dom";
import { toast, ToastContainer } from "react-toastify";
import "react-toastify/dist/ReactToastify.css";

export const CrearProductos = () => {
  const params = useParams();
  const { store, actions } = useContext(Context);
  let navegacion = useNavigate();

  const [nombre, setNombre] = useState("");
  const [cantidad, setCantidad] = useState("");
  const [precioVenta, setPrecioVenta] = useState("");
  const [foto, setFoto] = useState("");
  const [video, setVideo] = useState("");
  const [observaciones, setObservaciones] = useState("")
  const [proveedor, setProveedor] = useState("")

  useEffect(() => {
    actions.obtenerProveedores();
  }, []);

  const guardar = (e) => {
    e.preventDefault();

    if (
      actions.crearProductos(
        nombre,
        cantidad,
        precioVenta,
        observaciones,
        foto,
        video,
        proveedor,
      )
    ) {
      toast.success("💪 Guardado con éxito", {
        position: toast.POSITION.TOP_RIGHT,
        autoClose: 3000,
        hideProgressBar: false,
        closeOnClick: true,
        pauseOnHover: true,
        draggable: true,
        progress: undefined,
        theme: "dark",
      });
    }

    setNombre("")
    setCantidad("")
    setPrecioVenta("")
    setObservaciones("")
    setFoto("")
    setVideo("")
    setProveedor("")
    // setInterval(() => {
    //   navegacion("/ListadoAlumnos");
    // }, 5000);
  };

  return (
    <>
      <div className="container">
        <h3 style={{ marginBottom: "15px" }}>
          Ingresar un nuevo productos
        </h3>
        <hr />
        <br />

        <form>
          <div className="row">
            {/* Nombre */}
            <div className="col">
              <label htmlFor="nombre" style={{ marginBottom: "10px" }}>
                Nombre:
              </label>
              <input
                type="text"
                className="form-control"
                placeholder="Nombre"
                value={nombre}
                onChange={(e) => setNombre(e.target.value)}
              />
            </div>

            {/* Cantidad */}
            <div className="col">
              <label htmlFor="cantidad" style={{ marginBottom: "10px" }}>
                Cantidad:
              </label>
              <input
                type="text"
                className="form-control"
                placeholder="Cantidad"
                value={cantidad}
                onChange={(e) => setCantidad(e.target.value)}
              />
            </div>

            {/* Precio venta */}
            <div className="col">
              <label htmlFor="precio" style={{ marginBottom: "10px" }}>
                Precio de venta:
              </label>
              <input
                type="text"
                className="form-control"
                placeholder="Precio de venta"
                value={precioVenta}
                onChange={(e) => setPrecioVenta(e.target.value)}
              />
            </div>
          </div>

          <br />
          <div className="row">
            {/* Foto */}
            <div className="col">
              <label htmlFor="nombre" style={{ marginBottom: "10px" }}>
                Foto URL:
              </label>
              <input
                type="text"
                className="form-control"
                placeholder="URL de la foto"
                value={foto}
                onChange={(e) => setFoto(e.target.value)}
              />
            </div>

            {/* Video */}
            <div className="col">
              <label htmlFor="cantidad" style={{ marginBottom: "10px" }}>
                Video:
              </label>
              <input
                type="text"
                className="form-control"
                placeholder="URL del video"
                value={video}
                onChange={(e) => setVideo(e.target.value)}
              />
            </div>
          </div>

          <br />
          <div className="row">
            {/* Provedor */}
            <div className="col">
              <label htmlFor="proveedor" style={{ marginBottom: "10px" }}>
                Proveedor:
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
            </div>

            {/* Observaciones */}
            <div className="col">
              <label htmlFor="observaciones" style={{ marginBottom: "10px" }}>
                Observaciones:
              </label>
              <input
                type="text"
                className="form-control"
                placeholder="Observaciones"
                value={observaciones}
                onChange={(e) => setObservaciones(e.target.value)}
              />
            </div>
          </div>
          <br />
          <div style={{ marginTop: "15px" }}>
            <button
              type="submit"
              className="btn btn-outline-danger float-end w-25"
              onClick={(e) => guardar(e)}
            >
              Agregar
            </button>
          </div>
        </form>
      </div>
      <ToastContainer />
      <br />
    </>
  );
};
