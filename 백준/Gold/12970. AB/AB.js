const readline=require('readline')
const rl=readline.createInterface({
  input:process.stdin,
  output:process.stdout
})

// AB

const input=[]
let iter=0
rl.on('line',(line)=>{
  input.push(line)
}).on('close',()=>{
  const [N,K]=input[iter++].split(' ').map(item=>Number(item))

  let possible=0
  for(let i=0;i<=N/2;i++){
    possible=Math.max(possible,i*(N-i))
  }
  if (possible<K){
    console.log(-1)
    process.exit()
  }

  const l=[...new Array(N)].map(item=>'B')
  let cntA=0
  while(true){
    let flag=false
    for(let i=N-1;i>=0;i--){
      if (l[i]==='A') {
        l[i+1]='A'
        cntA+=1
        break
      }
      if (cntA*(N-cntA-1)+N-i-1===K){
        l[i]='A'
        flag=true
        break
      }
      if (i===0) {
        l[i]='A'
        cntA+=1
        if (cntA*(N-cntA)===K) flag=true
        break
      }
    }
    if (flag) break
  }
  console.log(l.join(''))
  process.exit()
})
