const readline = require('readline');
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let input = [];
rl.on('line', (line) => {
  input.push(line);
}).on('close', () => {
  const [s, p] = input.shift().split(' ').map(Number);
  const l = [...input.shift()];
  const [a, c, g, t] = input.shift().split(' ').map(Number);

  let answer = 0;
  let info = { A: 0, C: 0, G: 0, T: 0 };
  for (let i = 0; i < p; i++) {
    info[l[i]] += 1;
  }
  if (info['A'] >= a && info['C'] >= c && info['G'] >= g && info['T'] >= t)
    answer += 1;

  for (let i = p; i < s; i++) {
    const left = l[i - p];
    info[left] -= 1;
    info[l[i]] += 1;
    if (info['A'] >= a && info['C'] >= c && info['G'] >= g && info['T'] >= t)
      answer += 1;
  }
  console.log(answer);

  process.exit();
});
