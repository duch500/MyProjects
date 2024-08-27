function calc(){
    const bill = Number(document.getElementById("bill").value);
    const tip = Number(document.getElementById('tip').value);
    
    const total = document.getElementById('total');

    total.innerHTML = ((bill/100)*tip+bill).toFixed(2);
    console.log(bill)
    console.log(tip)
   

}
const button = document.getElementById('calculate');

button.addEventListener('click', calc);