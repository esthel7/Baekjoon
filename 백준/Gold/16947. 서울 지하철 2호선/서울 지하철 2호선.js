const readline=require('readline')
const rl=readline.createInterface({
  input:process.stdin,
  output:process.stdout
})

// 16947

const input=[]
let iter=0
rl.on('line',(line)=>{
  input.push(line)
}).on('close',()=>{
  const N=Number(input[iter++])
  const info=[...new Array(N)].map(item=>{return{}})
  for(let i=0;i<N;i++){
    const [u,v]=input[iter++].split(' ').map(item=>Number(item))
    info[u-1][v-1]=true
    info[v-1][u-1]=true
  }

  function find(node){
    if (flag) return
    const keys=Object.keys(info[node]).map(item=>Number(item))
    for(let i=0;i<keys.length;i++){
      const now=keys[i]
      if (now===stop) {
        flag=true
        return
      }
      if (visit[now]) continue
      save.push(now)
      visit[now]=true
      delete(info[node][now])
      delete(info[now][node])
      find(now)
      info[node][now]=true
      info[now][node]=true
      visit[now]=false
      if (flag) return
      save.pop()
    }
  }

  let flag=false
  let stop=0
  const save=[]
  const visit=[...new Array(N)].map(item=>false)
  for(let i=0;i<N;i++){
    stop=i
    save.push(i)
    visit[i]=true
    find(i)
    visit[i]=false
    if (flag) break
    save.pop()
  }

  const q=[]
  const answer=[...new Array(N)].map(item=>-1)
  for(let i=0;i<save.length;i++){
    answer[save[i]]=0
    q.push([save[i],0])
  }

  while(q.length>0){
    const [node,cost]=q.shift()
    const keys=Object.keys(info[node]).map(item=>Number(item))
    for(let i=0;i<keys.length;i++){
      if (answer[keys[i]]===-1) {
        answer[keys[i]]=cost+1
        q.push([keys[i],cost+1])
      }
    }
  }

  console.log(answer.join(' '))
  process.exit()
})
