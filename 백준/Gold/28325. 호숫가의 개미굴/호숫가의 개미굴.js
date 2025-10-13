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
  const C=input[iter++].split(' ').map(item=>Number(item))
  let start=0
  for(let i=0;i<N;i++){
    if (C[i]>0) {
      start=i
      break
    }
  }
  if (start===0 && C[0]===0) {
    console.log(Math.floor(N/2))
    process.exit()
  }
  let last=-2
  let answer=0
  let first=false
  for(let i=start;i<start+N-1;i++){
    if (C[i%N]>0) answer+=C[i%N]
    else {
      if (i===start) first=true
      if (last+1!==i) {
        last=i
        answer+=1
      }
    }
  }
  if (C[(start+N-1)%N]>0) answer+=C[(start+N-1)%N]
  else if (last!==start+N-2 && !first) answer+=1
  console.log(answer)
  process.exit()
})
