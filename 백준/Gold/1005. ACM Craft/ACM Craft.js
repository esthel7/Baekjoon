let input = require('fs').readFileSync('/dev/stdin').toString().split('\n');
let iter = 0;

const test = input[iter++];
const answers = [];
for (let _ = 0; _ < test; _++) {
  const command = input[iter++].split(' ');
  const N = Number(command[0]);
  const K = Number(command[1]);

  const time = [0].concat([
    ...input[iter++].split(' ').map((item) => Number(item)),
  ]);
  const next = [...new Array(N + 1)].map(() => []);
  const root = [...new Array(N + 1)].map(() => 0);

  for (let i = 0; i < K; i++) {
    const link = input[iter++]
      .split(' ')
      .map((item) => Number(item));
    next[link[0]].push(link[1]);
    root[link[1]] += 1;
  }

  const W = Number(input[iter++]);
  const final = [...new Array(N + 1)].map(() => -1);
  const building = [];
  for (let i = 1; i < N + 1; i++) {
    if (root[i] === 0) {
      building.push(i);
      final[i] = time[i];
    }
  }

  while (building.length) {
    const num = building.shift();
    for (let i = 0; i < next[num].length; i++) {
      const link = next[num][i];
      root[link] -= 1;
      final[link] = Math.max(final[link], final[num] + time[link]);
      if (root[link] === 0) building.push(link);
    }
  }

  answers.push(final[W]);
}
console.log(answers.join('\n'));
process.exit();
