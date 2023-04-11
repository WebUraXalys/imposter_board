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
  buttonForm.addEventListener("click", displayNextForm);
  window.addEventListener("DOMContentLoaded", displayFirstForm);