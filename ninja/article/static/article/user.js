console.log("author is s hegade")
document.getElementById('result').src ="/static/article/imag9es (6).png";
const reg=/lorem/gi;

const serach=document.getElementById("search");
const p=document.getElementsByTagName("p");

const bd=document.getElementById("body");
 bd.innerText
 console.log(reg.exec(bd.innerText));
Array.from(p).forEach((element,index)=>{
    serach.addEventListener('keyup',()=>{
        
    if(element.innerHTML.indexOf(serach.value)>-1){
        // console.log(indexOf(serach.value))
        element.style.color="red";
        // p.style.display="none";
        if(serach.value==""){
            element.style.color="";
            element.style.display="block";

        }
    }
    else{
        element.style.display="none";
    }

});
});
function fu() {
    var reader = new FileReader();
    var file = document.getElementById('demo').files[0];

    reader.onload = function(e) {
       document.getElementById('result').src = e.target.result;
    }

    reader.readAsDataURL(file);
 }
