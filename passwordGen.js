GeneratePassword = (passwordLength, uppercaseChar, lowercaseChar, symbols, numbers) =>{

    const UpChars = "QWERTYUIOPASDFGHJKLZXCVBNM";
    const LowChars = "qwertyuiopasdfghjklzxcvbnm";
    const NumChars = "1234567890";
    const SymbolsChar = `~!@#$%^&*()_+|}{":?><][';/.,`;
    
    let allowedChars = "";
    let password = ""

    uppercaseChar ? allowedChars+=UpChars : "";
    lowercaseChar ? allowedChars+=LowChars : "";
    symbols ? allowedChars+=SymbolsChar : "";
    numbers ? allowedChars+=NumChars : "";

    if (allowedChars.length === 0){
        console.log('At least 1 set of character must be true')
    }
    if(passwordLength === 0) {
        console.log('Password must be at least 1.')
    }

    
    for (let i = 0; i < passwordLength; i++){
        const RandomIndex = Math.floor(Math.random() * allowedChars.length);
        // console.log(RandomIndex)
        password += allowedChars[RandomIndex];
    }

    
   
    return password;




}




// DO EDYCJI UŻYTKOWNIKA true / false

const passwordLength = 15;
const uppercaseChar = true;
const lowercaseChar = true;
const symbols = true;
const numbers = true;

///

const password = GeneratePassword(passwordLength, uppercaseChar, lowercaseChar, symbols, numbers);

console.log(`Your password has been generated: ${password}`);
