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
  const f=[0,...input[iter++]]
  const s=[0,...input[iter++]]
  const t=[0,...input[iter++]]

  const l=[...new Array(f.length)].map(item=>[...new Array(s.length)].map(item=>[...new Array(t.length)].map(item=>0)))
  for(let i=1;i<f.length;i++){
    for(let  j=1;j<s.length;j++){
      for(let k=1;k<t.length;k++){
        if (f[i]===s[j] && s[j]===t[k]){
          l[i][j][k]=l[i-1][j-1][k-1]+1
        } else {
          l[i][j][k]=Math.max(l[i][j][k-1],l[i][j-1][k],l[i-1][j][k],l[i-1][j-1][k],l[i-1][j][k-1],l[i][j-1][k-1])
        }
      }
    }
  }
  console.log(l[f.length-1][s.length-1][t.length-1])
  process.exit()
})
