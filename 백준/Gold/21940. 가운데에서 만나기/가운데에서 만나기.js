const readline=require('readline')
const rl=readline.createInterface({
  input:process.stdin,
  output:process.stdout
})

const input=[]
let iter=0

// 가운데에서 만나기

rl.on('line',(line)=>{
  input.push(line)
}).on('close',()=>{
  const [N,M]=input[iter++].split(' ').map(item=>Number(item))

  const dir=[...new Array(N+1)].map(item=>[...new Array(N+1)].map(item=>-1))
  for(let i=1;i<=N;i++){
    dir[i][i]=0
  }
  for(let i=0;i<M;i++){
    const [a,b,c]=input[iter++].split(' ').map(item=>Number(item))
    dir[a][b]=c
  }

  for(let i=1;i<=N;i++){
    for(let a=1;a<=N;a++){
      for(let b=1;b<=N;b++){
        if (dir[a][i]===-1 || dir[i][b]===-1) continue
        if (dir[a][b]===-1 || dir[a][b]>dir[a][i]+dir[i][b]) dir[a][b]=dir[a][i]+dir[i][b]
      }
    }
  }

  let answer=[0,[]]
  const K=Number(input[iter++])
  const loc=input[iter++].split(' ').map(item=>Number(item))
  for(let i=1;i<=N;i++){
    let flag=true
    let Max=0
    for(let j=0;j<K;j++){
      const node=loc[j]
      if (dir[node][i]!==-1&&dir[i][node]!==-1){
        const value=dir[node][i]+dir[i][node]
        if (Max===0 || Max<value) Max=value
      }
      else {
        flag=false
        break
      }
    }
    if (!flag) continue
    if (answer[0]===0||answer[0]>Max) answer=[Max,[i]]
    else if (answer[0]===Max) answer[1].push(i)
  }
  console.log(answer[1].join(' '))
  process.exit()
})
