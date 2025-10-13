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
  const N=Number(input[iter++])
  const C=input[iter++].split(' ').map(item=>Number(item))
  const room=[]
  for(let i=0;i<N;i++){
    room.push([C[i],i])
  }
  room.sort((a,b)=>b[0]-a[0])
  
  const exist=[]
  let answer=0
  let move=0
  while(move<N){
    const [len,idx]=room[move++]
    if (len===0) break
    exist.push(idx)
    answer+=len
  }
  exist.sort((a,b)=>a-b)

  if (exist.length<=1){
    console.log(answer+Math.floor(N/2))
    process.exit()
  }

  // 겹치지 않게 사이에 추가하기
  for(let i=1;i<exist.length;i++){
    const first=exist[i-1]
    const second=exist[i]
    answer+=Math.ceil((second-first-1)/2)
  }
  answer+=Math.floor((exist[0]+N-exist[exist.length-1])/2)

  console.log(answer)
  process.exit()
})

// 연결된 방 또는 쪽방에 아무도 없어야함
// 1번에 들어있나 없나로 구분
