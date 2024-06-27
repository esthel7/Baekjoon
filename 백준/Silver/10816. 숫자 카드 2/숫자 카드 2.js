const readline = require('readline');
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let input = [];
rl.on('line', (line) => {
  input.push(line);
}).on('close', () => {
  const N = Number(input.shift());
  const have = input.shift().split(' ');

  let info = {};
  for (let i = 0; i < N; i++) {
    const num = have[i];
    if (info[num] != null) info[num] += 1;
    else info[num] = 1;
  }

  const M = Number(input.shift());
  const q = input.shift().split(' ').map(Number);
  let answer = [];
  for (let i = 0; i < M; i++) {
    const num = String(q[i]);
    if (info[num] == null) answer.push(0);
    else answer.push(info[num]);
  }
  console.log(answer.map((item) => item).join(' '));
  process.exit();
});
