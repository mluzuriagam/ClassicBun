/*!
* Start Bootstrap - Agency v7.0.11 (https://startbootstrap.com/theme/agency)
* Copyright 2013-2022 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-agency/blob/master/LICENSE)
*/
//
// Scripts
// 

window.addEventListener('DOMContentLoaded', event => {

    // Navbar shrink function
    var navbarShrink = function () {
        const navbarCollapsible = document.body.querySelector('#mainNav');
        if (!navbarCollapsible) {
            return;
        }
        if (window.scrollY === 0) {
            navbarCollapsible.classList.remove('navbar-shrink')
        } else {
            navbarCollapsible.classList.add('navbar-shrink')
        }

    };

    // Shrink the navbar 
    navbarShrink();

    // Shrink the navbar when page is scrolled
    document.addEventListener('scroll', navbarShrink);

    // Activate Bootstrap scrollspy on the main nav element
    const mainNav = document.body.querySelector('#mainNav');
    if (mainNav) {
        new bootstrap.ScrollSpy(document.body, {
            target: '#mainNav',
            offset: 74,
        });
    };

    // Collapse responsive navbar when toggler is visible
    const navbarToggler = document.body.querySelector('.navbar-toggler');
    const responsiveNavItems = [].slice.call(
        document.querySelectorAll('#navbarResponsive .nav-link')
    );
    responsiveNavItems.map(function (responsiveNavItem) {
        responsiveNavItem.addEventListener('click', () => {
            if (window.getComputedStyle(navbarToggler).display !== 'none') {
                navbarToggler.click();
                responsiveNavColor();
            }
        });
    });

    //Gives color on click for small devices collapsable menu
    var on=0
    const navbarCollapsible = document.body.querySelector('#mainNav');
    function responsiveNavColor(){
        if(on===0){
        navbarCollapsible.classList.add('navbar-color');
        on=1;
        }
        else{
        navbarCollapsible.classList.remove('navbar-color')
        on=0;
        }
    };
    navbarToggler.addEventListener('click', responsiveNavColor);

    function checkFloatingDiv() {
  var section1 = document.querySelector("#footer-info");
  var position1 = section1.getBoundingClientRect();

  //Checking whether the specified sections are visible
  //If any of them is visible, then show the float content. Else, hide it.
  if (position1.top < window.innerHeight && position1.bottom >= 0) {
    //Show the floating element
    document.querySelector('#float-popup').style.display = "none";
    return;
  } else {
    document.querySelector('#float-popup').style.display = "inline";
  }
  }
    // Run the function on scroll
    document.addEventListener("scroll", checkFloatingDiv);
    // Run the function on load, if any elements are already visible without scrolling
    document.addEventListener("load", checkFloatingDiv);
});

