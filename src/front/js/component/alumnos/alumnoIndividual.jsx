import React, { useContext, useEffect, useState } from "react";
import { Context } from "../../store/appContext";
import { Link, useNavigate, useParams } from "react-router-dom";

export const AlumnoIndividual = () => {
  const { store, actions } = useContext(Context);
  let navegacion = useNavigate();
  const params = useParams();

  useEffect(() => {
    const info = async () => {
      await actions.obtenerAlumnoId(parseInt(params.theid));
     };
    actions.obtenerMutualistaId(parseInt(params.theidMutualista));
    info();
  }, []);

  return (
    <>
      <div className="container">
        <h3 style={{ marginBottom: "25px", color: "red" }}>
          {store.alumno[0]?.nombre} {store.alumno[0]?.apellido} - {store.alumno[0]?.cuotasInfo.descripcion}
        </h3>
        <hr />
        <br />

        <p>Motivo del entrenamiento: <b>{store.alumno[0]?.motivoentrenamiento}</b></p>
        <br />
        <div className="container text-left">
          <div className="row">
            <div className="col-sm-4">
              {/* Foto */}
              <img
                src={store.alumno[0]?.foto}
                className="img-fluid rounded-circle"
              />
            </div>

            <div className="col-sm-3">
              {/* Datos personales */}
              
              <p>
                Cédula:{" "}
                <b>
                  {store.alumno[0]?.cedula}
                </b>
              </p>
              <p>
                Dirección: <b>{store.alumno[0]?.direccion}</b>
              </p>
              <p>
                Fecha de ingreso: <b>{store.alumno[0]?.fechaingreso}</b>
              </p>
              <p>Altura: <b>{store.alumno[0]?.altura}</b>. Peso: <b>{store.alumno[0]?.peso} kg.</b></p>
              <p>Condiciones médicas: <b>{store.alumno[0]?.condicionesmedicas}</b></p> 
              <p>Emergencias al: <b>{store.alumno[0]?.emergencias}</b></p> 
              <p>Comentarios: <b>{store.alumno[0]?.observaciones}</b></p> 
            </div>

            <div className="col-sm-5">
              {/* Datos personales */}
              
              <p>
                Celular:{" "}
                <b>
                  {store.alumno[0]?.celular}
                </b>
              </p>
              <p>
                Correo electrónico: <b>{store.alumno[0]?.email}</b>
              </p>
              <p>
                Fecha de nacimiento: <b>{store.alumno[0]?.fechanacimiento}</b>
              </p>
              <p>Mutualista: <b>{store.mutualista.nombre}</b></p>
              <p>Médicamentos: <b>{store.alumno[0]?.medicacion}</b></p> 
              <p>Mensualidad: <b style={{color: "red"}}>$ {store.alumno[0]?.cuotasInfo.precio}</b></p> 
            </div>

          </div>
        </div>

        <hr />
<br />
        <h3 style={{ marginBottom: "25px"}}>
          Mensualidades abonadas
        </h3>
        

        <div style={{ marginTop: "35px" }}>
          <table className="table" style={{ color: "white" }}>
            <thead>
              <tr>
                <th scope="col">Fecha</th>
                <th scope="col">Monto</th>
                <th scope="col">Factura</th>
                <th scope="col">Medio de pago</th>
                {/* <th scope="col"></th> */}
              </tr>
            </thead>
            {/* <tbody>
              {store.mutualistas.map((item, id) => ( 
                <tr key={id}>
                  <td>{item.nombre}</td>
                  <td>{item.direccion}</td>
                  <td>{item.telefono}</td>
                  <td>
                    <Link to={"/ModificarMutualista/" + item.id} style={{color: "white"}}> 
                      <i className="fa fa-pen"></i>
                     </Link>
                  </td>
                  <td>
                    <i
                      className="fa fa-trash"
                     onClick={(e) => borrar(e, item.id)}
                    >
                    </i>
                  </td>
                </tr>
              ))}
            </tbody> */}
          </table>
        </div>
     
 
      </div>
    </>
  );
};
