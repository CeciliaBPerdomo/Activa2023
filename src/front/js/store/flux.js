import axios from "axios";
let direccion = process.env.BACKEND_URL;

const getState = ({ getStore, getActions, setStore }) => {
  return {
    store: {
      cuotas: [],
      cuota: {},
      metodos: [],
      metodo: {},
      mutualistas: [],
      mutualista: {},
      alumnos: [],
      alumno: {},
    },
    actions: {
      ////////////////////////////////////
      //          Cuotas              ///
      ////////////////////////////////////
      /* Listar las cuotas*/
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
          if (
            item.descripcion.toString().toLowerCase().includes(
              valor.toLowerCase(),
            )
          ) {
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

      // Modificar cuota
      modificarCuota: async (id, descripcion, precio) => {
        try {
          const response = await axios.put(direccion + "/api/cuota/" + id, {
            id: id,
            descripcion: descripcion,
            precio: precio,
          });
          //console.log(response.data)
          return true;
        } catch (error) {
          if (error.code === "ERR_BAD_REQUEST") {
            console.log(error.response.data.msg);
          }
        }
      },

      ////////////////////////////////////
      //     Metodos de pago           ///
      ////////////////////////////////////
      /* Listar las Metodos*/
      obtenerMetodos: async () => {
        try {
          const response = await axios.get(direccion + "/api/metodos", {});
          setStore({
            metodos: response.data,
          });
        } catch (error) {
          console.log(error);
          if (error.code === "ERR_BAD_REQUEST") {
            console.log(error.response.data.msg);
          }
        }
      },

      /* Crea Metodos */
      crearMetodos: async (tipo, observaciones) => {
        try {
          await axios.post(direccion + "/api/metodos", {
            tipo: tipo,
            observaciones: observaciones,
          });
          getActions().obtenerMetodos();
          return true;
        } catch (error) {
          console.log(error);
        }
      },

      /* Borrar metodos */
      borrarMetodos: async (id) => {
        try {
          await axios.delete(direccion + "/api/metodos/" + id, {});
          getActions().obtenerMetodos();
          return true;
        } catch (error) {
          console.log(error);
        }
      },

      // Obtener metodo por id
      obtenerMetodoId: async (id) => {
        try {
          const response = await axios.get(
            direccion + "/api/metodos/" + id,
            {},
          );
          setStore({
            metodo: response.data,
          });
        } catch (error) {
          if (error.code === "ERR_BAD_REQUEST") {
            console.log(error.response.data.msg);
          }
        }
      },

      // Modificar metodo
      modificarMetodo: async (id, tipo, observaciones) => {
        try {
          await axios.put(direccion + "/api/metodos/" + id, {
            id: id,
            tipo: tipo,
            observaciones: observaciones,
          });
          return true;
        } catch (error) {
          if (error.code === "ERR_BAD_REQUEST") {
            console.log(error.response.data.msg);
          }
        }
      },

      // Buscador de metodos
      buscadorMetodos: (valor) => {
        let store = getStore();
        let resultados = store.metodos.filter((item) => {
          if (
            item.tipo.toString().toLowerCase().includes(
              valor.toLowerCase(),
            )
          ) {
            return valor;
          }
        });
        setStore({
          metodos: resultados,
        });
      },

      ////////////////////////////////////
      //       Mutualista              ///
      ////////////////////////////////////
      /* Listar las Mutualistas */
      obtenerMutualistas: async () => {
        try {
          const response = await axios.get(direccion + "/api/mutualistas", {});
          setStore({
            mutualistas: response.data,
          });
        } catch (error) {
          if (error.code === "ERR_BAD_REQUEST") {
            console.log(error.response.data.msg);
          }
        }
      },

      /* Crea Mutualista */
      crearMutualista: async (nombre, direccionMutualista, telefono) => {
        try {
          await axios.post(direccion + "/api/mutualistas", {
            nombre: nombre,
            direccion: direccionMutualista,
            telefono: telefono,
          });
          getActions().obtenerMutualistas();
          return true;
        } catch (error) {
          console.log(error);
        }
      },

      /* Borrar mutualistas */
      borrarMutualista: async (id) => {
        try {
          await axios.delete(direccion + "/api/mutualistas/" + id, {});
          getActions().obtenerMutualistas();
          return true;
        } catch (error) {
          console.log(error);
        }
      },

      // Obtener mutualista por id
      obtenerMutualistaId: async (id) => {
        try {
          const response = await axios.get(
            direccion + "/api/mutualistas/" + id,
            {},
          );
          setStore({
            mutualista: response.data,
          });
        } catch (error) {
          if (error.code === "ERR_BAD_REQUEST") {
            console.log(error.response.data.msg);
          }
        }
      },

      // Modificar mutualista
      modificarMutualista: async (
        id,
        nombre,
        direccionMutualista,
        telefono,
      ) => {
        try {
          await axios.put(direccion + "/api/mutualistas/" + id, {
            id: id,
            nombre: nombre,
            direccion: direccionMutualista,
            telefono: telefono,
          });
          return true;
        } catch (error) {
          if (error.code === "ERR_BAD_REQUEST") {
            console.log(error.response.data.msg);
          }
        }
      },

      // Buscador de mutualista
      buscadorMutualista: (valor) => {
        let store = getStore();
        let resultados = store.mutualistas.filter((item) => {
          if (
            item.nombre.toString().toLowerCase().includes(
              valor.toLowerCase(),
            )
          ) {
            return valor;
          }
        });
        setStore({
          mutualistas: resultados,
        });
      },

      ////////////////////////////////////
      //       Alumnos                 ///
      ////////////////////////////////////
      /* Listar los Alumnos */
      obtenerAlumnos: async () => {
        try {
          const response = await axios.get(direccion + "/api/alumnos", {});
          setStore({
            alumnos: response.data,
          });
        } catch (error) {
          if (error.code === "ERR_BAD_REQUEST") {
            console.log(error.response.data.msg);
          }
        }
      },

      /* Crea Alumnos */
      crearAlumnos: async (
        cedula,
        nombre,
        apellido,
        direccionAlumno,
        celular,
        fechanacimiento,
        peso,
        altura,
        email,
        idmutualista,
        condicionesmedicas,
        medicacion,
        emergencias,
        motivoentrenamiento,
        idcuota,
        rol,
        activo,
        observaciones,
        fechaingreso,
        foto
      ) => {
        try {
          await axios.post(direccion + "/api/alumnos", {
            cedula: cedula,
            nombre: nombre,
            apellido: apellido,
            direccion: direccionAlumno,
            email: email,
            fechanacimiento: fechanacimiento,
            condicionesmedicas: condicionesmedicas,
            medicacion: medicacion,
            emergencias: emergencias,
            password: cedula,
            rol: rol,
            motivoentrenamiento: motivoentrenamiento,
            observaciones: observaciones,
            foto: foto,
            celular: celular,
            peso: peso,
            altura: altura,
            fechaingreso: fechaingreso,
            activo: activo,
            idcuota: idcuota,
            idmutualista: idmutualista,
          });
          return true;
        } catch (error) {
          console.log(error);
        }
      },

      /* Borrar alumno */
      borrarAlumno: async (id) => {
        try {
          await axios.delete(direccion + "/api/alumnos/" + id, {});
          getActions().obtenerAlumnos();
          return true;
        } catch (error) {
          console.log(error);
        }
      },

      // Buscador de alumno
      buscadorAlumno: (valor) => {
              let store = getStore();
              let resultados = store.alumnos.filter((item) => {
                if (
                  item.nombre.toString().toLowerCase().includes(
                    valor.toLowerCase(),
                  )
                ) {
                  return valor;
                }
              });
              setStore({
                alumnos: resultados,
              });
      },
      
      // Obtener alumno por id
      obtenerAlumnoId: async (id) => {
        try {
          const response = await axios.get(
            direccion + "/api/alumnos/" + id,
            {},
          );
          setStore({
            alumno: response.data,
          });
          console.log(response.data)
        } catch (error) {
          if (error.code === "ERR_BAD_REQUEST") {
            console.log(error.response.data.msg);
          }
        }
      },

      // Modificar Alumno
      modificarAlumno: async (id, 
        cedula,
        nombre,
        apellido,
        direccionAlumno,
        celular,
        fechanacimiento,
        peso,
        altura,
        email,
        idmutualista,
        condicionesmedicas,
        medicacion,
        emergencias,
        motivoentrenamiento,
        idcuota,
        rol,
        activo,
        observaciones,
        fechaingreso,
        foto
      ) => {
        try {
          await axios.put(direccion + "/api/alumnos/" + id, {
            id: id,
            cedula: cedula,
            nombre: nombre,
            apellido: apellido,
            direccion: direccionAlumno,
            email: email,
            fechanacimiento: fechanacimiento,
            condicionesmedicas: condicionesmedicas,
            medicacion: medicacion,
            emergencias: emergencias,
            //password: cedula,
            rol: rol,
            motivoentrenamiento: motivoentrenamiento,
            observaciones: observaciones,
            foto: foto,
            celular: celular,
            peso: peso,
            altura: altura,
            fechaingreso: fechaingreso,
            activo: activo,
            idcuota: idcuota,
            idmutualista: idmutualista,
          });
          return true;
        } catch (error) {
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
