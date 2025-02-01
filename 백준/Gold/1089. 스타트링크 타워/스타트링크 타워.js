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
  const l=[]
  for(let i=0;i<5;i++){
    l.push(input[iter++].split(''))
  }

  const light=[...new Array(5)].map(item=>[...new Array(3)].map(item=>[]))
  light[0][0]=[1]
  light[0][1]=[1,4]
  light[1][0]=[1,2,3,7]
  light[1][1]=[0,1,2,3,4,5,6,7,8,9]
  light[1][2]=[5,6]
  light[2][0]=[1,7]
  light[2][1]=[0,1,7]
  light[3][0]=[1,3,4,5,7,9]
  light[3][1]=[0,1,2,3,4,5,6,7,8,9]
  light[3][2]=[2]
  light[4][0]=[1,4,7]
  light[4][1]=[1,4,7]

  function checkNum(idx){
    const info={}
    for(let i=0;i<10;i++){
      info[i]=true
    }
    const no={}
    for(let i=0;i<5;i++){
      for(let j=idx;j<idx+3;j++){
        if (l[i][j]==='#'){
          if (light[i][j-idx].length===10) {
            console.log(-1)
            process.exit()
          }
          for(let k=0;k<10;k++){
            if (light[i][j-idx].includes(k)) {
              no[k]=true
              delete(info[k])
            }
          }
        } else {
          for(let k=0;k<light[i][j-idx].length;k++){
            if (light[i][j-idx][k] in no) continue
            info[light[i][j-idx][k]]=true
          }
        }
      }
    }
    if (Object.keys(info).length===0){
      console.log(-1)
      process.exit()
    }
    return Object.keys(info)
  }

  let answer=0
  for(let i=0;i<3*N+(N-1);i+=4){
    const plus=checkNum(i).map(item=>Number(item))
    let now=0
    const Len=plus.length
    for(let i=0;i<Len;i++){
      now+=plus[i]
    }
    answer*=10
    answer+=now/Len
  }

  console.log(answer.toFixed(5))
  process.exit()
})

/*

9
###..#.......##..#.#.#...#.#...#.#.
#.##.......#...#...#.......#..#....
.###.......#.###.###.#.#.......#.#.
#.##...#......##.......#......##...
#..#..........##.#.#.#...#.#.##..##

*/
