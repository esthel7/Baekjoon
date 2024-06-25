const { info } = require('console');
const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let input = [];
rl.on('line', (line) => {
  input.push(line);
}).on('close', () => {
  T = Number(input.shift());
  for (let i = 0; i < T; i++) {
    [N, M] = input.shift().split(' ');
    N=Number(N)
    M = Number(M);
    l = input.shift().split(' ');

    let info = [];
    for (let i = 0; i < N; i++) {
      l[i] = [Number(l[i]), i];
      info.push(l[i][0]);
    }
    info.sort((a, b) => b - a);

    let cnt=0
    while (l.length>0) {
      if (l[0][0]==info[0]){
        cnt+=1
        if (l[0][1]==M){
          console.log(cnt)
          break
        }
        info.shift()
        l.shift()
      }
      else{
        l.push(l.shift())
      }
    }
  }
  process.exit();
});
