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
  const order=[...input[iter++].split(' ')]

  function otherSide(a,b){
    if (a==='1'&&b==='3' || a==='3'&&b==='1' || a==='2'&&b==='4' || a==='4'&&b==='2') return true
    return false
  }

  function update(newBox,key,now){
    if (key in newBox){
      if (newBox[key]>now) return now
      return newBox[key]
    } else return now
  }

  function keyName(a,b){
    if (Number(a)>Number(b)) return `${b}-${a}`
    return `${a}-${b}`
  }

  let box={[`0-${order[0]}`]:2}
  for(let i=1;i<order.length-1;i++){
    const now=order[i]
    const newBox={}
    const keys=Object.keys(box)
    for(let j=0;j<keys.length;j++){
      const [left,right]=keys[j].split('-')
      const prev=box[keys[j]]
      if (left===now||right===now) {
        newBox[keys[j]]=update(newBox,keys[j],prev+1)
        continue
      }
      if (left==='0') {
        const newKey=keyName(now,right)
        newBox[newKey]=update(newBox,newKey,prev+2)
      }
      if (otherSide(left,now)){
        const newKey=keyName(right,now)
        newBox[newKey]=update(newBox,newKey,prev+4)
      } else {
        const newKey=keyName(right,now)
        newBox[newKey]=update(newBox,newKey,prev+3)
      }
      if (otherSide(right,now)){
        const newKey=keyName(left,now)
        newBox[newKey]=update(newBox,newKey,prev+4)
      } else {
        const newKey=keyName(left,now)
        newBox[newKey]=update(newBox,newKey,prev+3)
      }
    }
    box={...newBox}
  }

  let answer=-1
  const keys=Object.keys(box)
  for(let i=0;i<keys.length;i++){
    const now=box[keys[i]]
    if (answer===-1 || answer>now) answer=now
  }
  console.log(answer)
  process.exit()
})
