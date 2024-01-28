const form = document.getElementById('form');
const username = document.getElementById('username');
const password = document.getElementById('password'); 

const setError = (element, message) => {
  const inputControl = element.parentElement;
  const errorDisplay = inputControl.querySelector('.error');

  errorDisplay.innerText = message;
  inputControl.classList.add('error');
  inputControl.classList.remove('success');
};

const setSuccess = element => {
  const inputControl = element.parentElement;
  const errorDisplay = inputControl.querySelector('.error');

  errorDisplay.innerText = '';
  inputControl.classList.add('success');
  inputControl.classList.remove('error');
};

const validateInputs = () => {
  const usernameValue = username.value.trim();
  const passwordValue = password.value.trim();

  if (usernameValue === '') {
    setError(username, 'Username is required');
  } else if (usernameValue !== validUserCredentials[0].username) {
    setError(username, 'Username is incorrect');
  } else {
    setSuccess(username);
    checkLogin(usernameValue, passwordValue)
  }

  if (passwordValue === '') {
    setError(password, 'Password is required');
  } else if (passwordValue !== validUserCredentials[0].password) {
    setError(password, 'Password is incorrect');
  } else {
    setSuccess(password);
    checkLogin(usernameValue, passwordValue)
  }
};

let validUserCredentials = [
  { username: "22801", password: "2001" },
];

const checkLogin = (inputUsername, inputPassword) => {
  for (let i = 0; i < validUserCredentials.length; i++) {
    const { username, password } = validUserCredentials[i];

    console.log('Checking:', inputUsername, username, inputPassword, password);

    if (inputUsername === username && inputPassword === password) {
      window.location.href = '/WebDevST/home-page.html';
      return;
    }
  }
  console.log('ValidUserCredentials:', validUserCredentials);
};
const handleLogin = () => {
    validateInputs();
};
form.addEventListener('submit', e => {
  e.preventDefault();
  handleLogin();
});