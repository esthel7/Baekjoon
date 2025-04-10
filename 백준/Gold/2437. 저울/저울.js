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
  const l=input[iter++].split(' ').map(item=>Number(item))
  l.sort((a,b)=>a-b)

  let move=1
  for(let i=0;i<N;i++){
    if (l[i]<=move) move+=l[i]
    else {
      console.log(move)
      process.exit()
    }
  }

  console.log(move)
  process.exit()
})
