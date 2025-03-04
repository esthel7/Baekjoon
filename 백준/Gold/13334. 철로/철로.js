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
    let [h,o]=input[iter++].split(' ').map(item=>Number(item))
    if (h>o){
      let cnt=h
      h=o
      o=cnt
    }
    l.push([h,o])
  }
  const d=Number(input[iter++])
  const info={}
  for(let i=0;i<N;i++){
    const [h,o]=l[i]
    if (o-h>d) continue
    if (o-d in info) info[o-d]+=1
    else info[o-d]=1
    if (h+1 in info) info[h+1]-=1
    else info[h+1]=-1
  }

  const keys=Object.keys(info).sort((a,b)=>a-b)
  if (keys.length===0){
    console.log(0)
    process.exit()
  }
  let answer=info[keys[0]]
  for (let i=1;i<keys.length;i++){
    info[keys[i]]+=info[keys[i-1]]
    if (answer<info[keys[i]]) answer=info[keys[i]]
  }

  console.log(answer)
  process.exit()
})
