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
  const [N, X] = [...input[iter++].split(' ')].map((item) => Number(item));
  const l = [...input[iter++].split(' ')].map((item) => Number(item));

  if (N == 1) {
    console.log(l[0] + '\n' + 1);
    process.exit();
  }

  let answer = 0;
  for (let i = 0; i < X; i++) {
    answer += l[i];
  }
  let prev = answer;
  let zone = 1;

  for (let i = 1; i < N - X + 1; i++) {
    let now = prev + l[i + X - 1] - l[i - 1];
    if (answer === now) zone += 1;
    else if (answer < now) {
      answer = now;
      zone = 1;
    }
    prev = now;
  }

  if (!answer) console.log('SAD');
  else console.log(answer + '\n' + zone);
  process.exit();
});
