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
  const [D,N]=input[iter++].split(' ').map(item=>Number(item))
  const oven=input[iter++].split(' ').map(item=>Number(item))
  const pizza=input[iter++].split(' ').map(item=>Number(item))

  for(let i=1;i<D;i++){
    if (oven[i-1]<oven[i]) oven[i]=oven[i-1]
  }
  
  let last=D-1
  for(let i=0;i<N;i++){
    const now=pizza[i]
    if (now>oven[0] || last<0){
      console.log(0)
      process.exit()
    }
    if (now<=oven[last]){
      last-=1
      continue
    }
    let left=0
    let right=last
    while(left<=right){
      const mid=Math.floor((left+right)/2)
      if (oven[mid]===now){
        if (oven[mid+1]<now) {
          last=mid-1
          break
        }
        left=mid+1
      } else if (oven[mid]>now){
        if (oven[mid+1]<now) {
          last=mid-1
          break
        }
        left=mid+1
      } else { // oven[mid]<now
        right=mid-1
      }
    }
  }
  console.log(last+2)
  process.exit()
})
