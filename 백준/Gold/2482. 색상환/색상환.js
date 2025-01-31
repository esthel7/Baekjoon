const fs = require('fs');
const path = process.platform === 'linux' ? '/dev/stdin' : 'input.txt';
const [n, k] = fs.readFileSync(path).toString().trim().split('\n').map(Number);

const dp = Array.from({ length: n + 1 }, () => Array(k + 1).fill(0));
const mod = 1000000003;

for (let i = 0; i <= n; i++) {
  dp[i][0] = 1;
  dp[i][1] = i;
}

for (let i = 2; i <= n; i++) {
  for (let j = 2; j <= k; j++) {
    dp[i][j] = dp[i - 1][j] + dp[i - 2][j - 1];
    dp[i][j] %= mod;
  }
}

const ans = (dp[n - 1][k] + dp[n - 3][k - 1]) % mod;
console.log(ans);