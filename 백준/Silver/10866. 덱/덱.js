const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let input = [];
rl.on('line', (line) => {
  input.push(line);
}).on('close', () => {
  n = input.shift();
  save = [];
  answer = [];
  for (let i = 0; i < n; i++) {
    now = input[i].split(' ');
    if (now.length === 2) {
      // push
      if (now[0] === 'push_back') save.push(now[1]);
      else save.unshift(now[1]);
    } else {
      now = now[0];
      if (now === 'pop_front') {
        if (save.length === 0) answer.push(-1);
        else {
          answer.push(save.shift());
        }
      } else if (now === 'pop_back') {
        if (save.length === 0) answer.push(-1);
        else {
          answer.push(save.pop());
        }
      } else if (now === 'size') answer.push(save.length);
      else if (now === 'empty') {
        if (save.length === 0) answer.push(1);
        else answer.push(0);
      } else if (now === 'front') {
        if (save.length === 0) answer.push(-1);
        else answer.push(save[0]);
      } else {
        if (save.length === 0) answer.push(-1);
        else answer.push(save[save.length-1]);
      }
    }
  }
  answer=answer.join('\n');
  console.log(answer);
  process.exit();
});
