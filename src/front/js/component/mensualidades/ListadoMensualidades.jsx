import React, { useContext, useEffect, useState } from "react";
import { Context } from "../../store/appContext";
import { Link, useNavigate } from "react-router-dom";
import { toast, ToastContainer } from "react-toastify";
import "react-toastify/dist/ReactToastify.css";

export const ListadoMensualidades = () => {
    const { store, actions } = useContext(Context);
    let navegacion = useNavigate();

    useEffect(() => {
       actions.obtenerMensualidades()
      }, []);

      return (
        <>
          <div className="container">
            <h3 style={{ marginBottom: "25px" }}>Pago de mensualidades</h3>
            <hr />
            <br />

            
            <ToastContainer />
      </div>
    </>
  );
};