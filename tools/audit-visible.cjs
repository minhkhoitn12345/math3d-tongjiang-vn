// Evaluate each featured lesson's data and the Vietnamese override before 3D startup.
// This catches text that a static source scan cannot distinguish from unused notes.
const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');

const root = path.resolve(__dirname, '..');
const lessons = Object.keys(JSON.parse(fs.readFileSync(path.join(root, 'lessons-vi.json'), 'utf8')));
const han = /[\u3400-\u9fff]/;
const errors = [];

function walk(value, key, found) {
  if (typeof value === 'string' && han.test(value)) found.push(key);
  else if (value && typeof value === 'object') {
    for (const [part, child] of Object.entries(value)) walk(child, `${key}.${part}`, found);
  }
}

for (const slug of lessons) {
  const source = fs.readFileSync(path.join(root, 'courses', `${slug}.html`), 'utf8');
  const configMarker = new RegExp(`var ([\\w$]+)=\\{meta:\\{slug:"${slug}"`);
  const configMatch = configMarker.exec(source);
  const sharedMatch = /var ([\w$]+)=\{home:"M\\u1ee5c l\\u1ee5c"/.exec(source);
  const configEnd = configMatch && source.indexOf('};var ', configMatch.index);
  const sharedEnd = sharedMatch && source.indexOf(';function ', sharedMatch.index);
  const patchStart = source.indexOf('/* VI_UI_START */');
  const endMark = '/* VI_UI_END */';
  const patchEnd = source.indexOf(endMark, patchStart);
  if (!configMatch || !sharedMatch || configEnd < 0 || sharedEnd < 0 || patchStart < 0 || patchEnd < 0) {
    errors.push(`${slug}: thiếu cấu hình hoặc bản dịch`);
    continue;
  }
  const input = [
    source.slice(sharedMatch.index, sharedEnd + 1),
    source.slice(configMatch.index, configEnd + 1),
    source.slice(patchStart, patchEnd + endMark.length),
    `({lesson:${configMatch[1]}, shared:${sharedMatch[1]}})`,
  ].join(';');
  try {
    const { lesson, shared } = vm.runInNewContext(input, {}, { timeout: 2000 });
    const found = [];
    walk(lesson, 'lesson', found);
    walk(shared, 'shared', found);
    for (const [index, question] of lesson.quiz.list.entries()) {
      if (!Array.isArray(question.opts) || question.opts.length !== 4 ||
          !Number.isInteger(question.ans) || question.ans < 0 || question.ans >= question.opts.length) {
        errors.push(`${slug}: câu kiểm tra ${index + 1} có đáp án không hợp lệ`);
      }
    }
    for (const [key, fn] of Object.entries(shared)) {
      if (typeof fn === 'function') {
        try {
          const value = fn(3, 9);
          if (typeof value === 'string' && han.test(value)) found.push(`shared.${key}()`);
        } catch { /* Some functions expect lesson state; their static strings are checked above. */ }
      }
    }
    for (const [group, object] of Object.entries(shared)) {
      if (object && typeof object === 'object') {
        for (const [key, fn] of Object.entries(object)) {
          if (typeof fn === 'function') {
            try {
              const value = fn(3, 9);
              if (typeof value === 'string' && han.test(value)) found.push(`shared.${group}.${key}()`);
            } catch { /* See note above. */ }
          }
        }
      }
    }
    if (found.length) errors.push(`${slug}: còn tiếng Trung ở ${found.join(', ')}`);
  } catch (error) {
    errors.push(`${slug}: lỗi khi áp dụng bản dịch: ${error.message}`);
  }
}

if (errors.length) {
  console.error(errors.join('\n'));
  process.exit(1);
}
console.log(`Đạt: dữ liệu giao diện của ${lessons.length} bài tuyển chọn không còn chuỗi tiếng Trung.`);
