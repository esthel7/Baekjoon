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
  const [N,K]=input[iter++].split(' ').map(item=>Number(item))
  const info={}
  let answer=0
  for(let i=0;i<N;i++){
    const name=input[iter++].length
    if (name in info) {
      info[[name]].push(i)
      let left=0
      let right=info[[name]].length-2
      while (left<=right){
        let mid=Math.floor((left+right)/2)
        if (i-info[[name]][mid]<=K){
          if (mid===0) {
            answer+=info[[name]].length-1
            break
          }
          if (i-info[[name]][mid-1]>K){
            answer+=info[[name]].length-1-mid
            break
          } else right=mid-1
        } else {
          left=mid+1
        }
      }
    }
    else info[[name]]=[i]
  }
  console.log(answer)
  process.exit()
})
