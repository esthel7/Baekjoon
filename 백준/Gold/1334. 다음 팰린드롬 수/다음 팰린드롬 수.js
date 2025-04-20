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
  const SN=input[iter++]
  const len=SN.length;
  const l=[...SN].map(item=>Number(item))

  function setOdd(half){
    for(let i=half-1;i>=0;i--){
      l[half+1+half-1-i]=l[i]
    }
  }

  function setEven(halfM1){
    for(let i=halfM1;i>=0;i--){
    l[halfM1+1+halfM1-i]=l[i]
    }
  }

  function printLast(){
    const answer=[1]
    for(let i=0;i<len-1;i++){
      answer.push(0)
    }
    answer.push(1)
    console.log(answer.join(''))
  }
  
  if (len%2===1){
    const half=Math.floor(len/2)
    let left=half-1
    let right=half+1
    while(left>=0){
      if (l[left]===l[right]){
        left-=1
        right+=1
      }
      else if (l[left]>l[right]){
        setOdd(half)
        console.log(l.join(''))
        process.exit()
      } else break
    }

    if (l[half]!==9){
      l[half]+=1
      setOdd(half)
      console.log(l.join(''))
      process.exit()
    }

    for(let i=half-1;i>=0;i--){
      if (l[i]!==9){
        l[i]+=1
        for(let j=i+1;j<=half;j++){
          l[j]=0
        }
        setOdd(half)
        console.log(l.join(''))
        process.exit()
      }
    }
    printLast()
  } else {
    const halfM1=Math.floor(len/2)-1
    let left=halfM1
    let right=halfM1+1
    while(left>=0){
      if (l[left]===l[right]){
        left-=1
        right+=1
      }
      else if (l[left]>l[right]){
        setEven(halfM1)
        console.log(l.join(''))
        process.exit()
      } else break
    }

    if (l[halfM1]!==9){
      l[halfM1]+=1
      setEven(halfM1)
      console.log(l.join(''))
      process.exit()
    }

    for(let i=halfM1;i>=0;i--){
      if (l[i]!==9){
        l[i]+=1
        for(let j=i+1;j<=halfM1;j++){
          l[j]=0
        }
        setEven(halfM1)
        console.log(l.join(''))
        process.exit()
      }
    }
    printLast()
  }
  process.exit()
})
