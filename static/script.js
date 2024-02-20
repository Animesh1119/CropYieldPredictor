alert("js included");
function stat()
{
    sta = document.querySelector("#state").value
    dist = document.querySelector("#district").value
    cro = document.querySelector("#crop").value
    yea = document.querySelector("#year").value
    sea = document.querySelector("#season").value
    are = document.querySelector("#area").value
}


document.querySelector("#sub").addEventListener("click",stat)