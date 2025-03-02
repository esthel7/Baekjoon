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
  const N=Number(input[iter++])
  const r=0
  const rb=1
  const b=2

  const l=[]
  for(let i=0;i<N;i++){
    l.push(input[iter++].split(' ').map(item=>Number(item)))
  }

  const visit=[...new Array(N)].map(item=>[...new Array(N)].map(item=>[...new Array(3)].map(item=>0)))
  visit[0][1][r]=1
  for(let i=0;i<N;i++){
    for(let j=0;j<N;j++){
      if (i===0&&j===0) continue
      for(let k=0;k<3;k++){
        if (visit[i][j][k]===0) continue
        if (k===r){
          if (j+1<N && l[i][j+1]!==1) {
            visit[i][j+1][r]+=visit[i][j][r]
            if (i+1<N){
              if (l[i+1][j]!=1 && l[i+1][j+1]!==1) visit[i+1][j+1][rb]+=visit[i][j][r]            
            }
          }
        } else if (k===b){
          if (i+1<N && l[i+1][j]!==1){
            visit[i+1][j][b]+=visit[i][j][b]
            if (j+1<N){
              if (l[i][j+1]!=1 && l[i+1][j+1]!==1) visit[i+1][j+1][rb]+=visit[i][j][b]   
            }
          }
        } else { // rb
          if (j+1<N && l[i][j+1]!==1) visit[i][j+1][r]+=visit[i][j][rb]
          if (i+1<N && l[i+1][j]!==1) visit[i+1][j][b]+=visit[i][j][rb]
          if (i+1<N && j+1<N){
            if (l[i+1][j]!==1 && l[i+1][j+1]!==1 && l[i][j+1]!==1){
              visit[i+1][j+1][rb]+=visit[i][j][rb]
            }
          }
        }
      }
    }
  }
  console.log(visit[N-1][N-1][0]+visit[N-1][N-1][1]+visit[N-1][N-1][2])
  process.exit()
})
