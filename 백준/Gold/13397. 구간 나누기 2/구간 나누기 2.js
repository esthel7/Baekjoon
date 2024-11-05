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
  const [N, M] = [...input[iter++].split(' ')].map((item) => Number(item));
  const l = [...input[iter++].split(' ')].map((item) => Number(item));
  let start = 0;
  let end = Math.max(...l);

  function calculate(mid) {
    let cnt = 1;
    let Min = l[0];
    let Max = l[0];
    for (let i = 0; i < N; i++) {
      if (Min > l[i]) Min = l[i];
      if (Max < l[i]) Max = l[i];
      if (Max - Min > mid) {
        cnt += 1;
        Min = l[i];
        Max = l[i];
      }
    }
    if (cnt <= M) return true;
    return false;
  }

  let answer = end - start;
  while (start <= end) {
    const mid = Math.floor((start + end) / 2);
    if (calculate(mid)) {
      answer = Math.min(answer, mid);
      end = mid - 1;
    } else start = mid + 1;
  }
  console.log(answer);

  process.exit();
});
