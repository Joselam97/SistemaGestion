//concatenacion de cadenas
var nombre1 =  "Jose";
var nombre2 = "Luis";
var nombreCompleto = nombre1 + " " + nombre2;
console.log(nombreCompleto);

var variables = "Hola" + " " + "Mundo";
console.log(variables);


//Contexto String 
var x = 10;
var y = "Meses";
var z = x +  " " + y;
console.log(z);

var numeroInt = 10;
var numeroStr = "5";
var unidas = numeroInt + numeroStr;
console.log(unidas);

var unidas2 = numeroStr + numeroInt;
console.log(unidas2); 
/*deberia ser 105, pero las toma como string debido a la primer variable que es string y no int */



