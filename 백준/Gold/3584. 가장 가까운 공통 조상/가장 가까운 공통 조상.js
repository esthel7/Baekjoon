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
  const answers=[]
  for(let _=0;_<T;_++){
    const N=Number(input[iter++])
    const parent=[...new Array(N+1)].map(item=>-1)
    const child=[...new Array(N+1)].map(item=>[])
    const depth=[...new Array(N+1)].map(item=>-1)
    for(let i=0;i<N-1;i++){
      const [A,B]=input[iter++].split(' ').map(item=>Number(item))
      parent[B]=A
      child[A].push(B)
    }

    const q=[]
    for(let i=1;i<=N;i++){
      if (parent[i]===-1){
        q.push([i,0])
        depth[i]=0
        break
      }
    }
    while(q.length>0){
      const [idx,d]=q.shift()
      for(let i=0;i<child[idx].length;i++){
        const node=child[idx][i]
        depth[node]=d+1
        q.push([node,d+1])
      }
    }

    let [A,B]=input[iter++].split(' ').map(item=>Number(item))
    while(A!==B){
      if (depth[A]<depth[B]) B=parent[B]
      else if (depth[A]>depth[B]) A=parent[A]
      else {
        A=parent[A]
        B=parent[B]
      }
    }
    answers.push(A)
  }
  console.log(answers.join('\n'))
  process.exit()
})
