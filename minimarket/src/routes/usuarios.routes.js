import {Router} from 'express'
import {crearUsuario,
        login,
        confirmarCuenta} from "../controllers/usuarios.controller.js"

export const usuarioRouter =Router()
usuarioRouter.post("/registro", crearUsuario)
usuarioRouter.post("/login",login)
usuarioRouter.post("/confirmar-cuenta", confirmarCuenta);