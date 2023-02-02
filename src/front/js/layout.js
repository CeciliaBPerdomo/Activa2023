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

                        <Route element={<h1>Not found!</h1>} />
                    </Routes>
                    <Footer />
                </ScrollToTop>
            </BrowserRouter>
        </div>
    );
};

export default injectContext(Layout);
