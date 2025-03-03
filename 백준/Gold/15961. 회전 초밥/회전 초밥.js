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
  let [N,d,k,c]=input[iter++].split(' ').map(item=>Number(item))
  let l=[]
  for(let i=0;i<N;i++){
    l.push(Number(input[iter++]))
  }
  l=[...l,...l]

  const info={[c]:1}
  for(let i=0;i<k;i++){
    if (l[i] in info) info[l[i]]+=1
    else info[l[i]]=1
  }
  let answer=Object.keys(info).length
  let cnt=answer

  for(let i=1;i<N;i++){
    const left=l[i-1]
    info[left]-=1
    if (info[left]===0) {
      delete(info[left])
      cnt-=1
    }
    const value=l[i+k-1]
    if (value in info) info[value]+=1
    else {
      info[value]=1
      cnt+=1
    }
    if (answer<cnt) answer=cnt
  }

  console.log(answer)
  process.exit()
})
