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
  const parent=input[iter++].split(' ').map(item=>Number(item))
  const child=[...new Array(N)].map(item=>[])
  for(let i=1;i<N;i++){
    child[parent[i]].push(i)
  }

  function find(node){
    if (child[node].length===0) return 1
    const time=[]
    for(let i=0;i<child[node].length;i++){
      time.push(find(child[node][i]))
    }
    time.sort((a,b)=>b-a)

    let now=1
    let Max=1
    for(let i=0;i<time.length;i++){
      if (now+time[i]>Max) Max=now+time[i]
      now+=1
    }
    return Max
  }
  console.log(find(0)-1)

  process.exit()
})
