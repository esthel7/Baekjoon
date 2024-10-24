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
  const A = Number(input[iter++]);
  const l = [...input[iter++].split(' ')].map((item) => Number(item));

  const dp = [[l[0], l[0]]];
  for (let i = 1; i < A; i++) {
    let insertFlag = false;
    for (let j = 0; j < dp.length; j++) {
      const [value, key] = dp[j];
      if (key < l[i]) {
        insertFlag = true;
        const newValue = value + l[i];
        for (let k = 0; k <= j; k++) {
          if (dp[k][0] < newValue) {
            dp.splice(k, 0, [newValue, l[i]]);
            break;
          }
        }
        break;
      }
    }
    if (!insertFlag) dp.push([l[i], l[i]]);
  }
  console.log(dp[0][0]);
  process.exit();
});
