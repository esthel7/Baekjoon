const readline = require('readline');
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const input = [];
let iter = 0;
rl.on('line', (line) => {
  input.push(line);
}).on('close', () => {
  const l = [...input[iter]].map((item) => Number(item));

  function how(cnt) {
    let now = 0;
    for (let i = 1; i < 10; i++) {
      now += 1;
      if (now === cnt) return i;
    }
    for (let i = 10; i <= 50; i++) {
      now += 2;
      if (now === cnt) return i;
    }
  }
  const last = l.length;
  const N = how(last);
  const visit = [...new Array(N + 1)].map(() => false);

  function find(idx, now) {
    if (idx === last) {
      console.log(now.trim());
      process.exit();
    }
    if (!visit[l[idx]]) {
      visit[l[idx]] = true;
      find(idx + 1, now + String(l[idx]) + ' ');
      visit[l[idx]] = false;
    }
    if (
      idx + 1 < last &&
      l[idx] * 10 + l[idx + 1] <= N &&
      !visit[l[idx] * 10 + l[idx + 1]]
    ) {
      visit[l[idx] * 10 + l[idx + 1]] = true;
      find(idx + 2, now + String(l[idx] * 10 + l[idx + 1]) + ' ');
      visit[l[idx] * 10 + l[idx + 1]] = false;
    }
  }
  find(0, '');

  process.exit();
});
