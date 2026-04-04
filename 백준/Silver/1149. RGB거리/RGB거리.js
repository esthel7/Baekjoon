const readline=require('readline')
const rl=readline.createInterface({
  input:process.stdin,
  output:process.stdout
})

function findMin(a,b,c){
  if (a<b){
    if (b<c) return [0,1,2]
    else {
      if (a<c) return [0,2,1]
      return [2,0,1]
    }
  }else { // a>b
    if (b>c) return [2,1,0]
    else { // b<c
      if (a<c) return [1,0,2]
      return [1,2,0]
    }
  }
}

const input=[]
let iter=0
rl.on('line',(line)=>{
  input.push(line)
}).on('close',()=>{
  const N=Number(input[iter++])
  const arr=[]
  for(let i=0;i<N;i++){
    arr.push(input[iter++].split(' ').map(Number))
  }
  const l=[...new Array(3)].map(item=>[...new Array(N)].map(item=>1000*1000))

  l[0][0]=arr[0][0]
  l[1][0]=arr[0][1]
  l[2][0]=arr[0][2]

  for(let i=1;i<N;i++){
    const [a,b,c]=findMin(l[0][i-1],l[1][i-1],l[2][i-1])
    l[b][i]=l[a][i-1]+arr[i][b]
    l[c][i]=l[a][i-1]+arr[i][c]
    l[a][i]=l[b][i-1]+arr[i][a]
  }
  console.log(Math.min(l[0][N-1],l[1][N-1],l[2][N-1]))
  process.exit()
})
