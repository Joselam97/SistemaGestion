inicio:
for(let contador = 0; contador <= 10; contador++){
    if (contador % 2 == 1) {
        console.log(contador)
        continue inicio;
    }
    console.log(contador)
}