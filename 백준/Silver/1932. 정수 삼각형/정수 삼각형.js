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
  const n=Number(input[iter++])
  const l=[]
  for(let i=0;i<n;i++){
    l.push(input[iter++].split(' ').map(Number))
  }
  const first=[...l].map(item=>[...item])

  for(let i=0;i<n-1;i++){
    for(let j=0;j<l[i].length;j++){
      l[i+1][j]=Math.max(l[i+1][j],first[i+1][j]+l[i][j])
      l[i+1][j+1]=Math.max(l[i+1][j+1],first[i+1][j+1]+l[i][j])
    }
  }

  console.log(Math.max(...l[n-1]))
  process.exit()
})
