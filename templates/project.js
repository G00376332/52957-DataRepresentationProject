// Script file for Blueberry project
// Sources for some part of the script: https://www.w3schools.com/

function indexMain(){
	showSlides();
	showIdxText();
}

// This function will change the background image in the banner on the home page. It will have an animation effect.

var showIndex = 0;

function showSlides() {
  var i;
  var img = ["url(images/sli3.jpg) no-repeat center","url(images/2a.jpg) no-repeat center", "url(images/back-now.jpg) no-repeat center"];
  for (i = 0; i < img.length; i++) {
    document.getElementById("idx-banner").style.background = "none";
  }
  showIndex++;
  if (showIndex > img.length) {showIndex = 1}    
  document.getElementById("idx-banner").style.background = img[showIndex-1]; 
  // Change image every 10 seconds. Match time with banner animation time in css file for smooth effect.
  setTimeout(showSlides, 10000); 
}

// This function will change the text in the banner on the home page. It will have an animation effect.

var textIndex = 0;

function showIdxText() {
  // Create an array with text to loop through.
  var txt = ["Your partner in blueberries","Our Promise", "Your Satisfaction","Our Quality","Your Profit","38 Years of Experience","14 Blueberry Varieties","105 Days of the Season"];
  textIndex++;
  if (textIndex > txt.length) {textIndex = 1}
  document.getElementById("idx-text").innerHTML = txt[textIndex-1];
  // Change the text every 5 seconds. Make the time half of banner animation time in CSS file for the nicer swap effect.
  setTimeout(showIdxText, 5000); 
}

// Login section

// Get the modal
var modal = document.getElementById('login-box');

//When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}

var count = 2;

// This function will handle login box. 

function logout() {
	alert ("You were logged out. Goodbye!");
	window.location ='\logout';
}

// Get the button
var topButton = document.getElementById("topBtn");

// When the user scrolls down 20px from the top of the document, show the button
window.onscroll = function() {scrollFunction()};

function scrollFunction() {
  if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
    topButton.style.display = "block";
  } else {
    topButton.style.display = "none";
  }
}

// When the user clicks on the button, scroll to the top of the document
function topFunction() {
  document.body.scrollTop = 0;
  document.documentElement.scrollTop = 0;