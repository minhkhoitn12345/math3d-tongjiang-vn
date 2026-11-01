const lessons = [
  { slug: 'projectile-step', title: 'Khám phá chuyển động ném ngang', subject: 'CHUYỂN ĐỘNG', kind: 'motion', code: '01', formula: 'x = v₀t · y = ½gt²', desc: 'Phóng bi, ghi bốn vị trí và tách một quỹ đạo thành hai chuyển động độc lập.', steps: 9 },
  { slug: 'centripetal-step', title: 'Lực hướng tâm và chuyển động tròn', subject: 'CHUYỂN ĐỘNG', kind: 'motion', code: '02', formula: 'F = mω²r', desc: 'Thay khối lượng, bán kính và tốc độ góc để thấy một quan hệ định lượng xuất hiện.', steps: 8 },
  { slug: 'accel-force-step', title: 'Gia tốc, lực và khối lượng', subject: 'CHUYỂN ĐỘNG', kind: 'motion', code: '03', formula: 'a = F/m', desc: 'Đo trên băng giấy và dùng cách giữ cố định biến để kiểm chứng định luật II Newton.', steps: 8 },
  { slug: 'energy-step', title: 'Bảo toàn cơ năng', subject: 'CHUYỂN ĐỘNG', kind: 'motion', code: '04', formula: '½v² ≈ gh', desc: 'Thả vật, đo độ cao và vận tốc, rồi tìm nguồn gốc của phần sai lệch.', steps: 8 },
  { slug: 'brownian-step', title: 'Chuyển động Brown và dữ liệu', subject: 'DỮ LIỆU & NGẪU NHIÊN', kind: 'data', code: '05', formula: '⟨r²⟩ = 4Dt', desc: 'Theo dõi hạt ngẫu nhiên, lấy mẫu nhiều lần và phân biệt đường đi với quy luật.', steps: 9 },
  { slug: 'river-step', title: 'Dòng sông tạo nên địa hình', subject: 'TỰ NHIÊN', kind: 'nature', code: '06', formula: 'Độ dốc → dòng chảy → địa hình', desc: 'Xoay sa bàn 3D, quan sát vận tốc, xói mòn và bồi tụ ở từng đoạn sông.', steps: 8 },
];

const grid = document.querySelector('#lesson-grid');
function render(filter = 'all') {
  grid.replaceChildren();
  for (const lesson of lessons.filter(item => filter === 'all' || item.kind === filter)) {
    const card = document.createElement('article');
    card.className = 'lesson-card';
    card.innerHTML = `<a href="./courses/${lesson.slug}.html" aria-label="Mở bài ${lesson.title}"><div class="card-image"><img src="./covers/${lesson.slug}.webp" alt="Ảnh mô hình 3D của bài ${lesson.title}" loading="lazy"><span class="card-code">${lesson.code} / 06</span></div><div class="card-body"><div class="card-top"><span>${lesson.subject}</span><span>${lesson.steps} BƯỚC</span></div><h3>${lesson.title}</h3><p>${lesson.desc}</p><div class="card-foot"><span>${lesson.formula}</span><strong aria-hidden="true">↗</strong></div></div></a>`;
    grid.append(card);
  }
}

document.querySelectorAll('[data-filter]').forEach(button => {
  button.addEventListener('click', () => {
    document.querySelectorAll('[data-filter]').forEach(item => {
      const active = item === button;
      item.classList.toggle('active', active);
      item.setAttribute('aria-pressed', String(active));
    });
    render(button.dataset.filter);
  });
});
render();
