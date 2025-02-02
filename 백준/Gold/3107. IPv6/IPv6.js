const readline=require('readline')
const rl=readline.createInterface({
  input:process.stdin,
  output:process.stdout
})

function change(text){
  switch (text.length){
    case 0:
      return '0000'
    case 1:
      return '000'+text
    case 2:
      return '00'+text
    case 3:
      return '0'+text
    default:
      return text
  }
}

const input=[]
let iter=0
rl.on('line',(line)=>{
  input.push(line)
}).on('close',()=>{
  const l=input[iter].split('::')
  const answer=[]
  if (l.length===1){
    const sep=input[iter].split(':')
    for(let i=0;i<8;i++){
      answer.push(change(sep[i]))
    }
  } else {
    const first=l[0].split(':')
    const second=l[1].split(':')
    const left=8-first.length-second.length
    for(let i=0;i<first.length;i++){
      answer.push(change(first[i]))
    }
    for(let i=0;i<left;i++){
      answer.push('0000')
    }
    for(let i=0;i<second.length;i++){
      answer.push(change(second[i]))
    }
  }

  console.log(answer.join(':'))
  process.exit()
})
