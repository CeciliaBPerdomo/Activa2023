import axios from "axios";
let direccion = process.env.BACKEND_URL;

const getState = ({ getStore, getActions, setStore }) => {
  return {
    store: {
      cuotas: [],
      cuota: {},
    },
    actions: {
      // Cuotas
      obtenerCuotas: async () => {
        try {
          const response = await axios.get(direccion + "/api/cuota", {});
          setStore({
            cuotas: response.data,
          });
        } catch (error) {
          console.log(error);
          if (error.code === "ERR_BAD_REQUEST") {
            console.log(error.response.data.msg);
          }
        }
      },

      /* Crea cuotas */
      crearCuota: async (descripcion, precio) => {
        try {
          await axios.post(direccion + "/api/cuota", {
            descripcion: descripcion,
            precio: precio,
          });
          getActions().obtenerCuotas();
          return true;
        } catch (error) {
          console.log(error);
        }
      },

      /* Borrar cuotas */
      borrarCuotas: async (id) => {
        try {
          await axios.delete(direccion + "/api/cuota/" + id, {});
          getActions().obtenerCuotas();
          return true;
        } catch (error) {
          console.log(error);
        }
      },

      // Buscador de cuotas
      buscadorCuota: (valor) => {
        let store = getStore();
        let resultados = store.cuotas.filter((item) => {
          if (item.descripcion.toString().toLowerCase().includes(
              valor.toLowerCase())) {
            return valor;
          }
        });
        setStore({
          cuotas: resultados,
        });
      },

      // Obtener cuota por id
      obtenerCuotaId: async (id) => {
        try {
            const response = await axios.get(direccion + "/api/cuota/" + id, {});
            setStore({
                cuota: response.data,
            });
        } catch (error) {
            if (error.code === "ERR_BAD_REQUEST") {
                console.log(error.response.data.msg);
            }
        }
      },

      modificarCuota: async(id, descripcion, precio) => {
        try {
          const response = await axios.put(direccion + "/api/cuota/"+ id, {
            id: id,
            descripcion: descripcion,
            precio: precio
          })
          //console.log(response.data)
          return true
        } catch(error){
          if (error.code === "ERR_BAD_REQUEST") {
            console.log(error.response.data.msg);
          }
        }
      },



      getMessage: async () => {
        try {
          // fetching data from the backend
          const resp = await fetch(process.env.BACKEND_URL + "/api/hello");
          const data = await resp.json();
          setStore({ message: data.message });
          // don't forget to return something, that is how the async resolves
          return data;
        } catch (error) {
          console.log("Error loading message from backend", error);
        }
      },
      changeColor: (index, color) => {
        //get the store
        const store = getStore();

        //we have to loop the entire demo array to look for the respective index
        //and change its color
        const demo = store.demo.map((elm, i) => {
          if (i === index) elm.background = color;
          return elm;
        });

        //reset the global store
        setStore({ demo: demo });
      },
    },
  };
};

export default getState;
