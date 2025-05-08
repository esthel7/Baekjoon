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
  // const A=[0,...input[iter++].split(' ').map(item=>Number(item))]
  const A=input[iter++].split(' ').map(item=>Number(item))
  const M=Number(input[iter++])
  // const B=[0,...input[iter++].split(' ').map(item=>Number(item))]
  const B=input[iter++].split(' ').map(item=>Number(item))

  const Ainfo={}
  for(let i=0;i<N;i++){
    if (A[i] in Ainfo) Ainfo[A[i]].push(i)
    else Ainfo[A[i]]=[i]
  }
  const Binfo={}
  for(let i=0;i<M;i++){
    if (B[i] in Binfo) Binfo[B[i]].push(i)
    else Binfo[B[i]]=[i]
  }

  const Akeys=Object.keys(Ainfo).map(item=>Number(item)).sort((a,b)=>b-a)
  const Bkeys=Object.keys(Binfo).map(item=>Number(item)).sort((a,b)=>b-a)
  let answer=[]
  let akeyidx=0
  let bkeyidx=0
  let aidx=-1
  let bidx=-1
  while(akeyidx!==Akeys.length && bkeyidx!==Bkeys.length){
    if (Akeys[akeyidx]!==Bkeys[bkeyidx]){
      if (Akeys[akeyidx]>Bkeys[bkeyidx]) akeyidx+=1
      else bkeyidx+=1
    } else {
      let nextAidx=-1
      let nextBidx=-1
      for(let i=0;i<Ainfo[Akeys[akeyidx]].length;i++){
        if (aidx>Ainfo[Akeys[akeyidx]][i]) continue
        else {
          nextAidx=i
          break
        }
      }
      for(let i=0;i<Binfo[Bkeys[bkeyidx]].length;i++){
        if (bidx>Binfo[Bkeys[bkeyidx]][i]) continue
        else {
          nextBidx=i
          break
        }
      }
      if (nextAidx!==-1 && nextBidx!==-1){
        const leftA=Ainfo[Akeys[akeyidx]].length-nextAidx
        const leftB=Binfo[Bkeys[bkeyidx]].length-nextBidx
        const Len=Math.min(leftA,leftB)
        for(let i=0;i<Len;i++){
          answer.push(Akeys[akeyidx])
        }
        aidx=Ainfo[Akeys[akeyidx]][nextAidx+Len-1]
        bidx=Binfo[Bkeys[bkeyidx]][nextBidx+Len-1]
      }
      akeyidx+=1
      bkeyidx+=1
    }
  }
  console.log(answer.length+'\n'+answer.join(' '))
  process.exit()
})
