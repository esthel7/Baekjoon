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
  if (N===1){
    console.log('A')
    process.exit()
  }
  else if (N===2){
    if (l[0]===l[1]) console.log(l[0])
    else console.log('A')
    process.exit()
  }

  function calculate(a,b){
    let flag=true
    for(let i=2;i<N-1;i++){
      if (l[i]*a+b===l[i+1]) continue
      else {
        flag=false
        break
      }
    }
    if (!flag) return [flag,-1]
    return [flag,l[N-1]*a+b]
  }

  if (l[0]===l[1]){
    for(let i=2;i<N;i++){
      if (l[i]===l[0]) continue
      else {
        console.log('B')
        process.exit()
      }
    }
    console.log(l[0])
    process.exit()
  }

  const a=(l[2]-l[1])/(l[1]-l[0])
  if (Math.floor(a)!==a){
    console.log('B')
    process.exit()
  }
  const b=l[1]-l[0]*a
  const [flag,answer]=calculate(a,b)
  if (flag) console.log(answer)
  else console.log('B')

  process.exit()
})
