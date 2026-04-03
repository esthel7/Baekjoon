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
  const T=Number(input[iter++])
  const answer=[]
  for(let _=0;_<T;_++){
    const N=Number(input[iter++])
    const [nx,ny]=input[iter++].split(' ').map(Number)
    const [mx,my]=input[iter++].split(' ').map(Number)

    if (nx===mx && ny===my) {
      answer.push(0)
      continue
    }

    const visited=[...new Array(N)].map(item=>[...new Array(N)].map(item=>false))
    visited[nx][ny]=true

    const xbox=[1,2,2,1,-1,-2,-2,-1]
    const ybox=[-2,-1,1,2,-2,-1,1,2]

    const q=[[nx,ny,0]]
    let finish=false
    while (q.length>0){
      const [nx,ny,cnt]=q.shift()
      for(let i=0;i<8;i++){
        const newx=nx+xbox[i]
        const newy=ny+ybox[i]
        if (0<=newx && newx<N && 0<=newy && newy<N){
          if (visited[newx][newy]) continue
          visited[newx][newy]=true
          if (newx===mx && newy===my){
            answer.push(cnt+1)
            finish=true
            break
          }
          q.push([newx,newy,cnt+1])
        }
      }
      if (finish) break
    }
  }

  console.log(answer.join('\n'))
  process.exit()
})
