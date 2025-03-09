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
  const [A,B,C]=input[iter++].split(' ').map(item=>Number(item))
  if ((A+B+C)%3!==0){
    console.log(0)
    process.exit()
  }
  if (A===B&&B===C){
    console.log(1)
    process.exit()
  }

  let l=[A,B,C]
  l.sort((a,b)=>a-b)
  
  const info={[`${l[0]}-${l[1]}-${l[2]}`]:true}
  const q=[[...l]]

  while (q.length>0){
    const [a,b,c]=q.pop()
    l=[a+a,b,c-a]
    l.sort((a,b)=>a-b)
    if (l[0]===l[1]&&l[1]===l[2]){
      console.log(1)
      process.exit()
    }
    const value=`${l[0]}-${l[1]}-${l[2]}`
    if (!(value in info)) {
      info[value]=true
      q.push([...l])
    }

    if (a!==b){
      l=[a+a,b-a,c]
      l.sort((a,b)=>a-b)
      if (l[0]===l[1]&&l[1]===l[2]){
        console.log(1)
        process.exit()
      }
      const value=`${l[0]}-${l[1]}-${l[2]}`
      if (!(value in info)) {
        info[value]=true
        q.push([...l])
      }
    }

    if (b!==c){
      l=[a,b+b,c-b]
      l.sort((a,b)=>a-b)
      if (l[0]===l[1]&&l[1]===l[2]){
        console.log(1)
        process.exit()
      }
      const value=`${l[0]}-${l[1]}-${l[2]}`
      if (!(value in info)) {
        info[value]=true
        q.push([...l])
      }
    }
  }
  console.log(0)
  process.exit()
})
