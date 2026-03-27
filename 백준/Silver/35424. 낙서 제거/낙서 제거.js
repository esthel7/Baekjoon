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
  const [N,K]=input[iter++].split(' ').map(item=>Number(item))
  const l=input[iter++].split(' ').map(item=>Number(item)-1)

  let line=0
  let start=l[0]
  let end=l[0]

  let answer=0
  for(let i=0;i<N;i++){
    start=Math.min(start,l[i])
    end=Math.max(end,l[i])
    let now=(i-line+1)*(end-start+1)
    if (now<=K) continue
    line=i
    answer+=1
    start=l[i]
    end=l[i]
  }

  console.log(answer+1)
  process.exit()
})
