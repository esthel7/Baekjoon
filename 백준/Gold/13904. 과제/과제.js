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
  const check=[...new Array(1000)].map(item=>false)
  const info=[]
  for(let i=0;i<N;i++){
    const [d,w]=input[iter++].split(' ').map(item=>Number(item))
    info.push([d,w])
  }
  info.sort((a,b)=>b[1]-a[1])

  let answer=0
  for(let i=0;i<N;i++){
    const [d,w]=info[i]
    for(let j=d;j>0;j--){
      if (!check[j]){
        check[j]=true
        answer+=w
        break
      }
    }
  }
  console.log(answer)
  process.exit()
})
