import {Router} from "express"
import { 
    crearProducto,
    listarProductos, 
    actualizarProducto,
    eliminarProducto } 
    from "../controllers/producto.controller.js"

export const productosRouter =Router()
productosRouter.route("/productos").post(crearProducto).get(listarProductos)
productosRouter.route("/productos/:id").put(actualizarProducto).delete(eliminarProducto)
// productosRouter.post('/productos', crearProducto)
// productosRouter.get('/productos',listarProductos)