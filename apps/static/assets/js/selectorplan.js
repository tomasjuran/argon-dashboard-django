"use strict";

var SelectorPlan = {
    main: function() {
        const selectorPlan = document.getElementById("selector-plan");
        selectorPlan.addEventListener("change", (event) => {
            const value = event.target.value;
            console.log(value);
        });
    }
}

window.addEventListener('DOMContentLoaded', (event) => {
    //SelectorPlan.main();
});
