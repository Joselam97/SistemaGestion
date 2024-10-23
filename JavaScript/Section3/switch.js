let numero = 3;
let desconocido = "Valor desconocido";

switch(numero){
    case 1:
        desconocido = "Uno";
        break;
    case 2:
        desconocido = "Tres";
        break;
    case 3:
        desconocido = "Tres";
        break;
    default:
        desconocido
        break;
}

console.log(desconocido);




let estacion = new Date().getMonth() + 1;
let estacionActual = "Desconocida";

switch(estacion){
    case 1: case 2: case 12:
        estacionActual = "Invierno";
        break;
    case 3: case 4: case 5:
        estacionActual = "Primavera";
        break;
    case 6: case 7: case 8:
        estacionActual = "Oto;o";
        break;
    case 9: case 10: case 11:
        estacionActual = "Verano";
        break;
    default:
        estacionActual
        break;
}

console.log(estacionActual);
