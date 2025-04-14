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
  const [a,b]=input[iter++].split(' ').map(item=>Number(item))
  if (a===b){
    console.log(a, a)
    process.exit()
  }
  const left=b/a
  // left 약수 구해서 가능한 두 수의 조합 중에서 합 작은거 

  function find(x,y){
    // 최대공약수가 1이면 true
    if (x===0){
      if (y===1) return true
      return false
    }
    return find(y%x,x)
  }
  
  let answer=[]
  let diff=-1
  for(let i=1;i<left**0.5;i++){
    if (left%i===0){
      const x=i
      const y=left/i
      if (find(x,y)){
        const value=a*x+a*y
        if (diff===-1 || diff>value){
          diff=value
          answer=[a*x,a*y]
        }
      }
    }
  }

  console.log(answer.join(' '))
  process.exit()
})
