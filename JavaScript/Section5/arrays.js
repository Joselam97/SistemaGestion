let autos = new Array("BMW","Audi","Mercedes","Volkswagen");
let colores = ["rojo","azul","verde","amarillo","morado","blanco"];

console.log(colores[2]);
console.log(autos[1]);

for(let i = 0; i < colores.length; i++){
    console.log(colores[i]);
}

for(let i = 0; i < autos.length; i++){
    console.log(i + ": " + autos[i]);
}

autos[2] = "Mercedes Benz";
autos[autos.length] = "Porsche";
console.log(autos);

console.log(typeof colores);
console.log(Array.isArray(colores));
console.log(autos instanceof Array);