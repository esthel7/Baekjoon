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
  const l=[...input[iter++]]
  let x=0
  let y=0
  for(let i=0;i<l.length;i++){
    if (l[i]==='S') x+=1
    if (l[i]==='L') y+=1
  }

  let answer=''
  for(let i=0;i<x;i++){
    answer+='SciCom'
  }
  for(let i=0;i<y;i++){
    answer+='Love'
  }
  console.log(answer)

  process.exit()
})
