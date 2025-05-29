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
  const G=Number(input[iter++])
  const save=[]
  const answer=[]
  let i=1
  while(true){
    const now=i*i
    if (save.length>1 && now-save[0]>G) break
    for(let j=0;j<save.length;j++){
      if (now-save[j]<G) continue
      else if (now-save[j]===G) answer.push(i)
      else break
    }
    save.unshift(now)
    i+=1
  }

  if (answer.length===0) console.log(-1)
  else console.log(answer.join('\n'))
  process.exit()
})
