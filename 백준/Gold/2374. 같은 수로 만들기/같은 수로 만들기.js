const readline=require('readline')
const rl=readline.createInterface({
  input:process.stdin,
  output:process.stdout
})

function isSmall(a,b){
  if (a[0]<b[0]) return true
  return false
}

function heappush(q,item){
  q.push(item)
  let loc=q.length-1
  while(loc>1){
    const parent=Math.floor(loc/2)
    if (isSmall(q[loc],q[parent])){
      [q[loc],q[parent]]=[q[parent],q[loc]]
      loc=parent
    } else break
  }
}

function heappop(q){
  const value=q[1]
  if (q.length<=2){
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
    if (right>=last){
      if (isSmall(q[left],q[loc])){
        [q[loc],q[left]]=[q[left],q[loc]]
      }
      break
    }
    const Min=isSmall(q[left],q[right])?left:right
    if (isSmall(q[Min],q[loc])){
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
  const l=[]
  for(let i=0;i<n;i++){
    l.push(Number(input[iter++]))
  }

  const point={[0]:[-1,1]}
  let last=0
  const q=[0,[l[0],0]]
  for(let i=1;i<n;i++){
    if (l[i-1]===l[i]) continue
    point[last][1]=i
    point[i]=[last,i+1]
    last=i
    heappush(q,[l[i],i])
  }
  point[last][1]=n

  let answer=0
  while(q.length>2){
    // console.log(q,point,'answer',answer,l)
    const [value,idx]=heappop(q)
    const [start,end]=point[idx]
    let Min=1000000001
    let loc=idx
    if (start!==-1){
      Min=l[start]
      loc=start
    }
    if (end!==n && Min>l[end]){
      Min=l[end]
      loc=end
    }
    const diff=Min-l[idx]
    l[idx]+=diff
    answer+=diff
    if (start!==-1) point[start][1]=end
    if (end!==n) point[end][0]=start
    delete(point[idx])
  }

  console.log(answer)
  process.exit()
})
