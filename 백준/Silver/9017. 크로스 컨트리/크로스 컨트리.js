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
  const T = Number(input[iter++]);
  const answers = [];
  for (let _ = 0; _ < T; _++) {
    const N = Number(input[iter++]);
    const t = [...input[iter++].split(' ')];

    const team = {};
    for (let i = 0; i < N; i++) {
      if (t[i] in team) team[t[i]] += 1;
      else team[t[i]] = 1;
    }

    const total = {};
    let rank = 1;
    let answer = [-1, -1, -1];
    for (let i = 0; i < N; i++) {
      if (team[t[i]] === 6) {
        if (t[i] in total) {
          if (total[t[i]][0] === 4) {
            if (
              answer[0] === -1 ||
              answer[0] > total[t[i]][1] ||
              (answer[0] === total[t[i]][1] && answer[1] > rank)
            ) {
              answer = [total[t[i]][1], rank, t[i]];
            }
          }
          total[t[i]][0] += 1;
          total[t[i]][1] += rank;
          rank += 1;
        } else {
          total[t[i]] = [1, rank];
          rank += 1;
        }
      }
    }
    answers.push(answer[2]);
  }
  console.log(answers.join('\n'));
  process.exit();
});

// 한 팀은 6명, 상위 네명 합해서 점수 계산
// 가장 낮은 점수가 우승
// 여섯명이 참여해야함
// 동점이면 5번째 주자 점수
