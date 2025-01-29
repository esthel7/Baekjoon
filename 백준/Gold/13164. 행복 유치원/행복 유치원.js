const readline = require('readline')
const rl=readline.createInterface({
  input:process.stdin,
  output:process.stdout
})

function swap(arr,a,b){
  [arr[a],arr[b]]=[arr[b],arr[a]]
}

function heappush(arr,item){
  arr.push(item)
  let idx=arr.length-1
  while (idx>1){
    const parent=Math.floor(idx/2)
    if (arr[parent]>arr[idx]){
      [arr[parent],arr[idx]]=[arr[idx],arr[parent]]
      idx=parent
    } else break
  }
}

function heappop(arr){
  const item=arr[1]
  arr[1]=arr.pop()
  let idx=1
  const last=arr.length
  while (idx<last){
    const left=idx*2
    const right=idx*2+1
    if (left>=last) break
    if (right>=last){
      if (arr[left]<arr[idx]) [arr[left],arr[idx]]=[arr[idx],arr[left]]
      break
    }
    let smaller=right
    if (arr[left]<=arr[right]){
      smaller=left
    }
    if (arr[smaller]<arr[idx]){
      [arr[smaller],arr[idx]]=[arr[idx],arr[smaller]]
      idx=smaller
    } else break
  }
  return item
}

const input=[]
let iter=0
rl.on('line',(line)=>{
  input.push(line)
}).on('close',()=>{
  const [N,K]=input[iter++].split(' ').map(item=>Number(item))
  const l=input[iter++].split(' ').map(item=>Number(item))
  let answer=0
  const q=[0]
  for(let i=1;i<N;i++){
    const diff=l[i]-l[i-1]
    answer+=diff
    heappush(q,-diff)
  }
  for(let i=0;i<K-1;i++){
    answer+=heappop(q)
  }
  console.log(answer)
  process.exit()
})
