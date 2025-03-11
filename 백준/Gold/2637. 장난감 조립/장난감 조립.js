const readline=require('readline');
const rl=readline.createInterface({
  input:process.stdin,
  output:process.stdout
})

const input=[]
let iter=0
rl.on('line',(line)=>{
  input.push(line)
}).on('close',()=>{
  const N=Number(input[iter++])
  const M=Number(input[iter++])

  const link=[...new Array(N+1)].map(item=>[])
  const basic=[...new Array(N+1)].map(item=>0)
  const items={}
  for(let i=0;i<M;i++){
    const [X,Y,K]=input[iter++].split(' ').map(item=>Number(item))
    if (X===N) items[Y]=K
    link[Y].push([X,K])
    basic[X]+=1
  }
  const first=[...basic]

  const leaf=[]
  for(let i=1;i<=N;i++){
    if (basic[i]===0) leaf.push(i)
  }

  const save=[...new Array(N+1)].map(item=>[...new Array(N+1)].map(item=>0))
  while(leaf.length>0){
    const item=leaf.shift()
    const keys=link[item]
    for(let i=0;i<keys.length;i++){
      const [node,cnt]=keys[i]
      basic[node]-=1
      if (basic[node]===0) leaf.push(node)
      if (first[item]===0) {
        save[node][item]+=cnt
      }
      else {
        for(let j=1;j<=N;j++){
          if (save[item][j]!==0) {
            save[node][j]+=save[item][j]*cnt
          }
        }
      }
    }
  }

  const print=[]
  for(let i=1;i<=N;i++){
    if (first[i]===0) print.push(`${i} ${save[N][i]}`)
  }
  console.log(print.join('\n'))
  process.exit()
})
