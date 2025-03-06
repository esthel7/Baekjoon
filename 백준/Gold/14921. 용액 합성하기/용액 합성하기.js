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

  let answer=l[0]+l[N-1]
  let left=0
  let right=N-1
  while (left<right){
    const value=l[left]+l[right]
    if (Math.abs(value)<Math.abs(answer)) answer=value
    if (value===0) {
      answer=0
      break
    }
    else if (value>0){
      right-=1
    }
    else {
      left+=1
    }
  }

  console.log(answer)
  process.exit()
})
