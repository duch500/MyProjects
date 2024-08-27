




rollDice = () => {

    let getNum = document.getElementById("inputNumber").value;
    let typeDices = document.getElementById('numberOfDices');
    let spaceForDices = document.getElementById('spaceForDices');
    let values = [];
    let pics = [];

    


    for(let i = 0; i < getNum; i++){

        
            const value = Math.floor(Math.random() * 6) + 1;

            values.push(value);
            pics.push(`<img src="pics/${value}.png" alt="Dice">`);

            typeDices.textContent = "Rolled dices: " + values.join(', ');
            spaceForDices.innerHTML = pics.join(''); 

    
    }


}