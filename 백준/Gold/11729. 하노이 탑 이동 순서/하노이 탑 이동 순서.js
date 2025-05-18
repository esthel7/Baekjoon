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
  const answer=[]
  
  function move(left,start,mid,end){
    if (left===1){
      answer.push(`${start} ${end}`)
      return
    }
    move(left-1,start,end,mid)
    answer.push(`${start} ${end}`)
    move(left-1,mid,start,end)
  }

  move(N,1,2,3)

  console.log(answer.length+'\n'+answer.join('\n'))
  process.exit()
})
