//Dato string
var nombre = "Jose";
console.log(nombre);



//integer
var numero = 1000;
console.log(numero);



//object
/*Vendria siendo similar a un diccionario en python */ 
var objeto = {
    nombre: "Jose",
    apellido: "Alvarez",
    edad: 27
}
console.log(objeto);



//variables sin definir
cadena = "Hola mundo";
console.log(typeof cadena); /*Imprime el tipo de variable debido a 'typeof'*/
console.log(cadena); /*Imprime el contenido de la variable*/ 



//boolean
var boleano = true;
console.log("Es mi nombre Jose? " + boleano);
console.log(typeof boleano);



//function
function miFuncion() {
    console.log("Ejecutando Funcion");
}

miFuncion();



//Symbol
var simbolo = Symbol("variable tipo simbolo");
console.log(simbolo);
console.log(typeof simbolo);



//class
class Persona {
    constructor(nombre, apellido, edad) {
        this.nombre = nombre;
        this.apellido = apellido;
        this.edad = edad;
    }
}

var clasePersona = new Persona("Jose", "Alvarez", 27);
console.log(clasePersona);
console.log(typeof clasePersona);



//undefined
var indefinida;
console.log(indefinida);
console.log(typeof indefinida);



//null
var nulo = null;
console.log(nulo);
console.log(typeof nulo);



//array
var lista = [1,2,3,4,5];
console.log(lista);

var arreglo = [];
arreglo.push("toyota");
arreglo.push("honda");
arreglo.push("nissan");
console.log(arreglo);


