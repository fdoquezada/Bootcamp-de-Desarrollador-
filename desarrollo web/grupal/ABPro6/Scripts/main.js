

/*
document.getElementById("btn-1").onclick = function (){
  alert('¡Gracias por realizar tu pedido! lo confirmaremos a la brevedad');
  }*/


var mailformat = /^([A-Za-z0-9_\-\.])+\@([A-Za-z0-9_\-\.])+\.([A-Za-z]{2,4})$/;

function validacion() {
  if (document.miFormu.nombre.value == "") {
    alert("ingresar nombre");
    return false
    document.miFormu.nombre.focus()

    } else if (document.miFormu.correo.value == "") {
    alert("ingresar correo");
    return false
    document.miFormu.correo.focus()

    }else if (!document.miFormu.correo.value.match(mailformat))
            {alert ("ingrese email valido");
            return false
                document.miFormu.correo.focus()
                


  } else if (document.miFormu.pedido.value == "") {
    alert("ingresar pedido");
    return false
    document.miFormu.pedido.focus()

  } else {


    return true

  }
}

$(document).ready(function() {
    $('#example').DataTable();
} );