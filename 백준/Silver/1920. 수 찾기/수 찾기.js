const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

function find(item) {
  start = 0;
  end = N;
  while (start <= end) {
    now = parseInt((start + end) / 2);
    if (item === lists[now]) return true;
    else if (item < lists[now]) {
      end = now - 1;
    } else {
      start = now + 1;
    }
  }
  return false;
}

let input = [],
  lists,
  N;

rl.on('line', (line) => {
  input.push(line);
}).on('close', () => {
  input.shift();
  lists = [...new Set(input.shift().split(' ').map(Number))];
  N = lists.length;
  lists.sort((a, b) => a - b);

  answer = [];
  M = Number(input.shift());
  check = [...input[0].split(' ').map(Number)];
  for (let i = 0; i < M; i++) {
    if (find(check[i])) answer.push(1);
    else answer.push(0);
  }

  console.log(answer.join('\n'))
  process.exit();
});
