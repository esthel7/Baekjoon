const readline=require('readline')
const rl=readline.createInterface({
  input:process.stdin,
  output:process.stdout
})

function isSmaller(a,b){
  if (a[0]<b[0]) return true
  return false
}

function heappush(q,item){
  q.push(item)
  let loc=q.length-1
  while (loc>1){
    const parent=Math.floor(loc/2)
    if (isSmaller(q[loc],q[parent])){
      [q[loc],q[parent]]=[q[parent],q[loc]]
      loc=parent
    } else break
  }
}

function heappop(q){
  const value=q[1]
  if (q.length===2){
    q.pop()
    return value
  }
  q.splice(1,1,q.pop())
  let loc=1
  const last=q.length
  while (loc<last){
    const left=loc*2
    const right=loc*2+1
    if (left>=last) break
    else if (right>=last){
      if (!isSmaller(q[loc],q[left])){
        [q[loc],q[left]]=[q[left],q[loc]]
      }
      break
    }
    const Min=isSmaller(q[left],q[right])?left:right
    if (isSmaller(q[Min],q[loc])){
      [q[loc],q[Min]]=[q[Min],q[loc]]
      loc=Min
    } else break
  }
  return value
}

const input=[]
let iter=0
rl.on('line',(line)=>{
  input.push(line)
}).on('close',()=>{
  const [N,M]=input[iter++].split(' ').map(item=>Number(item))
  const l=[]
  for(let i=0;i<N;i++){
    l.push(input[iter++].split(' ').map(item=>Number(item)))
  }

  let land=0
  const visit=[...new Array(N)].map(item=>[...new Array(M)].map(item=>false))
  const dir=[...new Array(N)].map(item=>[...new Array(M)].map(item=>[...new Array(4)].map(item=>true)))
  const xbox=[-1,1,0,0]
  const ybox=[0,0,-1,1]
  const info={}
  for(let i=0;i<N;i++){
    for(let j=0;j<M;j++){
      if (visit[i][j] || l[i][j]===0) continue
      land+=1
      l[i][j]=land
      info[land]=[]
      const have=[[i,j]]
      while (have.length!==0){
        const [x,y]=have.pop()
        info[land].push([x,y])
        for(let k=0;k<4;k++){
          const newX=x+xbox[k]
          const newY=y+ybox[k]
          if (0<=newX&&newX<N&&0<=newY&&newY<M){
            if (l[newX][newY]===1||l[newX][newY]===land){
              dir[x][y][k]=false
            }
            if (!visit[newX][newY]&&l[newX][newY]===1){
              l[newX][newY]=land
              visit[newX][newY]=true
              have.push([newX,newY])
            }
          } else {
            dir[x][y][k]=false
          }
        }
      }
    }
  }

  const left={}
  const bridge={}
  for(let i=1;i<=land;i++){
    left[String(i)]=true
    bridge[String(i)]={}
  }

  for(let i=1;i<=land;i++){
    for(let j=0;j<info[i].length;j++){
      const [x,y]=info[i][j]
      for(let d=0;d<4;d++){
        if (!dir[x][y][d]) continue
        if (d===0){ // top
          for(let move=1;move<N;move++){
            if (x-move<0) break
            if (l[x-move][y]!==0){
              const end=l[x-move][y]
              if (move<=2||end<=i) break
              if (String(end) in bridge[String(i)] && bridge[String(i)][String(end)]<move-1) continue
              bridge[String(i)][String(end)]=move-1
              if (String(i) in left) delete(left[String(i)])
              if (String(end) in left) delete(left[String(end)])
              break
            }
          }
        } else if (d===1){ // bottom
          for(let move=1;move<N;move++){
            if (x+move>=N) break
            if (l[x+move][y]!==0){
              const end=l[x+move][y]
              if (move<=2||end<=i) break
              if (String(end) in bridge[String(i)] && bridge[String(i)][String(end)]<move-1) continue
              bridge[String(i)][String(end)]=move-1
              if (String(i) in left) delete(left[String(i)])
              if (String(end) in left) delete(left[String(end)])
              break
            }
          }
        } else if (d===2){ // left
          for(let move=1;move<M;move++){
            if (y-move<0) break
            if (l[x][y-move]!==0){
              const end=l[x][y-move]
              if (move<=2||end<=i) break
              if (String(end) in bridge[String(i)] && bridge[String(i)][String(end)]<move-1) continue
              bridge[String(i)][String(end)]=move-1
              if (String(i) in left) delete(left[String(i)])
              if (String(end) in left) delete(left[String(end)])
              break
            }
          }
        } else { // right
          for(let move=1;move<M;move++){
            if (y+move>=M) break
            if (l[x][y+move]!==0){
              const end=l[x][y+move]
              if (move<=2||end<=i) break
              if (String(end) in bridge[String(i)] && bridge[String(i)][String(end)]<move-1) continue
              bridge[String(i)][String(end)]=move-1
              if (String(i) in left) delete(left[String(i)])
              if (String(end) in left) delete(left[String(end)])
              break
            }
          }
        }
      }
    }
  }

  if (Object.keys(left).length>0){
    console.log(-1)
    process.exit()
  }

  const q=[[]]
  for(let i=1;i<=land;i++){
    const keys=Object.keys(bridge[i])
    for(let j=0;j<keys.length;j++){
      heappush(q,[bridge[String(i)][keys[j]],i,Number(keys[j])])
    }
  }

  let answer=0
  const root=[...new Array(land+1)].map(item=>0)
  while (q.length>1){
    const [len,start,end]=heappop(q)
    // console.log(len,start,end,answer)
    if (root[start]===0){
      if (root[end]===0){
        root[start]=start
        root[end]=start
        answer+=len
      } else {
        root[start]=root[end]
        answer+=len
      }
    } else {
      if (root[end]===0){
        root[end]=root[start]
        answer+=len
      } else {
        if (root[start]===root[end]) continue
        const Min=root[end]<root[start]?root[end]:root[start]
        const Max=root[end]>root[start]?root[end]:root[start]
        answer+=len
        for(let i=1;i<=land;i++){
          if (root[i]===Max) root[i]=Min
        }
      }
    }
  }

  const first=root[1]
  for(let i=2;i<=land;i++){
    if (root[i]!==first){
      console.log(-1)
      process.exit()
    }
  }

  console.log(answer)
  process.exit()
})
