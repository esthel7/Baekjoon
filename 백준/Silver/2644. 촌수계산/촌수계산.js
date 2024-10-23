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
  function find(idx, num) {
    if (parent[idx] !== 0 && !visit[parent[idx]]) {
      if (parent[idx] === b) {
        console.log(num + 1);
        process.exit();
      }
      visit[parent[idx]] = true;
      find(parent[idx], num + 1);
    }
    const childList = Object.keys(child[idx]);
    for (let i = 0; i < childList.length; i++) {
      const mychild = Number(childList[i]);
      if (mychild === b) {
        console.log(num + 1);
        process.exit();
      }
      if (!visit[mychild]) {
        visit[mychild] = true;
        find(mychild, num + 1);
      }
    }
  }

  const n = Number(input[iter++]);
  let command = input[iter++].split(' ');
  const a = Number(command[0]);
  const b = Number(command[1]);

  const parent = [...new Array(n + 1)].map(() => 0);
  const child = [...new Array(n + 1)].map(() => new Object());

  const m = Number(input[iter++]);
  for (let i = 0; i < m; i++) {
    command = input[iter++].split(' ');
    const x = Number(command[0]);
    const y = Number(command[1]);
    parent[y] = x;
    child[x][y] = true;
  }

  const visit = [...new Array(n + 1)].map(() => false);
  visit[a] = true;
  find(a, 0);
  console.log(-1);
  process.exit();
});
