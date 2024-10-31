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

  const time = [];
  for (let i = 0; i < N; i++) {
    time.push(Number(input[iter++]));
  }

  const Min = Math.min(...time);

  let start = BigInt(Min);
  let end = BigInt(Min * M);
  let answer = end;
  while (start <= end) {
    const mid = BigInt((start + end) / 2n);
    let now = 0n;
    for (let i = 0; i < N; i++) {
      now += mid / BigInt(time[i]);
    }
    if (now >= M) {
      if (answer > mid) answer = mid;
      end = mid - 1n;
    } else start = mid + 1n;
  }

  console.log(String(answer));
  process.exit();
});
