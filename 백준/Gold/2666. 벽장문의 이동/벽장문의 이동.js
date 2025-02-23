const readline=require('readline')
const rl=readline.createInterface({
  input:process.stdin,
  output:process.stdout
})

function heappush(q,item){
  q.push(item)
  let loc=q.length-1
  while (loc>1){
    const parent=Math.floor(loc/2)
    if (q[parent][0]>q[loc][0]){
      [q[parent],q[loc]]=[q[loc],q[parent]]
      loc=parent
    } else break
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
      if (q[loc][0]>q[left][0]) [q[left],q[loc]]=[q[loc],q[left]]
      break
    }
    const Min=q[left][0]>q[right][0]?right:left
    if (q[loc][0]>q[Min][0]) {
      [q[Min],q[loc]]=[q[loc],q[Min]]
      loc=Min
    }
    else break
  }
  return value
}

const input=[]
let iter=0
rl.on('line',(line)=>{
  input.push(line)
}).on('close',()=>{
  const N=Number(input[iter++])
  const [a,b]=input[iter++].split(' ').map(item=>Number(item))
  let q=[[0,a,b]]
  const Len=Number(input[iter++])
  for(let i=0;i<Len;i++){
    const open=Number(input[iter++])
    const newQ=[]
    while (q.length>0){
      const [cnt,a,b]=q.pop()
      if (a>b){
        let cnt=a
        a=b
        b=cnt
      }
      const left=Math.abs(a-open)
      const right=Math.abs(b-open)
      if (open<=a){
        newQ.push([cnt+left,open,b])
        continue
      }
      else if (open>=b){
        newQ.push([cnt+right,a,open])
        continue
      }
      newQ.push([cnt+left,open,b])
      newQ.push([cnt+right,a,open])
    }
    q=newQ
  }
  let answer=q[0][0]
  for(let i=1;i<q.length;i++){
    if (answer>q[i][0]) answer=q[i][0]
  }
  console.log(answer)
  process.exit()
})
