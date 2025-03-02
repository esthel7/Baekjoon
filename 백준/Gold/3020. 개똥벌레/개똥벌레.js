const readline=require('readline')
const rl=readline.createInterface({
  input:process.stdin,
  output:process.stdout
})

// 개똥벌레 

function heappush(q,item){
  q.push(item)
  let loc=q.length-1
  while (loc>=1){
    const parent=Math.floor(loc/2)
    if (q[parent]>q[loc]){
      [q[parent],q[loc]]=[q[loc],q[parent]]
      loc=parent
    }
    else break
  }
}

function heappop(q){
  const value=q[1]
  q.splice(1,1,q.pop())
  let loc=1
  const last=q.length
  while (loc<last){
    const left=loc*2
    const right=loc*2+1
    if (left>=last) break
    else if (right>=last){
      if (q[loc]>q[left]) [q[left],q[loc]]=[q[loc],q[left]]
      break
    }
    const Min=q[left]>q[right]?right:left
    if (q[loc]>q[Min]) {
      [q[Min],q[loc]]=[q[loc],q[Min]]
      loc=Min
    } else break
  }
  return value
}

const input=[]
let iter=0
rl.on('line',(line)=>{
  input.push(line)
}).on('close',()=>{
  const [N,H]=input[iter++].split(' ').map(item=>Number(item))
  const l=[...new Array(H)].map(item=>0)
  for (let i=0;i<N;i++){
    const value=Number(input[iter++])
    if(i%2===0){
      l[0]+=1
      l[value]-=1
    } else {
      l[H-value]+=1
    }
  }

  const q=[0,l[0]]
  for(let i=1;i<H;i++){
    l[i]+=l[i-1]
    heappush(q,l[i])
  }
  
  const answer=heappop(q)
  let cnt=1
  while (q.length>1){
    const now=heappop(q)
    if (answer===now) cnt+=1
    else break
  }
  console.log(answer,cnt)
  process.exit()
})
