const readline = require('readline');
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let input = [];
rl.on('line', (line) => {
  input.push(line);
}).on('close', () => {
  function change(next, now) {
    if (l[next] == 0) l[next] = now;
    else if (l[next] > now) l[next] = now;
  }

  let N = Number(input.shift());
  if (N == 1) {
    console.log(0);
    process.exit();
  }
  if (N <= 3) {
    console.log(1);
    process.exit();
  }

  let l = [];
  for (let i = 0; i <= N; i++) {
    l.push(0);
  }
  for (let i = 1; i < N; i++) {
    if (i * 2 <= N) change(i * 2, l[i] + 1);
    if (i * 3 <= N) change(i * 3, l[i] + 1);
    if (i + 1 <= N) change(i + 1, l[i] + 1);
  }
  console.log(l[N])
  process.exit();
});
