const readline=require('readline')
const rl=readline.createInterface({
  input:process.stdin,
  output:process.stdout
})

// 두수의합? 

const input=[]
let iter=0
rl.on('line',(line)=>{
  input.push(line)
}).on('close',()=>{
  const t=Number(input[iter++])
  const answers=[]
  for(let _=0;_<t;_++){
    const [n,k]=input[iter++].split(' ').map(item=>Number(item))
    const l=input[iter++].split(' ').map(item=>Number(item))
    l.sort((a,b)=>a-b)

    let diff=[Math.abs(k-(l[0]+l[n-1])),0]
    let left=0
    let right=n-1
    while(left<right){
      const now=l[left]+l[right]
      const value=Math.abs(k-now)
      if (value===diff[0]){
        diff[1]+=1
      } else if (value<diff[0]){
        diff=[value,1]
      }
      if (k-now===0) {
        left+=1
        right-=1
      }
      else if (k-now>0) left+=1
      else right-=1
    }
    answers.push(diff[1])
  }
  console.log(answers.join('\n'))
  process.exit()
})

// -7, -4, -3, -2,  0, 1,  2,  5,  9, 12
// -7 12 -> 5 = 1
// -4 12 xxx
// -7 9 -> 2 = 2
