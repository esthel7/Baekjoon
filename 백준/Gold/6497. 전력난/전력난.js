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
  const last=q.length-1
  while(loc<last){
    const left=loc*2
    const right=loc*2+1
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
  const answers=[]
  while(true){
    const [m,n]=input[iter++].split(' ').map(item=>Number(item))
    if (m===0 && n===0) break
    const q=[0]
    for(let i=0;i<n;i++){
      const [x,y,z]=input[iter++].split(' ').map(item=>Number(item))
      heappush(q,[z,x,y])
    }

    const root=[...new Array(m)].map(item=>-1)
    const info={}

    function update(value,idx){
      if (value in info) info[value].push(idx)
      else info[value]=[idx]
    }

    let answer=0
    while(q.length>1){
      const [z,x,y]=heappop(q)
      if (root[x]===-1){
        if (root[y]===-1){
          const Min=Math.min(x,y)
          root[x]=Min
          root[y]=Min
          update(Min,x)
          update(Min,y)
        } else {
          root[x]=root[y]
          update(root[y],x)
        }
      } else {
        if (root[y]===-1){
          root[y]=root[x]
          update(root[x],y)
        } else {
          if (root[x]===root[y]) answer+=z
          else {
            const Min=Math.min(root[x],root[y])
            const Max=Math.max(root[x],root[y])
            for(let i=0;i<info[Max].length;i++){
              root[info[Max][i]]=Min
              update(Min,info[Max][i])
            }
            delete(info[Max])
          }
        }
      }
    }
    answers.push(answer)
  }
  console.log(answers.join('\n'))
  process.exit()
})
