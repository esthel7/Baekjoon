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
  let last=-2
  let answer=0
  let first=false
  for(let i=0;i<N-1;i++){
    if (C[i]>0) answer+=C[i]
    else {
      if (i===0) first=true
      if (last+1!==i) {
        last=i
        answer+=1
      }
    }
  }
  if (C[N-1]>0) answer+=C[N-1]
  else if (last!==N-2 && !first) answer+=1
  console.log(answer)
  process.exit()
})
