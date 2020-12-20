// var elementClicked = false;
// var isElemClicked = function(elem){
//     elementClicked = true;
//     if(elementClicked == true){
//         elem.className = elem.className.replace(/active/, '');
//     }
// }

// // All navv links
// var nav_links = Array.from(document.getElementsByClassName("nav-link"));
// for(let elem of nav_links){
//     elem.addEventListener('click',isElemClicked)
// }

$(document).ready(function(){
    $(".nav-link").click(function(){
        if(!$(this).attr('class').includes('active')){
            $(this).attr('class')+= "active";
        } else{
            $(this).attr('class') = $(this).attr('class').replace(/active/, '');
        }
    });
});