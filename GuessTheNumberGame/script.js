
let numberPlace = document.getElementById('number'); // Ukryta liczba ###
let inputNumber; // Wpis użytkownika
let submit = document.getElementById('submit'); // Guzik submit
let tries = document.getElementById('tries'); // próby - span


let numberInfo = document.getElementById('numberInfo'); // Czy wieksza czy nie

const RandomNumber = Math.floor((Math.random() *100)+1); // random numebr
let proby = 5;

tries.textContent = proby;
console.log(RandomNumber);
submit.onclick = () => {

    inputNumber = Number(document.getElementById('inputNumber').value);

    if (inputNumber < 1 || inputNumber > 100) {
        numberInfo.textContent = 'WPROWADZ POPRAWNA ILOSC : 1-100';
        return; // Zakończ funkcję, aby pozwolić użytkownikowi wpisać poprawną wartość
    }
    
    // console.log('Dziala');
    // console.log(typeof inputNumber, inputNumber);
    
    if(inputNumber < RandomNumber){
        numberInfo.textContent = "Liczba którą wybrałem jest WIĘKSZA";
        proby--;
        tries.textContent = proby;
    }
    else if(inputNumber > RandomNumber){
        numberInfo.textContent = "Liczba którą wybrałem jest MNIEJSZA";
        proby--;
        tries.textContent = proby;
    }
    else if (inputNumber == RandomNumber){
        numberInfo.textContent = "BRAWO! UDAŁO CI SIĘ";
        numberPlace.textContent = RandomNumber;
    }
    
    if (proby == 0) {
        numberInfo.textContent = "PRZEGRAŁEŚ! Liczba to szukana jest powyżej!";
        numberPlace.textContent = RandomNumber;
        submit.disabled = true; // Wyłącz przycisk submit po przegranej
        
    }


}

