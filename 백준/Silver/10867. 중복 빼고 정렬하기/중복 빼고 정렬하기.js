const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let input = [];
rl.on('line', (line) => {
  input.push(line);
}).on('close', () => {
  line = [...input[1].split(' ').map(Number)];
  line = [...new Set(line)];
  line.sort((a, b) => a - b);
  console.log(line.join(' '));
  process.exit();
});
