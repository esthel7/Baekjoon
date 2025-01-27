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
  let l=input[iter++].split(' ').map(item=>Number(item))
  let S=Number(input[iter++])
  let start=0
  function find(){
    let max=[l[start],-1]
    const last=Math.min(N,start+S+1)
    for (let i=start+1;i<last;i++){
      if (max[0]<l[i]) max=[l[i],i]
    }
    if (max[0]!==l[start]){
      S-=max[1]-start
      l.splice(max[1],1)
      l.splice(start,0,max[0])
    }
    start+=1
    if (start<N && S>0) find()
  }
  find()
  console.log(l.join(' '))
  process.exit()
})
