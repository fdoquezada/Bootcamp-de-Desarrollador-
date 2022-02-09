// JET: obtener los elementos que tienen clase="column"
var elements = document.getElementsByClassName("column");

// declarar variable para el loop
var i;

// JET: si se selecciona la vista en Lista, definir una funcion listView()
function listView() {
  // JET: para cada elemento i desde 0 hasta el largo de elementos en la variable elements -1
  // JET: "elements - 1" porque la indexación parte en 0 y no en 1,
  for (i = 0; i < elements.length; i++) {
    // asignar el ancho del elemento a un valor porcentual a elección. ej: 80%
    elements[i].style.width = "100%";
  }
}

// Vista de Grid...
function gridView() {
  for (i = 0; i < elements.length; i++) {
    elements[i].style.width = "40%";
  }
}
