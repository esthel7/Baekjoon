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
  const l=[]
  for(let i=0;i<N;i++){
    const [T,S]=input[iter++].split(' ').map(item=>Number(item))
    l.push([S,T])
  }
  l.sort((a,b)=>b[0]-a[0])
  
  let time=l[0][0]
  for(let i=0;i<N;i++){
    if (time<=l[i][0]) time-=l[i][1]
    else time=l[i][0]-l[i][1]
    if (time<0){
      time=-1
      break
    }
  }
  console.log(time)
  process.exit()
})
