//        Event Listener....    Event..       Event Handler
//                                          (Callback Function)
document.addEventListener("DOMContentLoaded", function () {

    console.log("Hello Universe!!");
    console.dir(document);
    var header1 = document.getElementById("header1");
    console.dir(header1);
    var button = document.getElementById("click-me");
    console.dir(button);
    button.addEventListener("click", function() {
        console.log("Button clicked!!")
        header1.style.color = "red"
    button.addEventListener("mouseover", function(){
        console.log("MousedOver!!")
    } )
    });

})        