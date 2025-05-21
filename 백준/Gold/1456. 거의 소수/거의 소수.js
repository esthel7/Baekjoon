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
  const [A,B]=input[iter++].split(' ').map(item=>Number(item))
  let answer=0
  const last=Math.ceil(B**0.5)+1
  const l=[...new Array(last)].map(item=>true)
  for(let i=2;i<last;i++){
    if (l[i]){
      let now=i*i
      while(now<=B){
        if (A<=now) answer+=1
        now*=i
      }
      for(let j=i+i;j<last;j+=i){
        l[j]=false
      }
    }
  }
  console.log(answer)
  process.exit()
})
