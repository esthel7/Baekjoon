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
  const word=input[iter++].split('')
  const d=input[iter++].split('')
  const a=input[iter++].split('')

  function match(item){
    switch(item){
      case 'R':
        return 0
      case 'I':
        return 1
      case 'N':
        return 2
      case 'G':
        return 3
      case 'S':
        return 4
      default:
        console.log(0)
        process.exit()
    }
  }

  const len=d.length
  const dinfo=[...new Array(5)].map(item=>[])
  const ainfo=[...new Array(5)].map(item=>[])
  for(let i=0;i<len;i++){
    dinfo[match(d[i])].push(i)
    ainfo[match(a[i])].push(i)
  }

  const dp=[...new Array(word.length)].map(item=>[...new Array(2)].map(item=>[...new Array(len)].map(item=>0)))
  const first=match(word[0])
  for(let i=0;i<dinfo[first].length;i++){
    dp[0][0][dinfo[first][i]]=1
  }
  for(let i=0;i<ainfo[first].length;i++){
    dp[0][1][ainfo[first][i]]=1
  }
  for(let i=1;i<word.length;i++){
    const now=match(word[i])
    const dlen=dinfo[now].length
    if (dlen>0){
      let cnt=[...new Array(dlen)].map(item=>0)
      let idx=0
      for(let j=0;j<dinfo[now][dlen-1];j++){
        if (dp[i-1][1][j]>0) {
          for(let k=idx;k<dlen;k++){
            if (j<dinfo[now][k]) {
              cnt[k]+=dp[i-1][1][j]
              idx=k
              break
            }
          }
        }
      }
      for(let j=0;j<dlen;j++){
        if (j>0) cnt[j]+=cnt[j-1]
        dp[i][0][dinfo[now][j]]=cnt[j]
      }
    }

    const alen=ainfo[now].length
    if (alen===0) continue
    cnt=[...new Array(alen)].map(item=>0)
    idx=0
    for(let j=0;j<ainfo[now][alen-1];j++){
      if (dp[i-1][0][j]>0) {
        for(let k=idx;k<alen;k++){
          if (j<ainfo[now][k]) {
            cnt[k]+=dp[i-1][0][j]
            idx=k
            break
          }
        }
      }
    }
    for(let j=0;j<alen;j++){
      if (j>0) cnt[j]+=cnt[j-1]
      dp[i][1][ainfo[now][j]]=cnt[j]
    }
  }

  let answer=0
  for(let i=0;i<len;i++){
    answer+=dp[word.length-1][0][i]+dp[word.length-1][1][i]
  }
  console.log(answer)
  process.exit()
})
