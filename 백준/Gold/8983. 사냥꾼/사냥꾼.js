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
  const shot=input[iter++].split(' ').map(item=>Number(item)).sort((a,b)=>a-b)
  const loc={}
  for(let i=0;i<N;i++){
    const [x,y]=input[iter++].split(' ').map(item=>Number(item))
    if (x in loc) loc[x].push(y)
    else loc[x]=[y]
  }

  let answer=0
  const keys=Object.keys(loc).map(item=>Number(item))
  for(let i=0;i<keys.length;i++){
    const spot=keys[i]
    loc[spot].sort((a,b)=>a-b)
    if(loc[spot][0]>L) continue

    let start=0
    let end=M-1
    let possibleY=-1
    while(start<=end){
      const mid=Math.floor((start+end)/2)
      if (shot[mid]===spot){
        possibleY=L
        break
      } else if (shot[mid]>spot){
        if (spot+L>=shot[mid]) possibleY=possibleY>L-(shot[mid]-spot)?possibleY:L-(shot[mid]-spot)
        end=mid-1
      } else {
        if (spot-L<=shot[mid]) possibleY=possibleY>L-(spot-shot[mid])?possibleY:L-(spot-shot[mid])
        start=mid+1
      }
    }
    if (possibleY===-1||loc[spot][0]>possibleY) continue

    start=0
    end=loc[spot].length-1
    let plus=0
    while(start<=end){
      const mid=Math.floor((start+end)/2)
      if (loc[spot][mid]===possibleY){
        plus=mid+1
        break
      } else if (loc[spot][mid]>possibleY) end=mid-1
      else {
        plus=mid+1
        start=mid+1
      }
    }
    answer+=plus
  }

  console.log(answer)
  process.exit()
})
