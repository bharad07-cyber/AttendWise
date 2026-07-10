document.addEventListener("DOMContentLoaded", () => {

    const circle = document.querySelector(".circle");

    if (!circle) return;

    const finalValue = parseFloat(circle.innerText);

    let current = 0;

    circle.innerText = "0%";

    const timer = setInterval(() => {

        current += 1;

        circle.innerText = current + "%";

        if (current >= finalValue) {

            clearInterval(timer);

            circle.innerText = finalValue + "%";

        }

    }, 20);

});


const button = document.querySelector("button");

if(button){

button.addEventListener("mouseenter",()=>{

button.style.transform="scale(1.03)";

});

button.addEventListener("mouseleave",()=>{

button.style.transform="scale(1)";

});

}
