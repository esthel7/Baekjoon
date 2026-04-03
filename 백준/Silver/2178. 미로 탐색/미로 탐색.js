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
  const [N,M]=input[iter++].split(' ').map(Number)
  const l=[]
  for(let i=0;i<N;i++){
    l.push(input[iter++].split('').map(Number))
  }

  const arr=[]
  const maxValue=N*M
  for(let i=0;i<N;i++){
    arr.push([...new Array(M)].map(()=>maxValue))
  }
  
  const xbox=[0,0,-1,1]
  const ybox=[-1,1,0,0]

  arr[0][0]=1
  const q=[[0,0]]
  while(q.length>0){
    const [x,y]=q.shift()
    if (x===N-1 && y===M-1) {
      console.log(arr[x][y])
      process.exit()
    }
    const now=arr[x][y]
    for(let i=0;i<4;i++){
      const newx=x+xbox[i]
      const newy=y+ybox[i]
      if (0<=newx && newx<N && 0<=newy && newy<M && l[newx][newy]!==0){
        if (arr[newx][newy]===maxValue) {
          arr[newx][newy]=now+1
          q.push([newx,newy])
        }
      }
    }
  }

  process.exit()
})
