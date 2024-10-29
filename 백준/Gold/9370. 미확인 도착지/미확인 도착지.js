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
      [q[idx], q[parent]] = [q[parent], q[idx]];
      idx = parent;
      continue;
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
  const Len = q.length;
  let idx = 1;
  while (idx < Len) {
    const left = idx * 2;
    const right = idx * 2 + 1;
    if (left >= Len) break;
    else if (right >= Len) {
      if (q[left][0] > q[idx][0]) {
        [q[left], q[idx]] = [q[idx], q[left]];
        idx = left;
        continue;
      } else break;
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
  const T = Number(input[iter++]);
  const answers = [];
  for (let _ = 0; _ < T; _++) {
    const [n, m, t] = [...input[iter++].split(' ')].map((item) => Number(item));
    const [s, g, h] = input[iter++].split(' ');

    const graph = {};
    for (let i = 1; i <= n; i++) {
      graph[String(i)] = [];
    }
    for (let i = 0; i < m; i++) {
      let [a, b, d] = input[iter++].split(' ');
      d = Number(d);
      graph[a].push([d, b]);
      graph[b].push([d, a]);
    }

    const possible = {};
    for (let i = 0; i < t; i++) {
      possible[input[iter++]] = true;
    }

    function find(start) {
      const visit = {};
      for (let i = 1; i <= n; i++) {
        visit[String(i)] = -1;
      }
      visit[start] = 0;

      const q = [0, [0, start]];
      while (q.length > 1) {
        const [total, start] = heappop(q);
        for (let i = 0; i < graph[start].length; i++) {
          const [cost, end] = graph[start][i];
          if (visit[end] === -1 || visit[end] > total + cost) {
            visit[end] = total + cost;
            heappush(q, [visit[end], end]);
          }
        }
      }
      return visit;
    }

    const S = find(s);
    const G = find(g);
    const H = find(h);

    const keys = [...Object.keys(possible)];
    for (let i = 0; i < keys.length; i++) {
      const node = keys[i];
      let answer = -2;
      if (S[g] !== -1 && H[node] !== -1) {
        const value = S[g] + G[h] + H[node];
        answer = value;
      }
      if (S[h] !== -1 && G[node] !== -1) {
        const value = S[h] + H[g] + G[node];
        if (answer === -2) answer = value;
        else answer = Math.min(answer, value);
      }
      if (answer !== S[node]) delete possible[node];
    }

    answers.push(
      [...Object.keys(possible)]
        .map((item) => Number(item))
        .sort((a, b) => a - b)
        .join(' ')
    );
  }
  console.log(answers.join('\n'));
  process.exit();
});
