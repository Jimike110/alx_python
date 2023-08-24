const number = 100;
prime = true;

for (i = 2; i < number; i++) {
  if (number % i === 0) {
    prime = false;
    break;
  }
}

if (prime) {
  console.log(`${number} is prime`);
} else {
  console.log(`${number} is not prime`);
}
