const readline = require('readline');
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let input = [];
let iter = 0;
rl.on('line', (line) => {
  input.push(line);
}).on('close', () => {
  function exchangeFirst(change) {
    // 곱하기 나누기
    for (let i = 0; i < change.length; i++) {
      if (change[i] === '*' || change[i] === '/') {
        const newLine = change[i - 1] + change[i + 1] + change[i];
        change.splice(i - 1, 2);
        change[i - 1] = newLine;
        i -= 1;
      }
    }
    return change;
  }

  function exchangeSecond(change) {
    // 더하기 빼기
    for (let i = 0; i < change.length; i++) {
      if (change[i] === '+' || change[i] === '-') {
        const newLine = change[i - 1] + change[i + 1] + change[i];
        change.splice(i - 1, 2);
        change[i - 1] = newLine;
        i -= 1;
      }
    }
    return change;
  }

  function inside(idx) {
    // 괄호 해결
    let change = [];
    let last = 0;
    for (let i = idx + 1; i < now.length; i++) {
      if (now[i] === '(') {
        inside(i);
        i -= 1;
        continue;
      } else if (now[i] === ')') {
        last = i;
        break;
      }
      change.push(now[i]);
    }
    now.splice(idx, last - idx);
    change = exchangeFirst(change);
    change = exchangeSecond(change);
    now[idx] = change.join();
  }

  let now = [...input[iter++]];
  for (let i = 0; i < now.length; i++) {
    if (now[i] === '(') inside(i);
  }
  now = exchangeFirst(now);
  now = exchangeSecond(now);
  console.log(now.join());
  process.exit();
});
