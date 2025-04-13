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
  const T=Number(input[iter++])
  const answer=[]
  const last=1000000
  const total=[...new Array(last+1)].map(item=>1)
  total[0]=0

  for(let i=2;i<=last;i++){
    for(let j=i;j<=last;j+=i){
      total[j]+=i
    }
  }

  for(let i=1;i<=last;i++){
    total[i]+=total[i-1]
  }

  for(let _=0;_<T;_++){
    const N=Number(input[iter++])
    answer.push(total[N])
  }

  console.log(answer.join('\n'))
  process.exit()
})
