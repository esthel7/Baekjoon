const readline=require('readline')
const rl=readline.createInterface({
  input:process.stdin,
  output:process.stdout
})

const input=[]
let iter=0
rl.on('line',(line)=>[
  input.push(line)
]).on('close',()=>{
  const N=Number(input[iter++])
  const l=[]
  for(let i=0;i<N;i++){
    l.push(Number(input[iter++]))
  }
  l.sort((a,b)=>a-b)

  let answer=0
  let num=1
  for(let i=0;i<N;i++){
    if (l[i]<num) continue
    if (l[i]===num) {
      num+=1
      continue
    }
    answer+=l[i]-num
    num+=1
  }

  console.log(answer)
  process.exit()
})

// 1부터 연속된 숫자로 되어야함
