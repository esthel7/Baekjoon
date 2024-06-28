const readline = require('readline');
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let input = [];
rl.on('line', (line) => {
  input.push(line);
}).on('close', () => {
  function find(now) {
    const idx = now[now.length - 1];
    const nextNode = l[idx];
    if (visited[nextNode]) {
      while (now.length) {
        if (now[0] == nextNode) {
          answer += now.length;
          break;
        }
        now.shift();
      }
    } else if (!visited[nextNode]) {
      visited[nextNode] = true;
      now.push(nextNode);
      find(now);
    }
  }

  const T = Number(input.shift());
  let N = 0;
  let l = [];
  let visited = [];
  let answers = [];
  let answer = 0;
  for (let i = 0; i < T; i++) {
    N = Number(input.shift());
    l = [0].concat(input.shift().split(' ').map(Number));
    for (let i = 0; i <= N; i++) {
      visited.push(false);
    }
    for (let i = 1; i <= N; i++) {
      if (!visited[i]) {
        visited[i] = true;
        find([i]);
      }
    }
    answers.push(N - answer);
    l = [];
    answer = 0;
    visited = [];
  }
  console.log(answers.join('\n'));
  process.exit();
});
