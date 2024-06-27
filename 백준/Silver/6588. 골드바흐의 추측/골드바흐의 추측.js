const input = require('fs')
  .readFileSync('/dev/stdin')
  .toString()
  .trim()
  .split('\n')
  .map(Number);

const primeNums = [];
const nums = Array(1_000_000 + 1).fill(true);
nums[0] = false;
nums[1] = false;

for (let i = 2; i <= Math.sqrt(1_000_000); i++) {
  if (!nums[i]) {
    continue;
  }
  primeNums.push(i);
  for (let j = i * 2; j <= 1_000_000; j += i) {
    nums[j] = false;
  }
}

console.log(
  input.slice(0, -1).map(num => {
    const low = primeNums.find(primeNum => nums[num - primeNum]);
    if (low) {
      const high = num - low;
      return `${num} = ${low} + ${high}`;
    }
    return "Goldbach's conjecture is wrong.";
  }).join('\n')
);