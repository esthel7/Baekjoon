const readline = require('readline');
const rl = readline.createInterface({ input: process.stdin, output: process.stdout });

const input = [];
let iter = 0;
rl.on('line', (line) => input.push(line)).on('close', () => {
  const [N, M] = input[iter++].split(' ').map(Number);

  // 2번째 줄이 없을 수도 있으니 안전하게 처리
  const originLine = (input[iter++] || '').trim();
  const arr = originLine === '' ? [] : originLine.split(/\s+/).map(Number);

  const empty = {};
  arr.forEach(d => { empty[d] = true; });

  const maxCoupon = N + 5;           // 쿠폰 인덱스 여유분
  const daysLen = N + 6;             // day+5 접근까지 안전
  const l = Array.from({ length: daysLen }, () => Array(maxCoupon).fill(-1));
  l[0][0] = 0;

  function possible(day, cp, cost) {
    if (day < 0 || day >= daysLen) return false;
    if (cp < 0 || cp >= maxCoupon) return false;
    return l[day][cp] === -1 || l[day][cp] > cost;
  }

  for (let day = 0; day < N; day++) {
    for (let cp = 0; cp < maxCoupon; cp++) {
      const cost = l[day][cp];
      if (cost === -1) continue; // ❌ break 아님

      // 다음날을 안 가는 날(빈 날)이면 비용 안 들고 다음날로 이동만 가능
      if (empty[day + 1]) {
        if (possible(day + 1, cp, cost)) l[day + 1][cp] = cost;
        continue;
      }

      // 쿠폰 3장 사용 (다음날 하루 무료)
      if (cp >= 3 && possible(day + 1, cp - 3, cost)) l[day + 1][cp - 3] = cost;

      // 1일권
      if (possible(day + 1, cp, cost + 10000)) l[day + 1][cp] = cost + 10000;

      // 3일권 (쿠폰+1)
      if (day + 3 <= N && (cp + 1) < maxCoupon && possible(day + 3, cp + 1, cost + 25000))
        l[day + 3][cp + 1] = cost + 25000;

      // 5일권 (쿠폰+2)
      if (day + 5 <= N && (cp + 2) < maxCoupon && possible(day + 5, cp + 2, cost + 37000))
        l[day + 5][cp + 2] = cost + 37000;
    }
  }

  let answer = Infinity;
  for (let i = 0; i < maxCoupon; i++) {
    if (l[N][i] !== -1) answer = Math.min(answer, l[N][i]);
  }

  console.log(answer === Infinity ? 0 : answer);
  process.exit();
});