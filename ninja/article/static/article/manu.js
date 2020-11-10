console.log("author");  
const pagemanu=document.getElementById('manu')
const container=document.getElementById('container')
const animate=document.getElementById('animation')
const para=document.getElementsByClassName('pa')
pagemanu.addEventListener('click',()=>{
    container.style.display="block";
    pagemanu.style.display="none";
    
});

console.log(para[0].innerHTML.length)