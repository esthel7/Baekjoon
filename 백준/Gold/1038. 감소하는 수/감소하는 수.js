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
  const N = Number(input[iter]);
  const num = [];
  for (let i = 0; i < 10; i++) {
    num.push(i);
  }
  if (num.length > N) {
    console.log(num[N]);
    process.exit();
  }

  let start = 0;
  let end = num.length;
  while (true) {
    let flag = false;
    for (let i = start; i < end; i++) {
      for (let j = 0; j < 10; j++) {
        if (num[i] % 10 > j) {
          num.push(num[i] * 10 + j);
          flag = true;
        }
      }
      if (num.length > N) break;
    }
    if (!flag) break;
    if (num.length > N) break;
    start = end;
    end = num.length;
  }
  if (num.length <= N) console.log(-1);
  else console.log(num[N]);

  process.exit();
});
