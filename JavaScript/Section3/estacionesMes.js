let mes = new Date().getMonth() + 1;

if (mes >= 1 && mes <= 2 || mes == 12){
    console.log("La estacion del mes es de invierno")
} else if(mes >= 3 && mes <= 5){
    console.log("La estacion del mes pertenece a primavera")
} else if (mes >= 6 && mes <= 8){
    console.log("La estacion del mes pertenece a verano")
} else{
    console.log("La estacion del mes pertenece a oto;o")
}




let horaDelDia = new Date().getHours();

if (horaDelDia >= 0 && horaDelDia <= 6){
    console.log("Es de madrugada")
} else if (horaDelDia >= 7 && horaDelDia <= 12){
    console.log("Es de ma;ana")
} else if (horaDelDia >= 13 && horaDelDia <= 18){
    console.log("Es de tarde")
} else if (horaDelDia >= 19 && horaDelDia <= 23){
    console.log("Es de noche")
}