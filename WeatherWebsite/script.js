
//////////////////// API POGODA

// API KEY    
/// DATA RAIN !! MOZE BYC ALE NIE MUSI
const apiKey = "";
const apiKeyUv = '';

const buttonSearch = document.getElementById("userBtn");

const nameOfDays = ["Ndz", "Pon", "Wt", "Śr", "Czw", "Pt", "Sob"]

// const userCity = 'Zabrze';

// API WEATHERBIT

async function getCordsAndCurrentInfo() {
    const userCity = String(document.getElementById('userInput').value);
    try {
        console.log(`Wybrane miasto: ${userCity}\n`);
        const responseLonLat = await fetch(`https://api.openweathermap.org/data/2.5/weather?q=${userCity}&appid=${apiKey}`);
        const dataLonLat = await responseLonLat.json();

        if (!dataLonLat.coord) {
            throw new Error('Współrzędne miasta nie zostały znalezione');
        }

        const lon = dataLonLat.coord.lon;
        const lat = dataLonLat.coord.lat;

        const response = await fetch(`https://api.openweathermap.org/data/2.5/weather?lat=${lat}&lon=${lon}&units=metric&appid=${apiKey}&lang=pl`); // OPENWEATHER

        const data = await response.json();


        console.log(data);

        if (!data.main || !data.weather || !data.wind) {
            throw new Error('Niekompletne dane pogodowe!');
        }

        const visibility = data.visibility || 'Brak';
        const feelsLike = data.main.feels_like ? Number(data.main.feels_like.toFixed(1)) : 'Brak';
        const humidity = data.main.humidity || 'Brak';
        const pressure = data.main.pressure || 'Brak';
        const temperature = data.main.temp ? Number(data.main.temp.toFixed(1)) : 'Brak';
        const cityName = data.name || 'Brak';
        const skyDesc = data.weather[0].description || 'Brak';
        const skyIcon = data.weather[0].icon || 'Brak';
        const windSpeed = data.wind.speed ? Number(data.wind.speed.toFixed(1)) : 'Brak';
        const windGust = data.wind.gust ? Number(data.wind.gust.toFixed(1)) : 'Brak';



        const uvApiResponse = await fetch(`https://api.weatherbit.io/v2.0/current?lat=${lat}&lon=${lon}&key=${apiKeyUv}`); // UV
        const dataUvApi = await uvApiResponse.json(); // UV DATA
        // console.log('dataUV', dataUvApi);

        console.log(dataUvApi)

        const uvIndex = dataUvApi.data && dataUvApi.data.length > 0 ? dataUvApi.data[0].uv : 'Brak';

        return { lon, lat, uvIndex, feelsLike, humidity, pressure, temperature, cityName, visibility, skyDesc, skyIcon, windSpeed, windGust };
    } catch (error) {
        returnError(error);
    }
}

async function getFiveDayWeather(currentData) {
    try {
        const response = await fetch(`https://api.openweathermap.org/data/2.5/forecast?lat=${currentData.lat}&lon=${currentData.lon}&units=metric&appid=${apiKey}`);
        const data = await response.json();

        console.log('Dane pogodowe pięciodniowe: ', data, `\n`);

        let todaysDay = data.list[0] && data.list[0].dt_txt ? (data.list[0].dt_txt).slice(11, 13) : 'Brak';
        let currentMonth = data.list[0] && data.list[0].dt_txt ? (data.list[0].dt_txt).slice(5, 7) : 'Brak';
        let currentDate = `${todaysDay}.${currentMonth}`;
        todayDate.innerHTML = currentDate;

        for (let i = 1; i < 9; i += 1) {
            const temperature = data.list[i] && data.list[i].main ? Number(data.list[i].main.temp.toFixed(1)) : 'Brak';
            const skyIcon = data.list[i] && data.list[i].weather[0].icon ? data.list[i].weather[0].icon : 'Brak';
            let hour = data.list[i] && data.list[i].dt_txt ? (data.list[i].dt_txt).slice(11, -3) : 'Brak';

            hourlyForecastDivContainer.innerHTML += `<div class="weatherContainer">
                <p style="font-size: 2vh;">${hour}</p>
                <h2 style="font-size: 2.5vh;">${temperature}°C</h2>
                <p id="nowIcon" style="font-size: 0.5vh;"><img  src="icons/${skyIcon}.png" alt="WEATHER ICON"</p>
            </div>`;
        } /// GODZINOWA POGODA

        containerForThatShitTen.innerHTML = "";
        let x;
        let tempX;
        ///// 10 DNIOWA

        let newDate = new Date();
        let currentHour = newDate.getHours();
        console.log(currentHour);

        for (x = 0; x < 30; x += 1) {
            tempX = data.list[x].dt_txt.slice(11, 13);
                tempX = x;
                console.log(tempX)
                break;
            
        }

        if(x % 3 == 1){
            x+=1;
        }
        else if(x % 3 == 2){
            x+=2;
        }
        
        tempX = x;
        for(;x < data.list.length; x+=8){
            
                console.log(data.list[x]);
                let temperatureTen = data.list[x] && data.list[x].main ? Number(data.list[x].main.temp.toFixed(1)) : 'Brak';
                let skyIcon = data.list[x] && data.list[x].weather[0].icon ? data.list[x].weather[0].icon : 'Brak';

                let day = data.list[x] && data.list[x].dt_txt ? (data.list[x].dt_txt).slice(8, 10) : 'Brak';
                let month = data.list[x] && data.list[x].dt_txt ? (data.list[x].dt_txt).slice(5, 7) : 'Brak';
                let dateTenDay = `${day}.${month}`;

                const dayName = new Date((data.list[x].dt_txt).slice(0, 10));
                let dayNum = dayName.getDay();
                

                console.log(`Dane pogodowe 10 dniowe szczególy: Day: ${nameOfDays[dayNum]}, Date: ${dateTenDay}, Temperature: ${temperatureTen}, Icon: ${skyIcon} \n`);
                containerForThatShitTen.innerHTML += `
                    <div class="tenDayForecastContainerInfo">
                        <p style="font-size: 2vh;">${nameOfDays[dayNum]}</p>
                        <p style="color: #aeafb8; font-size: 1.5vh;">${dateTenDay}</p>
                        <h2 style="font-size: 2vh;" class="nowTemp tenDayTemp">${temperatureTen}°C</h2>
                        <p style="font-size: 0.5vh;" class="tenDayIcon"><img src="icons/${skyIcon}.png" alt="WEATHER ICON"></p>
                    </div>`;

        
                
            
        }
    } catch (error) {
        returnError(error);
    }
}

// VARIABLES
const tempSpot = document.getElementById('temperature'); /// Główna temperatura lewaStrona
const weatherDescSpot = document.getElementById('weatherDesc'); // Opis pod spodem - rainy day
const tempText = document.getElementById('tempText'); // Mniejszy opis pod opisem - sam coś zrobić
const tempFeelsLikeTab = document.querySelector('#tabMoreInfo1 > h2'); /// Temperatura odczuwalna tab1
const pressureTabTwo = document.querySelector('#tabMoreInfo2 > h2'); // Ciśnienie
const visibilityTabThree = document.querySelector('#tabDesc3 > h2'); // Widoczność
const humidityTabFour = document.querySelector('#tabDesc4 > h2'); // Wilgoć

const windSpeed = document.querySelector('#windSpeed > h1');
const windGust = document.querySelector('#windGusts > h1');

const nowIcon = document.getElementsByClassName('nowIcon');
const uvDisplay = document.getElementById('uvInfoNumber');

const hourlyForecastDivContainer = document.getElementById('weatherContainerHourly');
const containerForThatShitTen = document.getElementById('containerForThatShitTen');

const todayDate = document.getElementById('todayDate');
const nowTemp = document.getElementsByClassName('nowTemp');

const sliderIndicator = document.getElementById('sliderIndicator');


async function displayWeather(currentData) {

    tempSpot.innerHTML = `${currentData.temperature}°C`;

    for (let i = 0; i < nowTemp.length; i++) {
        if (!nowTemp[i].classList.contains('tenDayTemp')) {
            nowTemp[i].innerHTML = `${currentData.temperature}°C`;
        }
    }

    for (let b = 0; b < nowIcon.length; b++) {
        if (!nowIcon[b].classList.contains('tenDayIcon')) {
            nowIcon[b].innerHTML = `<img src="icons/${currentData.skyIcon}.png" alt="WEATHER ICON">`;
        }
    }

    weatherDescSpot.innerHTML = currentData.skyDesc;
    tempFeelsLikeTab.innerHTML = `${currentData.feelsLike}°C`;
    pressureTabTwo.innerHTML = `${currentData.pressure}hPa`;

    visibilityTabThree.innerHTML = currentData.visibility === 10000 ? `Max - ${currentData.visibility / 1000}km` : `${currentData.visibility / 1000}km`;
    humidityTabFour.innerHTML = `${currentData.humidity}%`;

    windSpeed.innerHTML = currentData.windSpeed;
    windGust.innerHTML = currentData.windGust;
    uvDisplay.innerHTML = currentData.uvIndex;


    

}



async function mainTextInfo(currentWeather){


    
    const temperatureMain = currentWeather.temperature;

    const mainTextInfo = document.getElementById('tempText'); // Główny napis pod wielką temperatura
    let mainText = '';

    const pressureDesc = document.getElementById('pressureInfo');
    let pressureInfo = '';

    const celsiusDesc = document.getElementById('celsiusDesc');
    let feelLikeInfo = '';
    // 
    const visibilityDesc = document.getElementById('visibilityDesc');
    let visibility = '';

    const humidityDesc = document.getElementById('humidityDesc');
    let humidityData = '';
    
    const lvlUv = document.getElementById('lvlUv');
    let uvInfo = '';

const veryColdTexts = [
    "Brrr, bardzo zimno! Wychodząc, nie zapomnij o grubym płaszczu i rękawiczkach!",
    "Lodowate temperatury – idealny czas na gorącą czekoladę i koc!",
    "To prawdziwy mróz! Upewnij się, że Twoje ogrzewanie działa!"
];

const coldTexts = [
    "Zimno na zewnątrz! Czas na ciepły sweter i gorącą kawę.",
    "Chłodno, ale znośnie. Upewnij się, że masz ciepłą odzież.",
    "Przyda się dobra kurtka – dzisiaj nie będzie zbyt ciepło!"
];
const coolTexts = [
    "Chłodno, ale jeszcze znośnie. Może być przyjemnie, jeśli jesteś dobrze ubrany.",
    "Uważaj na chłód! Pogoda jeszcze nie odpuściła.",
    "Dzień będzie chłodny – idealny czas na ciepły napój!"
];
const mildWarmTexts = [
    "Przyjemnie ciepło! Doskonała pogoda na spacer.",
    "Miła temperatura na zewnątrz. Warto wykorzystać dzień na świeżym powietrzu!",
    "Wiosenne ciepło, idealne na wyjście na zewnątrz!"
];
const warmTexts = [
    "Ciepło i przyjemnie! Idealny dzień na piknik lub wycieczkę.",
    "Pamiętaj o kremie przeciwsłonecznym. Nie zapominaj o nawadnianiu się i korzystaj z życia!",
    "Słoneczny dzień – świetny czas na aktywności na świeżym powietrzu!"
];
const veryWarmTexts = [
    "Upalnie na zewnątrz! Pamiętaj o nawadnianiu i unikaj słońca.",
    "Gorący dzień – idealny na plażę lub basen!",
    "Upewnij się, że pijesz dużo wody i unikaj przebywania na słońcu!"
];
const hotTexts = [
    "Ekstremalne upały! Pozostań w chłodnych miejscach i pij dużo wody.",
    "Niebezpiecznie gorąco! Upewnij się, że jesteś dobrze nawodniony i unikaj wysiłku na zewnątrz.",
    "Gorąco jak piekło – najlepszy czas na klimatyzowane pomieszczenia i chłodne napoje!"
];

// Funkcja do uzyskania odpowiedniego tekstu na podstawie temperatury

    if (temperatureMain <= -10) {
        mainText = veryColdTexts[Math.floor(Math.random() * veryColdTexts.length)];
    } else if (temperatureMain <= 0) {
        mainText =  coldTexts[Math.floor(Math.random() * coldTexts.length)];
    } else if (temperatureMain <= 10) {
        mainText = coolTexts[Math.floor(Math.random() * coolTexts.length)];
    } else if (temperatureMain <= 20) {
        mainText = mildWarmTexts[Math.floor(Math.random() * mildWarmTexts.length)];
    } else if (temperatureMain <= 30) {
        mainText = warmTexts[Math.floor(Math.random() * warmTexts.length)];
    } else if (temperatureMain <= 40) {
        mainText = veryWarmTexts[Math.floor(Math.random() * veryWarmTexts.length)];
    } else {
        mainText =  hotTexts[Math.floor(Math.random() * hotTexts.length)];
    }
    
    console.log(mainText);
    mainTextInfo.innerHTML = mainText;



const lowPressureTexts = [
    "Niskie ciśnienie – możliwe opady i burze.",
    "Obniżone ciśnienie oznacza zwiększone ryzyko niepogody.",
    "Spodziewaj się nieprzyjemnej pogody z powodu niskiego ciśnienia."
];

const normalPressureTexts = [
    "Normalne ciśnienie – stabilna pogoda.",
    "Ciągle na poziomie normy, więc pogoda będzie umiarkowana.",
    "Ciśnienie w normie, czeka nas typowa pogoda."
];

const highPressureTexts = [
    "Wysokie ciśnienie – piękna i słoneczna pogoda.",
    "Wysokie ciśnienie sprzyja słonecznym dniom.",
    "Stabilne warunki z powodu wysokiego ciśnienia – świetny dzień na świeżym powietrzu!"
];

    if (currentWeather.pressure < 1000) {
        pressureInfo = lowPressureTexts[Math.floor(Math.random() * lowPressureTexts.length)];
    }
    else if (currentWeather.pressure <= 1020) {
        pressureInfo = normalPressureTexts[Math.floor(Math.random() * normalPressureTexts.length)];
    }
    else {
        pressureInfo = highPressureTexts[Math.floor(Math.random() * highPressureTexts.length)];
    }
    pressureDesc.innerHTML = pressureInfo;




    const coldTextsDesc = [
        "Zimno na zewnątrz – załóż ciepły sweter.",
        "Chłodno, ale znośnie. Przyda się dobra kurtka.",
        "Chłodna pogoda – pamiętaj o ciepłych ubraniach."
    ];
    
    const coolTextsDesc = [
        "Chłodno, ale znośnie. Warto się ubrać warstwowo.",
        "Dzień będzie chłodny – idealny na ciepły napój.",
        "Chłodna pogoda – warto mieć przy sobie coś ciepłego."
    ];
    
    const mildTextsDesc = [
        "Przyjemnie ciepło – świetna pogoda na spacer.",
        "Miła temperatura – doskonała na świeżym powietrzu.",
        "Wiosenne ciepło, idealne na aktywności na zewnątrz."
    ];
    
    const warmTextsDesc = [
        "Ciepło i przyjemnie – idealny dzień na piknik.",
        "Słoneczny dzień – pamiętaj o ochronie przeciwsłonecznej.",
        "Wiosna pełną parą – świetna pogoda na wycieczki."
    ];
    
    const hotTextsDesc = [
        "Upalnie! Pamiętaj o nawodnieniu i unikaj słońca.",
        "Gorący dzień – idealny na basen lub plażę.",
        "Ciepło jak latem – trzymaj się w cieniu i pij dużo wody."
    ];
    
    const veryHotTextsDesc = [
        "Ekstremalne upały – pozostań w chłodnych miejscach.",
        "Niebezpiecznie gorąco – unikaj wysiłku na zewnątrz.",
        "Gorąco jak piekło – najlepszy czas na klimatyzację i chłodne napoje."
    ];
    
    if (currentWeather.feelsLike <= -10) {
        feelLikeInfo = coldTextsDesc[Math.floor(Math.random() * coldTextsDesc.length)];
    } else if (currentWeather.feelsLike <= 0) {
        feelLikeInfo =  coolTextsDesc[Math.floor(Math.random() * coolTextsDesc.length)];
    } else if (currentWeather.feelsLike <= 10) {
        feelLikeInfo =  mildTextsDesc[Math.floor(Math.random() * mildTextsDesc.length)];
    } else if (currentWeather.feelsLike <= 20) {
        feelLikeInfo =  warmTextsDesc[Math.floor(Math.random() * warmTextsDesc.length)];
    } else if (currentWeather.feelsLike <= 30) {
        feelLikeInfo =  hotTextsDesc[Math.floor(Math.random() * hotTextsDesc.length)];
    } else if (currentWeather.feelsLike <= 40) {
        feelLikeInfo =  veryHotTextsDesc[Math.floor(Math.random() * veryHotTextsDesc.length)];
    } else {
        feelLikeInfo =  veryHotTextsDesc[Math.floor(Math.random() * veryHotTextsDesc.length)];
    }

    celsiusDesc.innerHTML = feelLikeInfo;

const excellentVisibilityTexts = [
    "Wspaniała widoczność! Ciesz się pięknym dniem.",
    "Idealna widoczność – doskonała pogoda na wycieczki.",
    "Wspaniałe warunki do podziwiania widoków."
];

const goodVisibilityTexts = [
    "Dobra widoczność – dzień idealny na spacery.",
    "Widoczność jest w porządku – korzystaj z ładnej pogody.",
    "Dzień jest przejrzysty – świetny czas na aktywności na świeżym powietrzu."
];

const moderateVisibilityTexts = [
    "Widoczność średnia – może być trochę mgliście.",
    "Dzień jest nieco zamglony, ale wciąż przyjemny.",
    "Widoczność umiarkowana – ubierz się odpowiednio."
];

const poorVisibilityTexts = [
    "Widoczność ograniczona – warto być ostrożnym na drodze.",
    "Zamglona pogoda – trudniej dostrzegać odległe obiekty.",
    "Widoczność kiepska – sprawdź prognozę, zanim wyjdziesz."
];

const veryPoorVisibilityTexts = [
    "Widoczność bardzo ograniczona – unikaj podróży.",
    "Mgła lub deszcz – widoczność mocno ograniczona.",
    "Trudna widoczność – najlepiej zostań w domu lub zachowaj szczególną ostrożność."
];

const extremeVisibilityTexts = [
    "Widoczność ekstremalnie ograniczona – bardzo trudne warunki.",
    "Bardzo słaba widoczność – unikaj podróży, jeśli to możliwe.",
    "Skrajnie ograniczona widoczność – zachowaj dużą ostrożność."
];

if ((currentWeather.visibility / 1000) >= 10) {
    visibility = excellentVisibilityTexts[Math.floor(Math.random() * excellentVisibilityTexts.length)];
} else if ((currentWeather.visibility / 1000) >= 7) {
    visibility = goodVisibilityTexts[Math.floor(Math.random() * goodVisibilityTexts.length)];
} else if ((currentWeather.visibility / 1000) >= 4) {
    visibility = moderateVisibilityTexts[Math.floor(Math.random() * moderateVisibilityTexts.length)];
} else if ((currentWeather.visibility / 1000) >= 2) {
    visibility = poorVisibilityTexts[Math.floor(Math.random() * poorVisibilityTexts.length)];
} else if ((currentWeather.visibility / 1000) >= 1) {
    visibility = veryPoorVisibilityTexts[Math.floor(Math.random() * veryPoorVisibilityTexts.length)];
} else {
    visibility = extremeVisibilityTexts[Math.floor(Math.random() * extremeVisibilityTexts.length)];
}

visibilityDesc.innerHTML = visibility;



const veryLowHumidityTexts = [
    "Wilgotność jest bardzo niska – idealne warunki do spędzenia czasu na zewnątrz.",
    "Powietrze jest suche – dobrze dla skóry i oddychania.",
    "Niska wilgotność – świetny dzień na aktywności na świeżym powietrzu."
];

const lowHumidityTexts = [
    "Wilgotność jest niska – przyjemna pogoda na spacery.",
    "Powietrze jest dość suche – dobrze się oddycha.",
    "Niska wilgotność – idealna pogoda na aktywności na świeżym powietrzu."
];

const moderateHumidityTexts = [
    "Wilgotność umiarkowana – komfortowa pogoda na zewnątrz.",
    "Średnia wilgotność – przyjemna pogoda, ale warto pić dużo wody.",
    "Wilgotność w normie – korzystaj z dnia, ale pamiętaj o nawodnieniu."
];

const highHumidityTexts = [
    "Wilgotność jest wysoka – może być duszno na zewnątrz.",
    "Wysoka wilgotność – warto mieć ze sobą wodę i ubrać się lekko.",
    "Duszne powietrze – postaraj się unikać długiego przebywania na zewnątrz."
];

const veryHighHumidityTexts = [
    "Wilgotność bardzo wysoka – ciężkie, duszne powietrze.",
    "Ekstremalna wilgotność – unikaj wysiłku na zewnątrz i często pij wodę.",
    "Bardzo wysoka wilgotność – poczujesz się lepki, staraj się unikać słońca."
];


if (currentWeather.humidity <= 20) {
    humidityData =  veryLowHumidityTexts[Math.floor(Math.random() * veryLowHumidityTexts.length)];
} else if (currentWeather.humidity <= 40) {
    humidityData =  lowHumidityTexts[Math.floor(Math.random() * lowHumidityTexts.length)];
} else if (currentWeather.humidity <= 60) {
    humidityData =  moderateHumidityTexts[Math.floor(Math.random() * moderateHumidityTexts.length)];
} else if (currentWeather.humidity <= 80) {
    humidityData =  highHumidityTexts[Math.floor(Math.random() * highHumidityTexts.length)];
} else {
    humidityData =  veryHighHumidityTexts[Math.floor(Math.random() * veryHighHumidityTexts.length)];
}

humidityDesc.innerHTML = humidityData;


// Lista krótkich tekstów w zależności od indeksu UV
const veryLowUvTexts = [
    "Bardzo niski UV – możesz spędzać czas na zewnątrz bez obaw.",
    "Niski UV – idealne warunki na spacer.",
    "Bardzo niski UV – brak potrzeby ochrony."
];

const lowUvTexts = [
    "Niski UV – użyj ochrony słonecznej przy dłuższym pobycie na słońcu.",
    "Niski UV – krótki pobyt na słońcu jest bezpieczny.",
    "Niski UV – warto użyć kremu przeciwsłonecznego."
];

const moderateUvTexts = [
    "Umiarkowany UV – stosuj ochronę przeciwsłoneczną przy dłuższym pobycie.",
    "Umiarkowany UV – używaj filtra w godzinach szczytu.",
    "Umiarkowany UV – unikaj słońca w godzinach największego nasilenia."
];

const highUvTexts = [
    "Wysoki UV – konieczna jest wysoka ochrona przeciwsłoneczna.",
    "Wysoki UV – unikaj słońca w godzinach szczytu.",
    "Wysoki UV – pamiętaj o kremie przeciwsłonecznym i okularach."
];

const veryHighUvTexts = [
    "Bardzo wysoki UV – używaj pełnej ochrony przeciwsłonecznej.",
    "Bardzo wysoki UV – unikaj słońca, stosuj krem i okulary.",
    "Bardzo wysoki UV – dbaj o pełną ochronę przeciwsłoneczną."
];

const extremeUvTexts = [
    "Ekstremalny UV – pozostań w cieniu i stosuj pełną ochronę.",
    "Ekstremalny UV – wyjście na słońce jest niebezpieczne.",
    "Ekstremalny UV – używaj bardzo wysokiego filtra i unikaj słońca."
];

// Funkcja do uzyskania odpowiedniego tekstu na podstawie indeksu UV
    
    const sliderIndicator = document.getElementById('sliderIndicator');

    if (currentWeather.uvIndex <= 1) {
        uvInfo = veryLowUvTexts[Math.floor(Math.random() * veryLowUvTexts.length)];
        sliderIndicator.style.left = '2%'
    }
    else if (currentWeather.uvIndex <= 2) {
        uvInfo = veryLowUvTexts[Math.floor(Math.random() * veryLowUvTexts.length)];
        sliderIndicator.style.left = '15%'
    }
    else if (currentWeather.uvIndex <= 4) {
        uvInfo = lowUvTexts[Math.floor(Math.random() * lowUvTexts.length)];
        sliderIndicator.style.left = '35%'
    }
    else if (currentWeather.uvIndex <= 6) {
        uvInfo = moderateUvTexts[Math.floor(Math.random() * moderateUvTexts.length)];
        sliderIndicator.style.left = '50%'
    }
    else if (currentWeather.uvIndex <= 8) {
        uvInfo = highUvTexts[Math.floor(Math.random() * highUvTexts.length)];
        sliderIndicator.style.left = '65%'
    }
    else if (currentWeather.uvIndex <= 10) {
        uvInfo = veryHighUvTexts[Math.floor(Math.random() * veryHighUvTexts.length)];
        sliderIndicator.style.left = '75%'
    }
    else if (currentWeather.uvIndex > 10) {
        uvInfo = extremeUvTexts[Math.floor(Math.random() * extremeUvTexts.length)];
        sliderIndicator.style.left = '95%'
    }
    else{
        uvInfo.innerHTML = "Brak informacji o stopniu UV :("
    }

    lvlUv.innerHTML = uvInfo;


}





async function getWeather() {

    const currentData = await getCordsAndCurrentInfo();
    if (currentData) {
        // console.log(currentDat?a);
        await getFiveDayWeather(currentData);
        await mainTextInfo(currentData);
        // await weatherAdditionalInfo(currentWeather);
        await displayWeather(currentData);
        
    }
}






function returnError(error) {
    console.error(error);
    alert('Pojawił się błąd. Proszę spróbuj ponownie.');
}

buttonSearch.addEventListener('click', getWeather);

































function border(){

  let elements = document.querySelectorAll("*");

  elements.forEach(element =>{
      element.classList.toggle('changed-style')
  });
}



// SWITCH LIGHT MODE
const toggleMode = () => {
  const themeStyle = document.getElementById('theme-style');
  if (themeStyle.getAttribute('href') === 'lightMode.css') {
    themeStyle.setAttribute('href', 'darkMode.css');
  } else {
    themeStyle.setAttribute('href', 'lightMode.css');
  }
};

document.addEventListener('DOMContentLoaded', (event) => {
  const button = document.getElementById('toggleButton');
  button.addEventListener('click', toggleMode);
});


  


let check = false;
const toggleIcon = () => {
  const elements = document.querySelectorAll('img');
  elements.forEach(element => {
  let src = element.src;
//   console.log('Original src:', src);
  
  // Pobierz nazwę pliku z src
  let fileName = src.substring(src.lastIndexOf('/') + 1);
//   console.log('File name:', fileName);

  // Znajdź ostatnią kropkę
  let dotIndex = fileName.lastIndexOf('.');
  if (dotIndex !== -1) {
      let newFileName;
      if (check) {
      // Usuń 'L' przed ostatnią kropką
      newFileName = fileName.slice(0, dotIndex).replace(/L$/, '') + fileName.slice(dotIndex);
      } else {
      // Dodaj 'L' przed ostatnią kropką
      newFileName = fileName.slice(0, dotIndex) + 'L' + fileName.slice(dotIndex);
      }
    //   console.log('New file name:', newFileName);
      
      // Zaktualizuj src elementu
      let newSrc = src.substring(0, src.lastIndexOf('/') + 1) + newFileName;
    //   console.log('New src:', newSrc);
      element.src = newSrc;
  }
  });
  // Przełącz wartość zmiennej check
  check = !check;
};

document.addEventListener('DOMContentLoaded', (event) => {
  const button = document.getElementById('toggleButton');
  button.addEventListener('click', toggleIcon);
});


// script.js


window.onload = function loading() {
    console.log('Page loaded');
    

    setTimeout(() =>{
        const preloader = document.getElementById('preloader');
    preloader.style.opacity = '0';
    preloader.style.transition = 'opacity 0.5s ease';
    setTimeout(() => {
        preloader.style.display = 'none';
        document.getElementById('main').style.display = 'flex';
    }, 500);
    }, 1000)
    
}