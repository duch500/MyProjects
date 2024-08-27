
const display = document.getElementById('display');
let answ;
function appendToDisplay(input){
    display.value += input;
}

function clearDisplay(){
    display.value = "";
}
function calculate(){

    try{

        if(eval(display.value) == Infinity){
            display.value = "Cannot divide by 0";
            
        }
        else{
            display.value = eval(display.value);
        }

        
    }
    catch(error){
        display.value = "Error"
    }
    
}

const switchDay = document.getElementById("switchDay");
let toggleNumber = 0;

switchDay.addEventListener('click', event = ()=>{

switch (toggleNumber){

    case 0:
        document.body.style.background = 'linear-gradient(90deg, rgba(2,0,36,1) 0%, rgba(255,255,255,1) 35%, rgba(233,251,255,1) 46%, rgba(201,246,255,1) 60%, rgba(0,212,255,1) 91%)';
        document.getElementById('container').style.backgroundColor = '#b1eefa';
        toggleNumber++;
        break;

    case 1:
        document.body.style.background = "linear-gradient(109.6deg, rgb(20, 30, 48) 11.2%, rgb(36, 59, 85) 91.1%)";
        document.getElementById('container').style.backgroundColor = 'rgb(54, 54, 54)';
        toggleNumber--;
        break;

}
})