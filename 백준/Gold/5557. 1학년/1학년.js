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
  const N = Number(input[iter++]);
  const l = [...input[iter++].split(' ')].map((item) => Number(item));

  const dp = [...new Array(N + 1)].map(() => [...new Array(21)].map(() => 0n));
  dp[0][l[0]] = 1n;

  for (let i = 1; i < N - 1; i++) {
    for (let j = 0; j <= 20; j++) {
      if (dp[i - 1][j] !== 0n) {
        if (j - l[i] >= 0n) dp[i][j - l[i]] += BigInt(dp[i - 1][j]);
        if (j + l[i] <= 20n) dp[i][j + l[i]] += BigInt(dp[i - 1][j]);
      }
    }
  }

  console.log(String(dp[N - 2][l[N - 1]]));
  process.exit();
});
