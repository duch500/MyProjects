let count = 0;
const dcrBut = document.getElementById("decrease");
const incrBut = document.getElementById("increase");
const reset = document.getElementById("reset");
const countNum = document.getElementById("numberCounted");

dcrBut.onclick = function (){
    count--;
    countNum.textContent = count;
}

reset.onclick = () => {
    count = 0;
    countNum.textContent = count;
}

incrBut.onclick = () => {
    count++;
    countNum.textContent = count;
}