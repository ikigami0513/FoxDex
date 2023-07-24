function setCookie(name, value){
    const expirationDate = new Date("9999-12-31T23:59:59");
    const expires = "expires=" + expirationDate.toUTCString();

    // Vérifier si le cookie existe déjà
    const existingCookie = getCookie(name);
    if (existingCookie !== null){
        // Le cookie existe déjà, met à jour sa valeur
        document.cookie = name + "=" + value + ";" + expires + ";path=/";
    }
    else{
        // Le cookie n'existe pas, crée un nouveau cookie avec la valeur spécifiée
        document.cookie = name + "=" + value + ";" + expires + ";path=/";
    }
}

function getCookie(name){
    const cookieName = name + "=";
    const cookies = document.cookie.split(';');
    for (let i = 0; i < cookies.length; i++){
        let cookie = cookies[i];
        while (cookie.charAt(0) === ' '){
            cookie = cookie.substring(1);
        }
        if (cookie.indexOf(cookieName) === 0){
            return cookie.substring(cookieName.length, cookie.length);
        }
    }
    return null;
}