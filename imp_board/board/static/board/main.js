const inputFac = document.querySelector('#id_faculty'),
   inputGroup = document.querySelector('#id_group'),
   inputEmail = document.querySelector('#id_email'),
   buttonForm = document.querySelector('.button1');
const formChain =[inputFac, inputGroup, inputEmail];
let currentVisibleFormIndex = 0;


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