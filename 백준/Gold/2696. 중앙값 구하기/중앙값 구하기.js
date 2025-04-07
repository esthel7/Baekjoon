const readline=require('readline')
const rl=readline.createInterface({
  input:process.stdin,
  output:process.stdout
})

function isSmall(a,b){
  if (a<b) return true
  return false
}

function heappush(q,item){
  q.push(item)
  let loc=q.length-1
  while(loc>1){
    const parent=Math.floor(loc/2)
    if (isSmall(q[loc],q[parent])){
      [q[loc],q[parent]]=[q[parent],q[loc]];
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
  const last=q.length-1
  while(loc<last){
    const left=loc*2
    const right=left+1
    if (left>last) break
    else if (right>last){
      if (isSmall(q[left],q[loc])){
        [q[loc],q[left]]=[q[left],q[loc]]
      }
      break
    } else {
      const Min=isSmall(q[left],q[right])?left:right
      if (isSmall(q[Min],q[loc])){
        [q[loc],q[Min]]=[q[Min],q[loc]]
        loc=Min
      } else break
    }
  }
  return value
}

const input=[]
let iter=0
rl.on('line',(line)=>{
  input.push(line)
}).on('close',()=>{
  const T=Number(input[iter++])
  const answer=[]
  for(let _=0;_<T;_++){
    const M=Number(input[iter++])
    answer.push(Math.ceil(M/2))

    let now=[]
    const l=[]
    for(let i=0;i<Math.ceil(M/10);i++){
      l.push(...input[iter++].split(' ').map(item=>Number(item)))
    }

    const left=[0]
    const right=[0]
    let mid=l[0]
    now.push(mid)
    for(let i=1;i<M;i++){
      if (i%2===1){
        if (mid<l[i]) heappush(right,l[i])
        else heappush(left,(-1)*l[i])
      } else {
        if (mid<l[i]) {
          if (left.length===right.length+1) heappush(right,l[i])
          else {
            heappush(left,(-1)*mid)
            heappush(right,l[i])
            mid=heappop(right)
          }
        } else {
          if (left.length+1===right.length) heappush(left,(-1)*l[i])
          else {
            heappush(right,mid)
            heappush(left,(-1)*l[i])
            mid=heappop(left)*(-1)
          }
        }
        now.push(mid)
        if (now.length===10){
          answer.push(now.map(item=>String(item)).join(' '))
          now=[]
        }
      }
    }
    if (now.length>0) answer.push(now.map(item=>String(item)).join(' '))
  }

  console.log(answer.join('\n'))
  process.exit()
})
