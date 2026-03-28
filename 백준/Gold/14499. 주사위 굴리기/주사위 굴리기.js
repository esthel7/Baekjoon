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
  const [N,M,x,y,K]=input[iter++].split(' ').map(Number)
  const loc=[]
  for(let i=0;i<N;i++){
    loc.push(input[iter++].split(' ').map(Number))
  }

  const mx=[0,0,-1,1]
  const my=[1,-1,0,0]

  const l=input[iter++].split(' ').map(item=>Number(item)-1)

  let dice=[...new Array(6)].map(item=>0)

  const answer=[]
  let nowx=x
  let nowy=y
  for(let i=0;i<K;i++){
    let newX=nowx+mx[l[i]]
    let newY=nowy+my[l[i]]
    if (0<=newX && newX<N && 0<=newY && newY<M){

      // dice 변경
      if (l[i]===0){
        dice=[dice[0],dice[2],dice[3],dice[5],dice[4],dice[1]]
      } else if (l[i]===1){
        dice=[dice[0],dice[5],dice[1],dice[2],dice[4],dice[3]]
      } else if (l[i]===2){
        dice=[dice[2],dice[1],dice[4],dice[3],dice[5],dice[0]]
      } else {
        dice=[dice[5],dice[1],dice[0],dice[3],dice[2],dice[4]]
      }

      if (loc[newX][newY]===0){
        loc[newX][newY]=dice[5]
      } else{
        dice[5]=loc[newX][newY]
        loc[newX][newY]=0
      }
      answer.push(dice[2])
      nowx=newX
      nowy=newY
    }
  }

  console.log(answer.join('\n'))
  process.exit()
})

// 0이면 바닥면 수가 칸에 복사
// 0이 아니면 칸 수가 바닥에 복사 & 칸은 0
// 바깥 이동은 무시 & 출력도 안하기
