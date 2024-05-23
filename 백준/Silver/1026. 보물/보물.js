const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let input = [];
rl.on('line', (line) => {
  input.push(line);
}).on('close', () => {
  N = Number(input.shift());
  input = input.map((err) => [...err.split(' ').map(Number)]);
  A = input[0];
  B = input[1];
  A.sort((a, b) => a - b);
  B.sort((a, b) => b - a);
  answer = 0;
  for (let i = 0; i < N; i++) {
    answer += A[i] * B[i];
  }
  console.log(answer);
  process.exit();
});
