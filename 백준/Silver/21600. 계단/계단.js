const readline = require('readline');
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const input = [];
let iter = 0;
rl.on('line', (line) => {
  input.push(line);
}).on('close', () => {
  const N = Number(input[iter++]);
  const l = [...input[iter++].split(' ')].map((item) => Number(item));
  let last = 1;
  let answer = last;
  for (let i = 0; i < N; i++) {
    if (l[i] >= last) {
      last += 1;
      answer = Math.max(answer, last);
    } else last = l[i];
  }
  answer = Math.max(answer, last);
  console.log(answer);
  process.exit();
});
