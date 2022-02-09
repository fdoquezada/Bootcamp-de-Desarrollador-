const dias = document.getElementById("dias");
const horas = document.getElementById("horas");
const minutos = document.getElementById("minutos");
const segunsdos = document.getElementById("segundos");

const añonuevo = " 1 Jan 2023 00:00:00";

function countTimer() {
  const añonuevoDate = new Date(añonuevo);
  const currentDate = new Date();

  const totalSeconds = (añonuevoDate - currentDate) / 1000;

  const diasCalc = Math.floor(totalSeconds / 3600 / 24);
  const horasCalc = Math.floor(totalSeconds / 3600) % 24;
  const minutosCalc = Math.floor(totalSeconds / 60) % 60;
  const segundossCalc = Math.floor(totalSeconds % 60);
  
  dias.innerHTML = diasCalc;
  horas.innerHTML = horasCalc;
  minutos.innerHTML = minutosCalc;
  segundos.innerHTML = segundossCalc;
}
countTimer();

setInterval(countTimer, 1000);

