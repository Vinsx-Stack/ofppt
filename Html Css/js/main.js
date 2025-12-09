let user ;
document.getElementById("Submit").onclick = function(){
    user = document.getElementById("userinput").value;
    document.getElementById("hellomsg").textContent = `Hello ${user} !`
}