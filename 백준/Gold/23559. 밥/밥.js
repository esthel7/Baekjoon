const readline=require('readline')
const rl=readline.createInterface({
  input:process.stdin,
  output:process.stdout
})

// 23559

const input=[]
let iter=0
rl.on('line',(line)=>{
  input.push(line)
}).on('close',()=>{
  const [N,X]=input[iter++].split(' ').map(item=>Number(item))
  const l=[]
  let answer=0
  const diff=[]
  for(let i=0;i<N;i++){
    const [A,B]=input[iter++].split(' ').map(item=>Number(item))
    l.push([A,B])
    answer+=B
    if (A-B>0) diff.push(A-B)
  }

  let money=1000*N
  diff.sort((a,b)=>b-a)
  for(let i=0;i<diff.length;i++){
    if (money+4000>X) break
    answer+=diff[i]
    money+=4000
  }

  console.log(answer)
  process.exit()
})
