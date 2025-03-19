const readline=require('readline')
const rl=readline.createInterface({
  input:process.stdin,
  output:process.stdout
})

const input=[]
let iter=0
rl.on('line',(line)=>{
  input.push(line)
}).on('close',()=>{
  const [N,M,K]=input[iter++].split(' ').map(item=>Number(item))
  const l=[]
  for(let i=0;i<N;i++){
    l.push([...input[iter++]])
  }

  const check=[...new Array(N)].map(item=>[...new Array(M)].map(item=>0))
  for(let i=0;i<N;i++){
    for(let j=0;j<M;j++){
      if (i%2===0 && j%2===0){
        if (l[i][j]==='B') check[i][j]=1
      } else if (i%2===0 && j%2!==0){
        if (l[i][j]==='W')  check[i][j]=1
      } else if (i%2!==0 && j%2===0){
        if (l[i][j]==='W') check[i][j]=1
      } else {
        if (l[i][j]==='B') check[i][j]=1
      }
    }
  }

  for(let i=0;i<N;i++){
    for(j=1;j<M;j++){
      check[i][j]+=check[i][j-1]
    }
  }
  for(let i=1;i<N;i++){
    for(j=0;j<M;j++){
      check[i][j]+=check[i-1][j]
    }
  }

  let answer=N*M
  for(let i=K-1;i<N;i++){
    for(let j=K-1;j<M;j++){
      let now=check[i][j]
      if (i===K-1){
        if (j!==K-1){
          now-=check[i][j-K]
        }
      } else {
        if (j===K-1){
          now-=check[i-K][j]
        } else {
          now-=check[i-K][j]+check[i][j-K]-check[i-K][j-K]
        }
      }
      const Min=now<K*K-now?now:K*K-now
      if (answer>Min) answer=Min
    }
  }

  console.log(answer)
  process.exit()
})
