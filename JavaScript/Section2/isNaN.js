//Not a Number
let numero = "18x";
console.log(isNaN(numero))

let edad = parseInt(numero);
console.log(isNaN(edad))
console.log("edad es: " +typeof edad + " = " + edad)

if(edad){
    console.log("edad es de tipo number")
} else {
    console.log("edad es de otro tipo diferente a number")
}

let noEsNumero = isNaN(edad) ? "Es un numero" : "No es un numero";
console.log(noEsNumero); 
/*Esto debido a que 'isNaN' le quita el valor de numero a 'edad'*/ 