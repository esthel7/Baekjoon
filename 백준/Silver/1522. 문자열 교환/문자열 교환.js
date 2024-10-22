const readline = require('readline');
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let input = [];
rl.on('line', (line) => {
  input.push(line);
}).on('close', () => {
  let word = [...input.pop()];
  const Word = word.length;
  const first = word[0];
  let window = 0;
  for (let i = 0; i < Word; i++) {
    if (word[i] === first) window += 1;
  }

  word = word.concat(word);
  let answer = Word;
  for (let i = 0; i < Word; i++) {
    let now = 0;
    for (let j = 0; j < window; j++) {
      if (word[i + j] !== first) now += 1;
    }
    answer = Math.min(answer, now);
  }
  console.log(answer);
  process.exit();
});
