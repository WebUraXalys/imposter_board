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

function sendmark() {
   let y = document.getElementById("y").value;
   let m = document.getElementById("m").value;
   let o = document.getElementById("o").value;
   let gtsid = document.getElementById("dsid").value;
   let rq = document.getElementById("rq").value;
   let csrf = document.getElementById("csrf").value;
   let body = "y=" + y + "&m=" + m + "&o=" + o + "&gtsid=" + gtsid + "&csrfmiddlewaretoken=" + csrf
   fetch(
      rq, {
         method: "POST",
         body: body,
         //headers: {"Content-Type": "application/x-www-form-urlencoded"}
      }).then((resp) => {
         console.log(resp);
      });
}

  buttonForm.addEventListener("click", displayNextForm);
  window.addEventListener("DOMContentLoaded", displayFirstForm);