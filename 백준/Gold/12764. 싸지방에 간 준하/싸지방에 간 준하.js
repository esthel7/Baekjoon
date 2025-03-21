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
  const last=q.length-1
  while(loc<last){
    const left=loc*2
    const right=loc*2+1
    if (left>last) break
    else if (right>last){
      if (isSmall(q[left],q[loc])){
        [q[left],q[loc]]=[q[loc],q[left]]
      }
      break
    } else {
      const Min=isSmall(q[left],q[right])?left:right
      if (isSmall(q[Min],q[loc])){
        [q[Min],q[loc]]=[q[loc],q[Min]]
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
  const N=Number(input[iter++])

  const last=1000002
  const l=[...new Array(last)].map(item=>[])
  for(let i=0;i<N;i++){
    const [p,q]=input[iter++].split(' ').map(item=>Number(item))
    l[p].push(q)
  }

  let cnt=0
  const answer=[] // 해당 번호 사용 수 
  const empty=[0] // 빈 번호 보관 (방번호, 0)
  const left=[0] // 언제 종료하는지 보관 (종료시간, 방번호)
  for(let i=0;i<last;i++){
    while(left.length>1){
      if (left[1][0]<i){
        const [endTime,idx]=heappop(left)
        heappush(empty,[idx,0])
      } else break
    }
    for(let j=0;j<l[i].length;j++){
      const end=l[i][j]
      let idx=-1
      if (empty.length===1){ // add new room
        idx=cnt
        answer.push(1)
        cnt+=1
      } else {
        [idx,tmp]=heappop(empty)
        answer[idx]+=1
      }
      heappush(left,[end,idx])
    }
  }

  console.log(cnt+'\n'+answer.join(' '))
  process.exit()
})
