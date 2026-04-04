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
  const l=input[iter++].split(' ').map(Number)
  const answer=[...new Array(N)].map(item=>0)

  for(let i=1;i<N;i++){
    let Max=0
    for(let j=0;j<i;j++){
      if (l[i]>l[j]){
        Max=Math.max(answer[j]+1,Max)
      }
    }
    answer[i]=Max
  }
  console.log(Math.max(...answer)+1)
  process.exit()
})
