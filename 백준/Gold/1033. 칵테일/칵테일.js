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
  const value=[...new Array(N)].map(item=>-1)
  const info=[...new Array(N)].map(item=>[])

  function change(p,q){
    if (p%q===0) return [p/q,1]
    if (q%p===0) return [1,q/p]
    let diff=Math.abs(p-q)
    while (diff!==1){
      if (p%diff===0 && q%diff===0){
        p/=diff
        q/=diff
      } else break
      diff=Math.abs(p-q)
    }
    return [p,q]
  }

  function multi(start,no,data){
    for(let i=0;i<info[start].length;i++){
      const node=info[start][i]
      if (node===no) continue
      value[node]*=data
      multi(node,start,data)
    }
  }

  function find(a,b){
    while(b>0){
      [a,b]=[b,a%b]
    }
    return a
  }

  for(let i=0;i<N-1;i++){
    let [a,b,p,q]=input[iter++].split(' ').map(item=>Number(item));
    [p,q]=change(p,q)
    if (value[a]===-1){
      if (value[b]===-1){
        value[a]=p
        value[b]=q
      } else {
        if (p*value[b]%q===0){
          value[a]=p*value[b]/q
        } else {
          value[a]=p*value[b]
          value[b]*=q
          multi(b,a,q)
        }
      }
    } else {
      if (value[b]===-1){
        if (q*value[a]%p===0){
          value[b]=q*value[a]/p
        } else {
          value[b]=q*value[a]
          value[a]*=p
          multi(a,b,p)
        }
      } else {
        if (value[a]/value[b]===p/q) continue
        const m=find(value[a],value[b])*value[a]*value[b]
        multi(a,b,p*m/value[a])
        multi(b,a,q*m/value[b])
        value[a]=p*m
        value[b]=q*m
      }
    }
    info[a].push(b)
    info[b].push(a)
  }

  let m=value[0]
  for(let i=1;i<N;i++){
    m=find(m,value[i])
  }

  for(let i=0;i<N;i++){
    value[i]/=m
  }

  console.log(value.join(' '))
  process.exit()
})
