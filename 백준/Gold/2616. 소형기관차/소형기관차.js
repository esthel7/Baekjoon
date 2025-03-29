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
  const N=Number(input[iter++])
  const l=input[iter++].split(' ').map(item=>Number(item))
  const M=Number(input[iter++])

  const cal=[...new Array(N)].map(item=>0)
  cal[0]=l[0]
  for(let i=1;i<N;i++){
    cal[i]+=cal[i-1]+l[i]
  }

  const dp=[...new Array(3)].map(item=>[...new Array(N+1)].map(item=>0))
  dp[0][M]=cal[M-1]
  for(let i=M+1;i<N;i++){
    dp[0][i]=Math.max(dp[0][i-1],cal[i-1]-cal[i-1-M])
  }
  for(let i=1;i<3;i++){
    for(let j=M;j<N;j++){
      if (j+M>N) break
      dp[i][j+M]=Math.max(dp[i][j+M-1],dp[i-1][j]+cal[j+M-1]-cal[j-1])
    }
  }

  console.log(dp[2][N])
  process.exit()
})
