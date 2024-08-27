document.addEventListener('DOMContentLoaded', async () => {
    await displayRandomCulinaryData(); // Wywołanie funkcji po załadowaniu DOM
});

const sliderInput = document.getElementById('myRangeTime');
const output = document.getElementById('sliderOutput');
if (sliderInput && output) {
    sliderInput.oninput = function (event) {
        output.innerHTML = event.target.value;
    };
}

const apiKey = '';

async function getSelectedCheckboxes(){

    try{
        let dietType = [];
        let intolerancyType = [];
        let dishType = [];
        let cuisineType = [];

            let checkboxes = document.querySelectorAll('input[type="checkbox"]');
            
                for (let checkboxIterator = 0; checkboxIterator < checkboxes.length; checkboxIterator++){

                    if(checkboxes[checkboxIterator].checked){
                        
                        switch(checkboxes[checkboxIterator].name){

                            case 'dietType':
                            
                            dietType.push(checkboxes[checkboxIterator].id);
                            break;

                            case 'intolerancyType':
                            intolerancyType.push(checkboxes[checkboxIterator].id);
                            break;

                            case 'dishType':

                            dishType.push(checkboxes[checkboxIterator].id);
                            break;
                            case 'cuisineType':

                            cuisineType.push(checkboxes[checkboxIterator].id);
                            break;
                        }

                      
                    

                    }
                    
            

                }


        const radioInputs = document.querySelectorAll('input[type="radio"]');
        let radioAnsw = "";
        for (let radioIterator = 0; radioIterator < radioInputs.length; radioIterator++) {
            if (radioInputs[radioIterator].checked) {
                radioAnsw = radioInputs[radioIterator].value;
                break;
            }
        }
        



        const sliderValue = document.getElementById('sliderOutput').value;
            
        

        console.log(dietType)
        console.log(intolerancyType)
        console.log(dishType)
        console.log(cuisineType)

        let createNewLink = `https://api.spoonacular.com/recipes/complexSearch?`
        


    }
    catch(error){
        returnError(error)
        throw new Error('Something went wrong :(')
    }



}





async function getRandomCulinaryData() {
    try {
        const response = await fetch(`https://api.spoonacular.com/recipes/random?number=10&apiKey=${apiKey}`);
        // const response = await fetch(`https://api.spoonacular.com/recipes/complexSearch?query=pasta&maxFat=25&number=2&apiKey=${apiKey}`); NIE DZIAŁA - INNA PĘTLA MUSI BYĆ
        if (!response.ok) {
            throw new Error(`Błąd sieci: ${response.status}`);
        }

        const data = await response.json();
        console.log(data)
        let results = [];

        for (let i = 0; i < data.recipes.length; i++) {
            const recipeData = {
                isCheap: data.recipes[i].cheap, // used
                cuisine: data.recipes[i].cuisines[0] || 'No idea', // used
                isDairyFree: data.recipes[i].dairyFree, // used
                diet: data.recipes[i].diets[0] || 'No idea', // used
                stepsToDoRecipe: data.recipes[i].analyzedInstructions[0], ///////////////////////
                dishType: data.recipes[i].dishTypes[0] || 'No idea', // used
                extendedIngredients: data.recipes[i].extendedIngredients, /////////////////////// 
                isGlutenFree: data.recipes[i].glutenFree, // used
                imageUrl: data.recipes[i].image || 'No idea', // used
                shortInstruction: data.recipes[i].instructions || 'No idea', // used
                bestOccasionsToServe: data.recipes[i].occasions || 'No idea', // used
                readyWhen: data.recipes[i].readyInMinutes || 'No idea', ///////////////////////
                dishTitle: data.recipes[i].title || 'No idea', // used
                isVegan: data.recipes[i].vegan, // used
                isVegetarian: data.recipes[i].vegetarian, // used
                isVeryHealthy: data.recipes[i].veryHealthy, // used
                isPopular: data.recipes[i].veryPopular, // used
                servings: data.recipes[i].servings || 'No idea', // used
                summary: data.recipes[i].summary || 'No idea' // used
            };
            results.push(recipeData);
        }
        return results;
    } catch (error) {
        returnError(error);
    }
}

async function displayRandomRecipes(culinaryData) {
    try {
        const section = document.getElementById('section');
        section.innerHTML = '';

        for (let o = 0; o < culinaryData.length; o++) {
            let instructionList = await createList(culinaryData[o]);

            let ingredientsList = await createIngrList(culinaryData[o]);

            const recipeContainer = document.createElement('div');
            recipeContainer.className = 'RecipeContainer';

            recipeContainer.innerHTML = `
            <div class="visiblePart">
                    <button class="toggle-button">&#9660;</button>
            <div class="titleAndImage">
                    <p style="font-size: 1.4rem; font-weight: bold;">${culinaryData[o].dishTitle}</p>
                    <img alt="${culinaryData[o].dishTitle} -- IMAGE MISSING -- SOMETHING WENT WRONG" style="width: 370px; height: auto; object-fit: cover;" draggable="false" src=${culinaryData[o].imageUrl}>
                </div>

                <div class="BooleanInfoMainContainer">
                ${await createBooleanInfo('Gluten free', culinaryData[o].isGlutenFree)}
                ${await createBooleanInfo('Vegan', culinaryData[o].isVegan)}
                ${await createBooleanInfo('Vegetarian', culinaryData[o].isVegetarian)}
                ${await createBooleanInfo('Healthy', culinaryData[o].isVeryHealthy)}
                ${await createBooleanInfo('Dairy free', culinaryData[o].isDairyFree)}
                ${await createBooleanInfo('Popular', culinaryData[o].isPopular)}
                ${await createBooleanInfo('Cheap', culinaryData[o].isCheap)}
                </div>

                <div class="dishRec">
                    <p>${culinaryData[o].summary}</p>
                </div>

                <div class="BooleanInfoMainContainer">
                    <div class="booleanInfoSmallContainer">
                        <p>Servings: <span style="font-weight: bold;"> ${culinaryData[o].servings}</span></p> 
                    </div>
                    <div class="booleanInfoSmallContainer">
                        <p>Type of cuisine: <span style="font-weight: bold;">${culinaryData[o].cuisine}</span></p> 
                    </div>
                    <div class="booleanInfoSmallContainer">
                        <p>Type of diet: <span style="font-weight: bold;">${culinaryData[o].diet}</span> </p>
                    </div>
                    <div class="booleanInfoSmallContainer">
                        <p>Type of dish: <span style="font-weight: bold;">${culinaryData[o].dishType}</span></p> 
                    </div>
                    <div class="booleanInfoSmallContainer">
                        <p>Best occasion to serve: <span style="font-weight: bold;">${culinaryData[o].bestOccasionsToServe}</span> </p> 
                    </div>
                </div>
            </div>
                <div class="notVisible">
                    <div class="additional-content">
                        <div class="dishRec instruction">
                        <h2>Instruction:</h2>
                            <p>${instructionList}</p>
                        </div>

                        <div class="neededStuff instruction">
                            <h2>Ingredients:</h2>
                            <p>${ingredientsList}</p>
                        </div>
                    </div>
                </div>
            `;

            section.appendChild(recipeContainer);
        }

        workingButtons(); // Musi być wywołana po wygenerowaniu zawartości

        const images = document.querySelectorAll('img');
    } catch (error) {
        returnError(error);
    }
}

async function createIngrList(recipe){

    try{

        let ingredientsList = [];

        let instruction = recipe.extendedIngredients;

        for(let i = 0; i < instruction.length; i++){

            ingredientsList.push(`<li>${instruction[i].original}</li>`);


        }
        ingredientsList = `<ol>${ingredientsList.join('')}</ol>`
        return ingredientsList;


    }
    catch(error){
        returnError(error);
        throw new Error("Lista składników uszkodzona")
    }

}


async function createList(recipe) {
    try {
        let instructionCreated = [];

        let instruction = recipe.shortInstruction;

        if (instruction[0] == "<") {
            instructionCreated = instruction;
        } else {
            let zdania = instruction.split('.').map(zdanie => zdanie.trim()).filter(zdanie => zdanie.length > 0);

            zdania.forEach(zdanie => {
                instructionCreated.push(`<li>${zdanie}.</li>`);
            });
            instructionCreated = `<ol>${instructionCreated.join('')}</ol>`;
        }

        return instructionCreated;
    } catch (error) {
        console.error('Błąd:', error);
        returnError(error);
    }
}

async function createBooleanInfo(name, value) {
    let iconSrc = 'Icons/culinary.png';
    if (value == true) {
        iconSrc = 'Icons/S.png';
    } else if (value == false) {
        iconSrc = 'Icons/X.png';
    }

    return `
    <div class="booleanInfoSmallContainer">
        <p>${name}: </p> <img src="${iconSrc}" alt="${name}" style="height: 30px;">
    </div>`;
}

function workingButtons() {

    const toggleButtons = document.getElementsByClassName('toggle-button');
    const additionalContents = document.getElementsByClassName('additional-content');


    Array.from(toggleButtons).forEach(function (element, index) {
        element.addEventListener('click', () => {
            const content = additionalContents[index];
            const isExpanded = content.classList.contains('expanded');

            if (isExpanded) {
                content.classList.remove('expanded'); 
                element.innerHTML = '&#9660;'; // Strzałka w dół
            } else {
                content.classList.add('expanded');
                element.innerHTML = '&#9650;'; // Strzałka w górę
            }
        });
    });
}

async function displayRandomCulinaryData() {
    const culinaryData = await getRandomCulinaryData();
    await displayRandomRecipes(culinaryData);
    // await getSelectedCheckboxes();
    console.log(`Dane kulinarne:`, culinaryData);
}

async function returnError(error) {
    console.error(error);
    throw new Error(error);
}

let isVisible = true;

function tick() {
    const aside = document.getElementById('aside');
    const section = document.getElementById('section');
    const button = document.getElementById('beruh');

    if (isVisible) {
        aside.style.left = '-12%';
        button.innerHTML = '>';
        button.style.left = '0.3%';

        section.style.left = '-50%';
        section.style.transform = 'translateX(50%)';
        section.style.width = '100%';
        isVisible = !isVisible;
    } else {
        aside.style.left = '0px';
        button.innerHTML = '<';
        button.style.left = '13.5%';
        section.style.left = '0px';
        section.style.transform = 'translateX(0)';
        section.style.width = '78%';
        isVisible = !isVisible;
    }
}
