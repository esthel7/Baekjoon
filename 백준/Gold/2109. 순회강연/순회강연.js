const readline=require('readline')
const rl=readline.createInterface({
  input:process.stdin,
  output:process.stdout
})

function heappush(q,item){
  q.push(item)
  let loc=q.length-1
  while(loc>1){
    const parent=Math.floor(loc/2)
    if (q[loc]<q[parent]){
      [q[parent],q[loc]]=[q[loc],q[parent]]
      loc=parent
    } else break
  }
}

function heappop(q){
  const value=q[1]
  if (q.length===2){
    q.pop()
    return value
  }
  q.splice(1,1,q.pop())
  let loc=1
  const last=q.length
  while(loc<last){
    const left=loc*2
    const right=loc*2+1
    if (left>=last) break
    else if (right>=last){
      if (q[left]<q[loc]){
        [q[loc],q[left]]=[q[left],q[loc]]
      }
      break
    }
    const Min=q[left]>q[right]?right:left
    if (q[Min]<q[loc]){
      [q[loc],q[Min]]=[q[Min],q[loc]]
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
  const n=Number(input[iter++])
  const info={}
  for(let i=0;i<n;i++){
    const [p,d]=input[iter++].split(' ').map(item=>Number(item))
    if (d in info) heappush(info[d],-p)
    else info[d]=[0,-p]
  }

  const keys=Object.keys(info).map(item=>Number(item)).sort((a,b)=>a-b)
  const q=[0]
  let time=1
  for(let i=0;i<keys.length;i++){
    while(info[keys[i]].length>1){
      const item=heappop(info[keys[i]])*(-1)
      if (time>keys[i]){
        if (q.length>=2&&q[1]<item){
          heappop(q)
          heappush(q,item)
          continue
        } else break
      }
      heappush(q,item)
      time+=1
    }
  }

  // console.log(q)

  let answer=0
  for(let i=0;i<q.length;i++){
    answer+=q[i]
  }
  console.log(answer)

  process.exit()
})

// 20 100 10 5 50
