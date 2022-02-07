//var nombre=prompt("dime tu nombre");//

//alert("hola " + nombre);//




/*function bmi(peso,alturta){
   // imc=peso/altura**2
   // if (imc<18.5) {
        //return console.log("bajo de peso")
   // }
    // else if (imc >= 18.5 && imc <= 24.9) {
    //    return console.log("normal")
  //  }
   // else if (imc >=25 && imc <= 29.9) {
        return console.log("Soprepeso")
    }
      else {
    return console.log("obeso")
      }
}

console.log(bmi 65, 1.8))
console.log(bmi 72, 1.6))
console.log(bmi 52, 1.75))
console.log(bmi 135, 1.87)) */



function bmi(peso,alturta){
    imc=peso/altura**2
    if (imc<18.5) {
        return alert("bajo de peso")
    }
     else if (imc >= 18.5 && imc <= 24.9) {
        return alert("normal")
    }
    else if (imc >=25 && imc <= 29.9) {
        return alert("Soprepeso")
    }
      else {
    return alert("obeso")
      }
}

console.log(bmi 65, 1.8))
console.log(bmi 72, 1.6))
console.log(bmi 52, 1.75))
console.log(bmi 135, 1.87))

