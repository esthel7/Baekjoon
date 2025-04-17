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
  const N=Number(input[iter++])
  if (N===1){
    console.log(0)
    process.exit()
  }
  if (N===2){
    console.log(1)
    process.exit()
  }

  const mod=1000000000
  const dp=[...new Array(N+1)].fill(0)
  dp[2]=1
  dp[3]=2
  for(let i=4;i<=N;i++){
    dp[i]=((dp[i-1]+dp[i-2])*(i-1))%mod // a와 선물 맞교환 or a 선물 받고 a는 다른 선물 픽
  }

  console.log(dp[N])
  process.exit()
})

// 1 2 3 4

// 2 1 4 3
// 2 3 4 1
// 2 4 1 3
// 3 1 4 2
// 3 4 1 2
// 3 4 2 1
// 4 1 2 3
// 4 3 1 2
// 4 3 2 1

// 12, 13, 14, 23, 24, 34
// 1234

// 1234   -
// 1243 -
// 1324 -
// 1342
// 1423
// 1432 -
// 2134 -
// 2143
// 2314
// 2341
// 2413
// 2431
// 3124
// 3142
// 3214 -
// 3241
// 3412
// 3421
// 4123
// 4132
// 4213
// 4231 -
// 4312
// 4321

// 12,13,14,23,24,34
// 1234

// total 24, minus 6+1
// 6
