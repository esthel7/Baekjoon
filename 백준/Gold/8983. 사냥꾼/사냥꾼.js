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
  const [M,N,L]=input[iter++].split(' ').map(item=>Number(item))
  const shot=input[iter++].split(' ').map(item=>Number(item))
  const loc={}
  for(let i=0;i<N;i++){
    const [x,y]=input[iter++].split(' ').map(item=>Number(item))
    if (x in loc) loc[x].push(y)
    else loc[x]=[y]
  }

  const keys=Object.keys(loc)
  for(let i=0;i<keys.length;i++){
    loc[keys[i]].sort((a,b)=>a-b)
  }

  let answer=0
  for(let i=0;i<M;i++){
    const spot=shot[i]
    const start=spot-L<=0?1:spot-L
    const end=spot+L>=1000000000?1000000000:spot+L+1
    let possibleY=L-(Math.abs(start-spot))
    for(let j=start;j<end;j++){
      if (j in loc){
        while (loc[j].length>0){
          if (loc[j][0]<=possibleY){
            answer+=1
            loc[j].shift()
          } else break
        }
      }
      if (j>=spot) possibleY-=1
      else possibleY+=1
    }
  }

  console.log(answer)
  process.exit()
})
