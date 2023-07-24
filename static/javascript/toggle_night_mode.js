const toggleNightMode = document.getElementById('night_mode');

toggleNightMode.addEventListener("change", function() {
    if(this.checked){
        setCookie("theme", "dark");
    }
    else {
        setCookie("theme", "light");
    }
    window.location.reload();
});