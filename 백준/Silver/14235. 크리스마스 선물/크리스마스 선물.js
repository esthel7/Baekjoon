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
    if (q[parent] > q[idx]) {
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
  const Len = q.length;
  let idx = 1;
  while (idx < Len) {
    const left = idx * 2;
    const right = idx * 2 + 1;
    if (left >= Len) break;
    else if (right >= Len) {
      if (q[idx] > q[left]) {
        [q[idx], q[left]] = [q[left], q[idx]];
        idx = left;
        continue;
      } else break;
    } else {
      let smaller = right;
      if (q[left] < q[right]) smaller = left;
      if (q[smaller] < q[idx]) {
        [q[idx], q[smaller]] = [q[smaller], q[idx]];
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
  const n = Number(input[iter++]);
  const answers = [];
  const gift = [];
  for (let i = 0; i < n; i++) {
    const a = [...input[iter++].split(' ')].map((item) => Number(item));
    if (a[0] === 0) {
      if (!gift.length) answers.push(-1);
      else answers.push(heappop(gift) * -1);
    } else {
      for (let j = 1; j <= a[0]; j++) {
        heappush(gift, -a[j]);
      }
    }
    // console.log(gift)
  }

  console.log(answers.join('\n'));
  process.exit();
});
