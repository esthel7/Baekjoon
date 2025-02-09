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
  const l=input[iter++].split('')
  const s=[...new Array(4)].map(item=>[])
  for(let i=0;i<N;i++){
    if (l[i]==='D') s[0].push(i)
    else if (l[i]==='K') s[1].push(i)
    else if (l[i]==='S') s[2].push(i)
    else if (l[i]==='H') s[3].push(i)
  }

  let answer=0
  function find(idx,start){
    if (idx===4){
      answer+=1
      return
    }
    for(let i=0;i<s[idx].length;i++){
      if (s[idx][i]<start) continue
      find(idx+1,s[idx][i]+1)
    }
  }
  for(let i=0;i<s[0].length;i++){
    find(1,s[0][i]+1)
  }
  console.log(answer)
  process.exit()
})
