const readline=require('readline');
const rl=readline.createInterface({
  input:process.stdin,
  output:process.stdout
})

const input=[]
let iter=0
rl.on('line',(line)=>{
  input.push(line)
}).on('close',()=>{
  const [N,M]=input[iter++].split(' ').map(item=>Number(item))
  const l=[]
  for(let i=0;i<N;i++){
    const value=Number(input[iter++])
    l.push(value)
  }

  const info=[-1]
  function make(idx,start,end){
    if (start===end){
      info[idx]=[l[start],l[start]]
      return info[idx]
    }
    const mid=Math.floor((start+end)/2)
    const left=make(idx*2,start,mid)
    const right=make(idx*2+1,mid+1,end)
    info[idx]=[Math.min(left[0], right[0]), Math.max(left[1], right[1])]
    return info[idx]
  }
  make(1,0,N-1)

  const answer=[]
  for(let i=0;i<M;i++){
    let [a,b]=input[iter++].split(' ').map(item=>Number(item))
    a-=1
    b-=1
    let Min=l[a]
    let Max=l[a]
    // console.log('start',a,b)
    function find(idx,left,right){
      // console.log('in find',left,right)
      if (a<=left&&right<=b){
        // console.log('update')
        Min=Min>info[idx][0]?info[idx][0]:Min
        Max=Max<info[idx][1]?info[idx][1]:Max
        return
      }
      const mid=Math.floor((left+right)/2)
      if (a<=mid&&left<=b) {
        find(idx * 2, left, mid);
      }
      if (mid<b&&a<=right) {
        find(idx * 2 + 1, mid + 1, right);
      }
    }
    find(1,0,N-1)
    answer.push(`${Min} ${Max}`)
  }

  console.log(answer.join('\n'))
  process.exit()
})
