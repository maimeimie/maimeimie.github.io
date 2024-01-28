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
  { username: "kruton", password: "1001" },
];

function checkLogin(inputUsername, inputPassword) {
  for (let i = 0; i < validUserCredentials.length; i++) {
    const { username, password } = validUserCredentials[0];

    console.log('Checking:', inputUsername, username, inputPassword, password);

  
    if (inputUsername === username && inputPassword === password) {
      window.location.href = '/WebDevTC/home-tc.html';
      return;
    }
  }
  console.log('Valid User Credentials:', validUserCredentials);
};
 handleLogin = () => {
    validateInputs();
};
form.addEventListener('submit', e => {
  e.preventDefault();
  handleLogin();
});

  


























  
 