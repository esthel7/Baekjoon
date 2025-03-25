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
  const T=Number(input[iter++])
  const answer=[]
  for(let test=1;test<=T;test++){
    answer.push(`Scenario ${test}:`)
    const n=Number(input[iter++])
    const k=Number(input[iter++])

    const root=[...new Array(n)].map(item=>-1)
    const info={}

    function update(value,idx){
      if (value in info) info[value].push(idx)
      else info[value]=[idx]
    }

    for(let i=0;i<k;i++){
      const [a,b]=input[iter++].split(' ').map(item=>Number(item))
      if (root[a]===-1){
        if (root[b]===-1){
          const Min=Math.min(a,b)
          root[a]=Min
          root[b]=Min
          update(Min,a)
          update(Min,b)
        } else {
          root[a]=root[b]
          update(root[b],a)
        }
      } else {
        if (root[b]===-1){
          root[b]=root[a]
          update(root[a],b)
        } else {
          if (root[a]===root[b]) continue
          const Min=Math.min(root[a],root[b])
          const Max=Math.max(root[a],root[b])
          for(let j=0;j<info[Max].length;j++){
            root[info[Max][j]]=Min
            update(Min,info[Max][j])
          }
          delete(info[Max])
        }
      }
    }

    const m=Number(input[iter++])
    for(let i=0;i<m;i++){
      const [u,v]=input[iter++].split(' ').map(item=>Number(item))
      if (u===v){
        answer.push(1)
        continue
      }
      if (root[u]===-1) answer.push(0)
      else{
        if (root[u]===root[v]) answer.push(1)
        else answer.push(0)
      }
    }

    answer.push('')
  }

  console.log(answer.join('\n'))
  process.exit()
})
