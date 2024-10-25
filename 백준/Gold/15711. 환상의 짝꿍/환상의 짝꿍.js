const readline = require('readline');
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let input = [];
let iter = 0;
rl.on('line', (line) => {
  input.push(line);
}).on('close', () => {
  const T = Number(input[iter++]);
  const answers = [];

  const Last = 2000000;
  const possible = [...new Array(Last)].map(() => true);
  const num = [];
  possible[0] = false;
  possible[1] = false;
  for (let i = 2; i < Last; i++) {
    if (possible[i]) {
      num.push(i);
      for (let j = i * 2; j < Last; j += i) {
        possible[j] = false;
      }
    }
  }

  for (let _ = 0; _ < T; _++) {
    const [A, B] = [...input[iter++].split(' ')].map((item) => Number(item));
    const N = A + B - 2;
    if (N <= 1) {
      answers.push('NO');
      continue;
    }
    if (N % 2 === 0) {
      answers.push('YES');
      continue;
    }
    let flag = false;
    for (let i = 0; i < num.length; i++) {
      if (N === num[i] || N < num[i]) {
        answers.push('YES');
        flag = true;
        break;
      }
      if (N % num[i] === 0) {
        answers.push('NO');
        flag = true;
        break;
      }
    }
    if (!flag) answers.push('YES');
  }

  console.log(answers.join('\n'));
  process.exit();
});
