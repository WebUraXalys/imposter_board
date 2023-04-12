const inputFac = document.querySelector('#id_faculty'),
   inputGroup = document.querySelector('#id_group'),
   inputEmail = document.querySelector('#id_email'),
   buttonForm = document.querySelector('.button1');

const button = document.querySelector(".button_temp");
const div = document.querySelector(".vidhuk");
const input = document.querySelector(".kom_inp");
const blok = document.querySelector('.block_marks');
const disciplines = document.querySelector('.disciplines');

if (window.location.search.indexOf('qr=true') !== -1) {
  // URL містить параметр qr=true
  console.log('QR code parameter detected!');
  const urlParams = new URLSearchParams(window.location.search);
const word = urlParams.split('/t/')[1].slice(0, -1);
console.log(word)
} else {
  // URL не містить параметр qr=true
  console.log('QR code parameter not found');
}



function fff(){
   blok.classList.remove('none');
}
disciplines.addEventListener('click', fff);

const formChain =[inputFac, inputGroup, inputEmail];
let currentVisibleFormIndex = 0;

function ohh(){
   div.classList.remove('none');
}
div.addEventListener('click', function(e){
   const text = e.currentTarget.textContent.trim();
   input.value = text;
   div.classList.add('none');
});

button.addEventListener('click', ohh);
function displayForm(formEl){
   hideForms();
      formEl.classList.add('add');
      formEl.classList.remove('none');
}

formChain.forEach(form => {
   form.addEventListener('submit', event =>{
      event.preventDefault();
   });
});

function displayNextForm() {
   displayForm(formChain[++currentVisibleFormIndex]);
}

function displayFirstForm(){
   displayForm(formChain[0]);
}

function hideForms(){
   formChain.forEach(form => {
      form.classList.add('none');
      form.classList.remove('add');
});
}


// const emailInput = document.getElementById('email');
// const submitButton = document.getElementById('submit');
let clickCount = 0;

buttonForm.addEventListener('click', () => {
  clickCount++;
   console.log(currentVisibleFormIndex);
  if (currentVisibleFormIndex === 2) {
    const emailValue = inputEmail.value;
    const validDomain = '@lnu.edu.ua';

    if (emailValue.endsWith(validDomain)) {
      // valid email
      // do something here
    } else {
      // invalid email
      alert('Ви ввели неправильну пошту, пройдіть реєстрацію знов викоритовуючи Вашу корпоратвину пошту @lnu.edu.ua');
    }
  }
});

  buttonForm.addEventListener("click", displayNextForm);
  window.addEventListener("DOMContentLoaded", displayFirstForm);