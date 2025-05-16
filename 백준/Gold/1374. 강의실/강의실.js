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
  if (q.length===2){
    q.pop()
    return value
  }
  q.splice(1,1,q.pop())
  let loc=1
  const last=q.length
  while(loc<last){
    let left=loc*2
    let right=loc*2+1
    if (left>=last) break
    if (right>=last){
      if (isSmall(q[left],q[loc])) {
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
  const N=Number(input[iter++])
  const save=[]
  for(let i=0;i<N;i++){
    const [num,start,end]=input[iter++].split(' ').map(item=>Number(item))
    save.push([start,end,num])
  }
  save.sort((a,b)=>a[0]-b[0])
  
  const possible=[]
  const endtime=[0]
  let room=0
  for(let i=0;i<N;i++){
    const [start,end,num]=save[i]
    while(endtime.length>1){
      if (endtime[1][0]<=start) {
        const [,num]=heappop(endtime)
        possible.push(num)
      } else break
    }
    if (possible.length>0){
      const empty=possible.shift()
      heappush(endtime,[end,empty])
    } else {
      room+=1
      heappush(endtime,[end,room])
    }
  }

  console.log(room)
  process.exit()
})
