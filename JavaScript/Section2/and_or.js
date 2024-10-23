let and = 5;
let or = -20;

let minimo = 0;
let maximo = 10;


//AND &&
if(and > minimo && and < maximo){
    console.log("a se encuentra entre el rango de 0 a 10")
} else {
    console.log("a no se encuentra dentro del rango de 0 a 10")
}

//OR ||
if(or > minimo || or > maximo){ //no se debe cumplir ninguna para que no se ejecute
    console.log("a se encuentra entre el rango de 0 a 10")
} else { // deben fallar las dos para que se ejecute else
    console.log("a no se encuentra dentro del rango de 0 a 10")
}