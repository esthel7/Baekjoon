const readline = require('readline');
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

function heappush(q, item) {
  if (!q.length) {
    q.push(0);
    q.push(item);
    return;
  }
  let idx = q.length;
  q.push(item);
  while (idx > 1) {
    const parent = Math.floor(idx / 2);
    if (q[parent][0] > q[idx][0]) {
      [q[parent], q[idx]] = [q[idx], q[parent]];
      idx = parent;
    } else break;
  }
}

function heappop(q) {
  const value = q[1];
  if (q.length === 2) {
    q.pop();
    q.pop();
    return value;
  }

  q.splice(1, 1, q.pop());
  let idx = 1;
  const Len = q.length;

  while (idx < Len) {
    const left = idx * 2;
    const right = idx * 2 + 1;
    if (left >= Len) break;
    else if (right >= Len) {
      if (q[left][0] < q[idx][0]) {
        [q[left], q[idx]] = [q[idx], q[left]];
      }
      break;
    } else {
      let smaller = right;
      if (q[left][0] < q[right][0]) smaller = left;
      if (q[smaller][0] < q[idx][0]) {
        [q[smaller], q[idx]] = [q[idx], q[smaller]];
        idx = smaller;
        continue;
      } else break;
    }
  }
  return value;
}

const input = [];
let iter = 0;
rl.on('line', (line) => {
  input.push(line);
}).on('close', () => {
  const [V, E] = [...input[iter++].split(' ')].map((item) => Number(item));

  const graph = [...new Array(V + 1)].map(() =>
    [...new Array(V + 1)].map(() => 5000000)
  );
  for (let i = 0; i < E; i++) {
    const [a, b, c] = [...input[iter++].split(' ')].map((item) => Number(item));
    graph[a][b] = c;
  }

  for (let i = 1; i < V + 1; i++) {
    for (let j = 1; j < V + 1; j++) {
      for (let k = 1; k < V + 1; k++) {
        if (
          graph[i][j] > graph[i][k] + graph[k][j] &&
          graph[i][k] + graph[k][j] < 5000000
        )
          graph[i][j] = graph[i][k] + graph[k][j];
      }
    }
  }

  let answer = -1;
  for (let i = 1; i < V + 1; i++) {
    if (graph[i][i] >= 5000000) continue;
    if (answer === -1 || graph[i][i] < answer) answer = graph[i][i];
  }
  console.log(answer);
  process.exit();
});
