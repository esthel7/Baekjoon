const readline=require('readline')
const rl=readline.createInterface({
  input:process.stdin,
  output:process.stdout
})

let input=[]
let iter=0
rl.on('line',(line)=>{
  input.push(line)
}).on('close',()=>{
  const N=Number(input[iter++])
  let l=input[iter++].split(' ').map(item=>Number(item))
  let answer=0
  const info={}
  for (let i=0;i<N;i++){
    if (l[i]+1 in info) {
      info[l[i]+1]-=1
      if (info[l[i]+1]===0) delete(info[l[i]+1])
      if (l[i] in info) info[l[i]]+=1
      else info[l[i]]=1
    }
    else {
      if (l[i] in info) info[l[i]]+=1
      else info[l[i]]=1
      answer+=1
    }
  }
  console.log(answer)
  process.exit()
})
