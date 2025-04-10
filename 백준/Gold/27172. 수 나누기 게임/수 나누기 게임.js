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
  const last=1000001
  const b=[...new Array(last)].map(item=>[])
  for(let i=0;i<N;i++){
    for(let j=l[i]*2;j<last;j+=l[i]){
      b[j].push(i)
    }
  }
  
  const answer=[...new Array(N)].map(item=>0)
  for(let i=0;i<N;i++){
    const len=b[l[i]].length
    answer[i]+=(-1)*len
    for(let j=0;j<len;j++){
      answer[b[l[i]][j]]+=1
    }
  }
  console.log(answer.join(' '))
  process.exit()
})
