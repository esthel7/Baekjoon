const readline=require('readline')
const rl=readline.createInterface({
  input:process.stdin,
  output:process.stdout
})

const input=[]
let iter=0
rl.on('line',(line)=>{
  input.push(line)
}).on('close',()=>{
  const N=Number(input[iter++])
  const [mp,mf,ms,mv]=input[iter++].split(' ').map(item=>Number(item))
  const l=[0]
  for(let i=0;i<N;i++){
    l.push(input[iter++].split(' ').map(item=>Number(item)))
  }

  let answer=-1
  let answers=[]

  function calculate(now){
    let cnt=[0,0,0,0]
    let total=0
    for(let i=0;i<now.length;i++){
      const idx=now[i]
      for(let j=0;j<4;j++){
        cnt[j]+=l[idx][j]
      }
      total+=l[idx][4]
    }
    if (cnt[0]>=mp && cnt[1]>=mf && cnt[2]>=ms && cnt[3]>=mv){
      if (answer===-1 || answer>total) {
        answer=total
        answers=[...now]
      }
    }
  }
  
  function make(now,idx){
    calculate(now)
    for(let i=idx;i<=N;i++){
      now.push(i)
      make(now,i+1)
      now.pop()
    }
  }

  make([],1)

  if (answer===-1){
    console.log(answer)
    process.exit()
  }
  console.log(answer)
  console.log(answers.join(' '))
  process.exit()
})
