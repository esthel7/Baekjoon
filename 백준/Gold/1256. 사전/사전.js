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
  const [N,M,K]=input[iter++].split(' ').map(item=>Number(item))
  const last=N+M-1

  const l=[]
  for(let i=0;i<N;i++){
    l.push(i)
  }
  let cnt=1

  // N-1 -> last
  // N-2 -> last-1

  while(true){
    if (cnt+last-l[N-1]+1<=K){ // 맨뒷자리 끝까지 이동 & 모양 변화
      cnt+=last-l[N-1]+1
      let flag=true
      for(let i=N-2;i>=0;i--){
        if (l[i]!==last-(N-1-i)){
          l[i]+=1
          let value=l[i]
          for(let j=i+1;j<N;j++){
            l[j]=value+1
            value+=1
          }
          flag=false
          break
        }
      }
      if (flag){
        console.log(-1)
        process.exit()
      }
    } else {
      for(let i=l[N-1]+1;i<=last;i++){
        if (cnt===K) break
        cnt+=1
        l[N-1]=i
      }
      break
    }
  }

  let answer=''
  for(let i=0;i<=last;i++){
    if (l.length>0 && l[0]===i){
      answer+='a'
      l.shift()
    }
    else answer+='z'
  }
  console.log(answer)
  process.exit()
})
