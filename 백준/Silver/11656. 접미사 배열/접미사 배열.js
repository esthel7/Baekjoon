const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

rl.on("line", (line) => {
  answers=[]
  now=''
  for (let i=line.length-1;i>=0;i--){
    now=line[i]+now
    answers.push(now)
  }
  answers.sort()
  answers.forEach(item=>console.log(item))
  rl.close()
}).on("close", () => {
  process.exit()
});

