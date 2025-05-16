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
  let k=Number(input[iter++])

  const info=[2]
  let prev=2
  while(true){
    prev*=2
    info.push(info[info.length-1]+prev)
    if (info[info.length-1]>=k) break
  }

  let answer=[]
  while(k!==0){
    if (k===1){
      answer.push(4)
      break                                 
    }
    if (k===2){
      answer.push(7)
      break
    }
    for(let i=info.length-1;i>=0;i--){
      if (k<=info[i]){
        const diff=info[i]-info[i-1]
        const half=info[i-1]+(diff/2)
        if (k<=half) {
          answer.push(4)
          k-=diff/2
        }
        else {
          answer.push(7)
          k-=diff
        }
        info.pop()
        break
      }
    }
  }
  console.log(answer.join(''))
  process.exit()
})
