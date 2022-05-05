import express, {json} from 'express';
const app= express()
app.use(json())

//nulish coalescingoperator
//si el primer valor no es nulo o undefined entonces sera ese valor
//caso contrario tomara el segundo valor
//https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Nullish_coalescing_operator
const PORT= process.env.PORT ??3000
//SIRV PAara hacer una comprobacion previa
const prueba =process.env.PORT && 10
//-------
//https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Logical_AND
// const numero = 40// 52 es guaraddo en numero
// const prueba_numero = numero<50 && numero+1 // prueba _numero 
 //guarda toda la operacion, en total sera 41
 //------------------
 const persona ={
     nombre:'eduardo',
     apellido:'derivero',
    // actividades:['Nadar','Montar caballo']
 }
 //Esto puede tomar dos valores, el de nadar |undifined
 let actividades=persona.actividades&&persona.actividades[0]
 actividades = false
 actividades=10.2
 actividades= new Date()
 actividades = undefined

 //----------------------operador OR ||
 //en JS el 0 significa False y el 1 y los demas numeros True

// Operador OR ||
// https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Logical_OR
// en JS el 0 significa False y el 1 y los demas numeros significan True
const numero1 = false;
// si la primera condicion es verdadera entonces devuelvo esa sino devolvere la segunda
const resultado = numero1 || 10;
// si el primero resultado no es null o undefined lo devolvere caso contrario devolver el segundo valor
const resultado2 = numero1 ?? 10;
console.log(resultado);
console.log(resultado2);