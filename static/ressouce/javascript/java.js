const openMenu = document.querySelector(".bx-menu");
const closeMenu =document.querySelector(".bx-x");
const navlink =document.querySelector(".nav-links");
console.log(openMenu)
console.log(closeMenu)
openMenu.addEventListener("click",()=>{
    navlink.style.left="0"
});
closeMenu.addEventListener("click",()=>{
    navlink.style.left="-100%"
})

// ------------------------------------
const onscroll = (el, listener) => {
    el.addEventListener('scroll', listener)
  }
let backtotop = document.querySelector('.back-to-top')
if (backtotop) {
  const toggleBacktotop = () => {
    
    if (window.scrollY > 100) {
      backtotop.classList.add('active')
    } else {
      backtotop.classList.remove('active')
    }
  }
  window.addEventListener('load', toggleBacktotop)
  onscroll(document, toggleBacktotop)
}




