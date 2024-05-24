const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

function change(N, item) {
  save = [];
  for (let i = 0; i < N; i++) {
    if (item[i] === 1) save.push(3);
    else if (item[i] === 2) save.push(4);
    else if (item[i] === 3) save.push(1);
    else save.push(2);
  }
  lists.push(save);
  lists[2] = [...lists[2], ...lists[2]];
  lists.push([...lists[2]].reverse());
}

const input = [];
const lists = [];
rl.on('line', (line) => {
  input.push(line);
}).on('close', () => {
  const N = Number(input.shift());
  lists.push([...input.shift().split(' ').map(Number)]);
  lists[0] = [...lists[0], ...lists[0]];
  lists.push([...lists[0]].reverse());
  change(N, lists[0]);

  const M = Number(input.shift());
  const l = [];
  while (input.length) {
    l.push([...input.shift().split(' ').map(Number)]);
  }

  let answer = 0;
  const answers = [];
  for (let i = 0; i < M; i++) {
    let now = l[i];
    findFlag = false;

    for (let k = 0; k < 4; k++) {
      for (let j = 0; j < N; j++) {
        if (lists[k][j] === now[0]) {
          let check = lists[k].slice(j, j + N);
          if (JSON.stringify(now)===JSON.stringify(check)) {
            answer++;
            answers.push(now.join(' '));
            findFlag = true;
            break;
          }
        }
      }
      if (findFlag) break;
    }
  }

  console.log(answer);
  console.log(answers.join('\n'));

  process.exit();
});
