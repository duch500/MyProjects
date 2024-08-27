
    let numberToConvert;
    let toFahrenheit = document.getElementById("toFahrenheit");
    let toCelsius = document.getElementById("toCelsius");
    let answer = document.getElementById("answer");
    let value;


function Convert(){
    numberToConvert = document.getElementById("numberToConv").value;
    if (toFahrenheit.checked) {

        value = Number(numberToConvert);
        value = (value * 9/5) + 32;
        
        answer.textContent = value.toFixed(2) + "°F";
    } else if (toCelsius.checked) {
        value = Number(numberToConvert);
        value = (value - 32) * 5/9;
        answer.textContent = value.toFixed(2) + "°C";
    } else {
        answer.textContent = "Select unit!";
    }
}
