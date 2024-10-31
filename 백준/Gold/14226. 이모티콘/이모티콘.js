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
  const S = Number(input[iter]);
  const visit = [...new Array(2000)].map(() =>
    [...new Array(2000)].map(() => false)
  );
  visit[1][0] = true;

  const q = [[0, 1, 0]];
  while (q.length) {
    const [time, total, paste] = q.shift();
    if (total === S) {
      console.log(time);
      process.exit();
    }
    if (!visit[total][total]) {
      visit[total][total] = true;
      q.push([time + 1, total, total]);
    }
    if (paste !== 0 && total + paste < 2000 && !visit[total + paste][paste]) {
      visit[total + paste][paste] = true;
      q.push([time + 1, total + paste, paste]);
    }
    if (total !== 1 && !visit[total - 1][paste]) {
      visit[total - 1][paste] = true;
      q.push([time + 1, total - 1, paste]);
    }
  }
  process.exit();
});
