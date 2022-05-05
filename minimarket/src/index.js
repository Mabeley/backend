import express, {json} from 'express'
import { productosRouter } from './routes/productos.routes.js' 
import {usuarioRouter} from './routes/usuarios.routes.js'
console.log(process.env.EMAIL_ACCOUNT)
const app = express()
app.use(json())
const PORT =process.env.PORT?? 3000
app.get("/",(req, res) => {
    res.json({
        message: "Bienvenido a mi API del minimarket"
    })
})
app.use(productosRouter)
app.use(usuarioRouter)
app.listen(PORT,()=>{
    console.log(`Servidor corriendo exitosamente en el puerto ${PORT}`)
})
