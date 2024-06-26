const readline = require('readline');
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let input = [];
rl.on('line', (line) => {
  input.push(line);
}).on('close', () => {
  [N, start] = input.shift().split(' ').map(Number);

  function find(now, cnt) {
    if (cnt >= answer) return;
    if (now.length === N) {
      answer = Math.min(answer, cnt);
      return;
    }
    for (let i = 0; i < N; i++) {
      if (now.includes(i)) continue;
      now.push(i);
      find(now, cnt + visited[now[now.length - 2]][i]);
      now.pop();
    }
  }

  for (let i = 0; i < N; i++) {
    input[i] = input[i].split(' ').map(Number);
  }

  let visited = [];
  for (let i = 0; i < N; i++) {
    visited.push([]);
    visited[i] = input[i];
  }

  for (let i = 0; i < N; i++) {
    for (let j = 0; j < N; j++) {
      if (j == i) continue;
      for (let k = 0; k < N; k++) {
        visited[i][j] = Math.min(visited[i][j], visited[i][k] + visited[k][j]);
      }
    }
  }

  let answer = 20000;
  find([start], 0);
  console.log(answer);
  process.exit();
});
