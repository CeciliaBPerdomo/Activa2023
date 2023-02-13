import React from "react";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import ScrollToTop from "./component/scrollToTop";

import { Home } from "./pages/home";
import injectContext from "./store/appContext";

import { Navbar } from "./component/navbar";
import { Footer } from "./component/footer";


// Cuotas
import { CrearCuota } from "./component/cuotas/crearCuota.jsx";
import { ModificarCuota } from "./component/cuotas/modificarCuota.jsx"

//Metodos de pago
import { CrearMetodos } from "./component/metodospago/crearMetodos.jsx"
import { ModificarMetodos } from "./component/metodospago/modificarMetodos.jsx"

// Mutualista
import { CrearMutualista } from "./component/mutualista/crearMutualista.jsx"
import { ModificarMutualistas } from "./component/mutualista/modificarMutualista.jsx"

// Alumnos
import { CrearAlumno } from "./component/alumnos/crearAlumno.jsx"
import { ListaAlumnos } from "./component/alumnos/listaAlumnos.jsx"
import { AlumnoIndividual } from "./component/alumnos/alumnoIndividual.jsx"
import { ModificarAlumno } from "./component/alumnos/modificarAlumno.jsx"

// Mensualidades
import { ListadoMensualidades } from "./component/mensualidades/ListadoMensualidades.jsx"
import { CrearMensualidad } from "./component/mensualidades/crearMensualidades.jsx"
import { ModificarMensualidad } from "./component/mensualidades/modificarMensualidades.jsx"

//create your first component
const Layout = () => {
    //the basename is used when your project is published in a subdirectory and not in the root of the domain
    // you can set the basename on the .env file located at the root of this project, E.g: BASENAME=/react-hello-webapp/
    const basename = process.env.BASENAME || "";

    return (
        <div>
            <BrowserRouter basename={basename}>
                <ScrollToTop>
                    <Navbar />
                    <Routes>
                        <Route element={<Home />} path="/" />

                        {/* Cuotas */}
                        <Route element={<CrearCuota />} path="/CrearCuota" />
                        <Route element={<ModificarCuota />} path="/ModificarCuota/:theid" />

                        {/* Metodos de pagos */}
                        <Route element={<CrearMetodos />} path="/MetodosPago" />
                        <Route element={<ModificarMetodos />} path="/ModificarMetodos/:theid" />

                        {/* Mutualista */}
                        <Route element={<CrearMutualista />} path="/Mutualista" />
                        <Route element={<ModificarMutualistas />} path="/ModificarMutualista/:theid" />

                        {/* Alumnos */}
                        <Route element={<CrearAlumno />} path="/CrearAlumno" />
                        <Route element={<ListaAlumnos />} path="/ListadoAlumnos" />
                        <Route element={<AlumnoIndividual />} path="/AlumnoIndividual/:theid/:theidMutualista" />
                        <Route element={<ModificarAlumno />} path="/ModificarAlumno/:theid" />

                        {/* Mensualidades */}
                        <Route element={<CrearMensualidad />} path="/CrearMensualidad" />
                        <Route element={<ListadoMensualidades />} path="/ListadoMensualidades" />
                        <Route element={<ModificarMensualidad />} path="/ModificarMensualidad/:theid" />

                        <Route element={<h1>Not found!</h1>} />
                    </Routes>
                    <Footer />
                </ScrollToTop>
            </BrowserRouter>
        </div>
    );
};

export default injectContext(Layout);
