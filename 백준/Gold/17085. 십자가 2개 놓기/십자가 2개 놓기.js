const readline=require('readline')
const rl=readline.createInterface({
  input:process.stdin,
  output:process.stdout
})

// 십자가 2개놓기

const input=[]
let iter=0

rl.on('line',(line)=>{
  input.push(line)
}).on('close',()=>{
  const [N,M]=input[iter++].split(' ').map(item=>Number(item))
  const l=[]
  for(let i=0;i<N;i++){
    const now=[...input[iter++].split('')]
    l.push(now)
  }

  function find(x,y){
    for(let i=0;i<N;i++){
      if (i+x>=N) break
      if (l[x+i][y]!=='#') break
      const now=[]
      for(let j=0;j<=i;j++){
        now.push([x+j,y])
      }
      let flag=true
      if (i%2!==0) continue
      const half=i/2
      for(let j=1;j<=half;j++){
        if (y-j<0) {
          flag=false
          break
        }
        if (l[x+half][y-j]!=='#'){
          flag=false
          break
        }
        now.push([x+half,y-j])
      }
      if (!flag)continue
      for(let j=1;j<=half;j++){
        if (y+j>=M) {
          flag=false
          break
        }
        if (l[x+half][y+j]!=='#'){
          flag=false
          break
        }
        now.push([x+half,y+j])
      }
      if (!flag) continue
      const Len=now.length
      if (Len in info) info[Len].push(now)
      else info[Len]=[now]
    }
  }

  let answer=1
  const info={}
  for(let i=0;i<N;i++){
    for(let j=0;j<M;j++){
      if (l[i][j]==='#') find(i,j)
    }
  }

  function diff(a,b){
    const visit=[...new Array(N)].map(item=>[...new Array(M)].map(item=>false))
    for(let i=0;i<a.length;i++){
      visit[a[i][0]][a[i][1]]=true
    }
    for(let i=0;i<b.length;i++){
      if (visit[b[i][0]][b[i][1]]) return false
    }
    return true
  }

  const keys=Object.keys(info).map(item=>Number(item)).sort((a,b)=>b-a)
  for(let i=0;i<keys.length;i++){
    for(let j=0;j<info[keys[i]].length;j++){
      for(let k=i;k<keys.length;k++){
        if (answer>keys[i]*keys[k]) break
        for(let w=0;w<info[keys[k]].length;w++){
          if (i===k && j===w) continue
          if (diff(info[keys[i]][j],info[keys[k]][w])){
            if (answer<keys[i]*keys[k]) answer=keys[i]*keys[k]
            break
          }
        }
      }
    }
  }
  console.log(answer)

  process.exit()
})
