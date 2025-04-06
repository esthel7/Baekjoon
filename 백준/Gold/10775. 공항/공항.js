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
  const G=Number(input[iter++])
  const P=Number(input[iter++])
  const l=[]
  for(let i=0;i<P;i++){
    l.push(Number(input[iter++]))
  }
  
  let answer=0
  const loc=[...new Array(G+1)].map((item,idx)=>item=idx)
  function find(idx,go){
    if (loc[idx]===0||idx===0) return 0
    if (loc[idx]===idx) {
      for(let i=0;i<go.length;i++){
        loc[go[i]]=loc[idx-1]
      }
      loc[idx]=loc[idx-1]
      return idx
    } else {
      go.push(idx)
      return find(loc[idx],go)
    }
  }
  for(let i=0;i<P;i++){
    const now=l[i]
    const park=find(now,[])
    if (park===0){
      break
    }
    answer+=1
    // console.log(loc,answer)
  }

  console.log(answer)
  process.exit()
})
