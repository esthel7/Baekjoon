const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const input = [];
rl.on("line", (line) => {
  input.push(line);
}).on("close", () => {
  const [N, M] = input[0].split(" ").map(Number);
  const arr = input.slice(1, N + 1).map(Number);
  const queries = input.slice(N + 1).map((q) => q.split(" ").map(Number));

  const info = Array(4 * N).fill([Infinity, -Infinity]); // 세그먼트 트리 초기화

  // 세그먼트 트리 생성 함수
  function make(idx, start, end) {
    if (start === end) {
      info[idx] = [arr[start], arr[start]];
      return info[idx];
    }
    const mid = Math.floor((start + end) / 2);
    const left = make(idx * 2, start, mid);
    const right = make(idx * 2 + 1, mid + 1, end);
    info[idx] = [Math.min(left[0], right[0]), Math.max(left[1], right[1])]; // 부모 노드 갱신
    return info[idx];
  }

  make(1, 0, N - 1);

  // 구간 최소, 최대값을 찾는 함수
  function find(idx, start, end, left, right) {
    if (right < start || end < left) return [Infinity, -Infinity]; // 범위 밖
    if (left <= start && end <= right) return info[idx]; // 완전히 포함되는 경우

    const mid = Math.floor((start + end) / 2);
    const lQuery = find(idx * 2, start, mid, left, right);
    const rQuery = find(idx * 2 + 1, mid + 1, end, left, right);
    return [Math.min(lQuery[0], rQuery[0]), Math.max(lQuery[1], rQuery[1])];
  }

  const answer = [];
  for (const [a, b] of queries) {
    const [minVal, maxVal] = find(1, 0, N - 1, a - 1, b - 1);
    answer.push(`${minVal} ${maxVal}`);
  }

  console.log(answer.join("\n"));
});