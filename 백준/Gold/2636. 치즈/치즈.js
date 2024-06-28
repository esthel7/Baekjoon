const readline = require('readline');
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let input = [];
rl.on('line', (line) => {
  input.push(line);
}).on('close', () => {
  const [X, Y] = input.shift().split(' ').map(Number);
  let l = [];
  let prev = 0;
  for (let i = 0; i < X; i++) {
    const now = input.shift().split(' ').map(Number);
    for (let j = 0; j < Y; j++) {
      if (now[j] == 1) prev += 1;
    }
    l.push(now);
  }

  const xbox = [-1, 1, 0, 0];
  const ybox = [0, 0, -1, 1];

  let left = prev;
  let time = 0;
  while (true) {
    if (left == 0) {
      console.log(time);
      console.log(prev);
      break;
    }
    time += 1;

    let visited = [];
    for (let i = 0; i < X; i++) {
      visited.push([]);
      for (let j = 0; j < Y; j++) {
        visited[i].push(false);
      }
    }
    let q = [[0, 0]];
    visited[0][0] = true;

    prev = 0;
    while (q.length > 0) {
      const [x, y] = q.shift();
      if (l[x][y] == 1) {
        l[x][y] = 0;
        prev += 1;
        continue;
      } else {
        for (let i = 0; i < 4; i++) {
          let newX = x + xbox[i];
          let newY = y + ybox[i];
          if (
            0 <= newX &&
            newX < X &&
            0 <= newY &&
            newY < Y &&
            !visited[newX][newY]
          ) {
            visited[newX][newY] = true;
            q.push([newX, newY]);
          }
        }
      }
    }

    left -= prev;
  }
  process.exit();
});
