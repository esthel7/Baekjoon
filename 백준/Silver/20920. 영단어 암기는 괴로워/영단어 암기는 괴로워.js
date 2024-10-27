const readline = require('readline');
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

function isSmaller(q, a, b) {
  if (
    q[a][0] < q[b][0] ||
    (q[a][0] === q[b][0] && q[a][1] < q[b][1]) ||
    (q[a][0] === q[b][0] && q[a][1] === q[b][1] && q[a][2] < q[b][2])
  ) {
    return true;
  }
  return false;
}

function heappush(q, item) {
  if (!q.length) {
    q.push(0);
    q.push(item);
    return;
  }
  let idx = q.length;
  q.push(item);
  while (idx > 1) {
    const parent = Math.ceil(idx / 2);
    if (isSmaller(q, idx, parent)) {
      [q[parent], q[idx]] = [q[idx], q[parent]];
      idx = parent;
    } else break;
  }
}

function heappop(q) {
  if (q.length == 2) {
    const value = q.pop();
    q.pop();
    return value;
  }

  const value = q[1];
  q.splice(1, 1, q.pop());

  let idx = 1;
  const Len = q.length;
  while (idx < Len) {
    const left = idx * 2;
    const right = idx * 2 + 1;
    if (left >= Len) break;
    else if (right >= Len) {
      if (isSmaller(q, left, idx)) {
        [q[left], q[idx]] = [q[idx], q[left]];
        idx = left;
        continue;
      }
    } else {
      let smaller = right;
      if (isSmaller(q, left, right)) smaller = left;
      if (isSmaller(q, smaller, idx)) {
        [q[smaller], q[idx]] = [q[idx], q[smaller]];
        idx = smaller;
        continue;
      }
    }
    break;
  }
  return value;
}

let input = [];
let iter = 0;
rl.on('line', (line) => {
  input.push(line);
}).on('close', () => {
  const [N, M] = [...input[iter++].split(' ')].map((item) => Number(item));
  const info = {};
  for (let i = 0; i < N; i++) {
    const word = input[iter++];
    if (word.length < M) continue;
    if (word in info) info[word] += 1;
    else info[word] = 1;
  }

  const keys = Object.keys(info);
  const q = {};
  for (let i = 0; i < keys.length; i++) {
    // heappush(q, [-info[keys[i]], -keys[i].length, keys[i]]);
    // q.push([-info[keys[i]], -keys[i].length, keys[i]]);
    if (!(info[keys[i]] in q)) q[info[keys[i]]] = {};
    if (keys[i].length in q[info[keys[i]]])
      q[info[keys[i]]][keys[i].length].push(keys[i]);
    else q[info[keys[i]]][keys[i].length] = [keys[i]];
  }

  const answers = [];
  // while (q.length >= 2) {
  //   const [num, Len, key] = heappop(q);
  //   answers.push(key);
  // }
  const freq = Object.keys(q).sort((a, b) => b - a);
  for (let i = 0; i < freq.length; i++) {
    const num = Object.keys(q[freq[i]]).sort((a, b) => b - a);
    for (let j = 0; j < num.length; j++) {
      const now = q[freq[i]][num[j]].sort();
      for (let k = 0; k < now.length; k++) {
        answers.push(now[k]);
      }
    }
  }
  console.log(answers.join('\n'));
  process.exit();
});
