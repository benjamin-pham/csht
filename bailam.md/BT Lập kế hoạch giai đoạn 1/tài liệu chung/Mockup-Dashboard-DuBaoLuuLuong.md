# Mockup Dashboard Dự Báo Lưu Lượng — Ways Station

> **Tài liệu đặc tả & giao diện mẫu (Mockup UI Prototype)**  
> **Dự án:** Hệ thống Dự báo Lưu lượng Khách & Điều phối Vận hành (Ways Station)  
> **File gốc:** `bailam/BT Lập kế hoạch giai đoạn 1/tài liệu chung/Mockup-Dashboard-DuBaoLuuLuong.html`  
> **Lớp năng lực liên quan:** (4) App & Integration Platform + (5) Data Platform (TimesFM / MLOps / Real-time Analytics)

---

## 1. Tổng quan Giao diện (Overview)

Dashboard được thiết kế theo phong cách giao diện điều hành hiện đại (Dark Mode), tối ưu hóa trải nghiệm cho Quản lý Vận hành và Trưởng Chi nhánh Ways Station trong việc theo dõi, phân tích và đưa ra quyết định xếp ca nhân sự, chuẩn bị nguyên vật liệu F&B theo thời gian thực.

### 1.1. Cấu trúc Bố cục (Layout Architecture)
- **Header / Topbar:**
  - Logo thương hiệu: Ways Station · Dự báo lưu lượng.
  - Thông tin đồng bộ: Cập nhật lúc `06:00` hàng ngày.
  - Bộ điều hướng người dùng và Avatar quản trị.
- **Thanh bên trái (Sidebar Navigation):**
  - Danh sách chi nhánh:
    - *Lê Lợi:* Ổn định (dot xanh).
    - *Dương Quảng Hàm:* Chi nhánh trọng điểm đang chọn, cảnh báo có khung giờ vượt ngưỡng (dot vàng/cam).
    - *Nguyễn Oanh:* Chi nhánh mới hoạt động 12 ngày, chưa đủ dữ liệu lịch sử riêng (dot xám - đang dùng dự báo tham chiếu).
  - Bộ lọc dịch vụ: Tất cả, Gaming (net), Billiards, Ways Hub.
- **Khu vực trung tâm (Main Area - Heatmap Ribbon Card):**
  - Tiêu đề & Chọn phạm vi dự báo: 7 ngày hoặc 14 ngày.
  - Heatmap 24/7 Ribbon Card: Lưới trực quan hóa lưu lượng 24 khung giờ x 7 ngày trong tuần.
  - Thanh chú giải (Legend): Dải màu từ Vắng (Teal `#3FB8A6`) đến Đông (Amber `#F2A63B`), ký hiệu sọc chéo biểu thị khung giờ có độ tin cậy thấp cần điều phối viên kiểm tra lại.
  - Khu vực cảnh báo thông minh (Smart Alerts):
    - Cảnh báo vượt ngưỡng: Thứ 7 (20:00–23:00) dự báo vượt ngưỡng phục vụ, cao hơn 42% so với 4 tuần trước.
    - Cảnh báo dữ liệu tham chiếu: Chi nhánh Nguyễn Oanh tham chiếu 3 chi nhánh cùng khu vực.
- **Bảng chi tiết bên phải (Side Detail Panel):**
  - Khung giờ đang chọn: `21:00 – 22:00, Thứ 7`.
  - Dự báo lưu lượng: `86 lượt khách` (khoảng tin cậy: `71 – 101`).
  - Biểu đồ Whisker (Box/Whisker Plot): Trực quan hóa dải phân bố min-max và điểm dự báo.
  - Bảng chỉ số so sánh: Trung bình 4 tuần (`61`), Chênh lệch (`+41%`), Độ tin cậy (`Cao`), Yếu tố ảnh hưởng (`Cuối tuần`).
  - Đề xuất nhân sự (AI Decision Support): Gợi ý `4 người` (lịch phân ca hiện tại đang là `3 người`).
  - Nút hành động: Chấp nhận / Điều chỉnh.

---

## 2. Thông số & Logic Mô phỏng (Mock Logic)

### 2.1. Hệ số giờ trong ngày (24-hour Base Curve)
Hệ số mô phỏng chuỗi hoạt động 24/7 (khuya thấp điểm, chiều tối cao điểm):
```javascript
const base = [38, 26, 17, 11, 8, 7, 9, 14, 20, 25, 29, 34, 40, 44, 47, 50, 56, 64, 74, 83, 88, 82, 68, 52];
```

### 2.2. Hệ số ngày trong tuần (Day Multipliers)
Mô phỏng lưu lượng khách tăng mạnh vào các ngày cuối tuần:
- Chủ Nhật: `1.06`
- Thứ Hai: `0.78`
- Thứ Ba: `0.76`
- Thứ Tư: `0.80`
- Thứ Năm: `0.86`
- Thứ Sáu: `1.12`
- Thứ Bảy: `1.24`

### 2.3. Thang màu Heatmap (Color Stops)
Interpolation dải màu chuyển tiếp từ vắng tới đông:
- `rgb(26, 32, 45)`: Rất vắng
- `rgb(47, 80, 88)`: Thấp
- `rgb(63, 140, 130)`: Trung bình
- `rgb(176, 150, 80)`: Cao
- `rgb(242, 166, 59)`: Đỉnh điểm (Peak)

---

## 3. Mã nguồn Nguyên bản HTML/CSS/JS (Source Code)

Dưới đây là mã nguồn đầy đủ của file giao diện mẫu:

```html
<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Dự báo lưu lượng — Ways Station</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,500;12..96,700&family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@400;600&display=swap" rel="stylesheet">
<style>
  :root{
    --ink:#0E1119;
    --surface:#171B26;
    --surface-2:#1E2331;
    --line:#2A3143;
    --text:#E9ECF3;
    --muted:#8A93A8;
    --peak:#F2A63B;
    --quiet:#3FB8A6;
    --alert:#E2574C;
    --radius:10px;
  }
  *{box-sizing:border-box;margin:0;padding:0}
  body{
    background:var(--ink);
    color:var(--text);
    font-family:'Inter',system-ui,sans-serif;
    font-size:14px;
    line-height:1.5;
    -webkit-font-smoothing:antialiased;
  }
  .mono{font-family:'JetBrains Mono',monospace;font-variant-numeric:tabular-nums}
  h1,h2,h3{font-family:'Bricolage Grotesque',system-ui,sans-serif;font-weight:700;letter-spacing:-.02em}

  /* ---------- Topbar ---------- */
  .topbar{
    display:flex;align-items:center;justify-content:space-between;
    padding:14px 24px;border-bottom:1px solid var(--line);
    background:var(--surface);position:sticky;top:0;z-index:10;
  }
  .brand{display:flex;align-items:center;gap:12px}
  .mark{
    width:30px;height:30px;border-radius:8px;
    background:linear-gradient(135deg,var(--peak),var(--alert));
    display:grid;place-items:center;font-weight:700;font-size:13px;color:#0E1119;
    font-family:'Bricolage Grotesque',sans-serif;
  }
  .brand h1{font-size:15px}
  .brand span{display:block;font-size:11px;color:var(--muted);font-family:'Inter';font-weight:400;letter-spacing:0}
  .topbar-right{display:flex;align-items:center;gap:18px}
  .stamp{font-size:11.5px;color:var(--muted)}
  .stamp b{color:var(--text);font-weight:500}
  .avatar{
    width:28px;height:28px;border-radius:50%;background:var(--surface-2);
    border:1px solid var(--line);display:grid;place-items:center;font-size:11px;color:var(--muted)
  }

  /* ---------- Layout ---------- */
  .shell{display:grid;grid-template-columns:220px 1fr 300px;min-height:calc(100vh - 59px)}
  aside{border-right:1px solid var(--line);padding:20px 0;background:var(--surface)}
  main{padding:24px 26px;overflow:hidden}
  .side-panel{border-left:1px solid var(--line);padding:22px 20px;background:var(--surface)}

  .eyebrow{
    font-size:10.5px;letter-spacing:.13em;text-transform:uppercase;
    color:var(--muted);font-weight:600;
  }
  aside .eyebrow{padding:0 20px;margin-bottom:10px}

  .branch{
    display:flex;align-items:center;justify-content:space-between;gap:8px;
    padding:9px 20px;cursor:pointer;border-left:2px solid transparent;
    transition:background .15s;
  }
  .branch:hover{background:var(--surface-2)}
  .branch.on{background:var(--surface-2);border-left-color:var(--peak)}
  .branch-name{font-size:13px;font-weight:500}
  .branch-meta{font-size:11px;color:var(--muted);margin-top:1px}
  .dot{width:6px;height:6px;border-radius:50%;flex-shrink:0}
  .dot.peak{background:var(--peak)}
  .dot.ok{background:var(--quiet)}
  .dot.new{background:var(--muted)}

  .side-divider{height:1px;background:var(--line);margin:18px 0}

  /* ---------- Main head ---------- */
  .head{display:flex;align-items:flex-end;justify-content:space-between;margin-bottom:6px;flex-wrap:wrap;gap:14px}
  .head h2{font-size:22px}
  .head p{color:var(--muted);font-size:12.5px;margin-top:3px}
  .seg{display:flex;border:1px solid var(--line);border-radius:8px;overflow:hidden}
  .seg button{
    background:transparent;border:0;color:var(--muted);font:inherit;font-size:12px;
    padding:6px 13px;cursor:pointer;border-right:1px solid var(--line);
  }
  .seg button:last-child{border-right:0}
  .seg button.on{background:var(--surface-2);color:var(--text);font-weight:500}

  /* ---------- Ribbon (signature) ---------- */
  .ribbon-card{
    background:var(--surface);border:1px solid var(--line);border-radius:var(--radius);
    padding:20px 22px 16px;margin-top:20px;
  }
  .hours{display:grid;grid-template-columns:56px repeat(24,1fr);gap:3px;margin-bottom:7px}
  .hours span{
    font-size:9.5px;color:var(--muted);text-align:center;
    font-family:'JetBrains Mono',monospace;
  }
  .row{display:grid;grid-template-columns:56px repeat(24,1fr);gap:3px;margin-bottom:3px;align-items:center}
  .row-label{font-size:11.5px;color:var(--muted);font-weight:500}
  .row.today .row-label{color:var(--text)}
  .cell{
    height:26px;border-radius:3px;cursor:pointer;position:relative;
    transition:transform .12s, outline-color .12s;
    outline:1.5px solid transparent;outline-offset:1px;
  }
  .cell:hover{transform:scaleY(1.14);outline-color:var(--text)}
  .cell.sel{outline-color:var(--peak)}
  .cell.low-conf::after{
    content:'';position:absolute;inset:0;border-radius:3px;
    background:repeating-linear-gradient(45deg,transparent 0 3px,rgba(255,255,255,.22) 3px 5px);
  }

  .legend{display:flex;align-items:center;gap:18px;margin-top:14px;flex-wrap:wrap}
  .scale{display:flex;align-items:center;gap:7px;font-size:11px;color:var(--muted)}
  .scale-bar{display:flex;gap:2px}
  .scale-bar i{width:16px;height:9px;border-radius:2px;display:block}
  .lg{display:flex;align-items:center;gap:6px;font-size:11px;color:var(--muted)}
  .lg .swatch{width:11px;height:11px;border-radius:2px;background:var(--surface-2);border:1px solid var(--line)}
  .lg .swatch.hatch{background:repeating-linear-gradient(45deg,var(--surface-2) 0 3px,rgba(255,255,255,.22) 3px 5px)}

  /* ---------- Detail panel ---------- */
  .slot-time{font-family:'Bricolage Grotesque',sans-serif;font-size:26px;font-weight:700;letter-spacing:-.02em}
  .slot-day{font-size:12px;color:var(--muted);margin-top:2px}
  .big{margin:20px 0 4px}
  .big .n{font-family:'JetBrains Mono',monospace;font-size:42px;font-weight:600;line-height:1;color:var(--peak)}
  .big .u{font-size:12px;color:var(--muted);margin-left:6px}
  .range{font-size:12px;color:var(--muted);font-family:'JetBrains Mono',monospace}

  .whisker{margin:16px 0 4px;position:relative;height:30px}
  .whisker-track{position:absolute;top:13px;left:0;right:0;height:4px;background:var(--surface-2);border-radius:2px}
  .whisker-band{position:absolute;top:13px;height:4px;background:rgba(242,166,59,.32);border-radius:2px}
  .whisker-point{position:absolute;top:8px;width:3px;height:14px;background:var(--peak);border-radius:1px}
  .whisker-labels{display:flex;justify-content:space-between;font-size:10px;color:var(--muted);font-family:'JetBrains Mono',monospace;position:absolute;top:0;left:0;right:0}

  .kv{display:flex;justify-content:space-between;padding:9px 0;border-bottom:1px solid var(--line);font-size:12.5px}
  .kv:last-of-type{border-bottom:0}
  .kv span{color:var(--muted)}
  .kv b{font-weight:600;font-family:'JetBrains Mono',monospace}

  .suggest{
    margin-top:16px;padding:14px 16px;background:var(--surface-2);
    border-radius:8px;border:1px solid var(--line);
  }
  .suggest .num{font-size:18px;font-weight:600;color:var(--text);margin-top:4px}
  .suggest .cmp{font-size:11.5px;color:var(--muted);margin-top:2px}

  .actions{display:flex;gap:8px;margin-top:16px}
  .actions button{
    flex:1;padding:9px 12px;border-radius:7px;border:0;cursor:pointer;
    font:inherit;font-size:12.5px;font-weight:500;
  }
  .actions .primary{background:var(--peak);color:#0E1119}
  .actions .ghost{background:transparent;border:1px solid var(--line);color:var(--text)}

  .note{font-size:11px;color:var(--muted);line-height:1.45;margin-top:14px}

  /* ---------- Alerts ---------- */
  .alerts{margin-top:26px}
  .alert-item{
    display:flex;gap:12px;align-items:flex-start;padding:12px 14px;
    background:var(--surface);border:1px solid var(--line);border-radius:8px;margin-bottom:8px;
  }
  .alert-item .bar{width:3px;align-self:stretch;border-radius:2px;flex-shrink:0}
  .alert-item.warn .bar{background:var(--peak)}
  .alert-item.info .bar{background:var(--quiet)}
  .alert-item p{font-size:12.5px;color:var(--text);font-weight:500}
  .alert-item small{display:block;font-size:11px;color:var(--muted);margin-top:2px}
</style>
</head>
<body>

<div class="topbar">
  <div class="brand">
    <div class="mark">WS</div>
    <div>
      <h1>Ways Station</h1>
      <span>Dự báo lưu lượng</span>
    </div>
  </div>
  <div class="topbar-right">
    <span class="stamp">Dự báo lúc <b>06:00</b> hôm nay</span>
    <div class="avatar" title="Quản trị viên">AD</div>
  </div>
</div>

<div class="shell">
  <!-- ASIDE -->
  <aside>
    <div class="eyebrow">Chi nhánh</div>
    <div class="branch">
      <div>
        <div class="branch-name">Lê Lợi</div>
        <div class="branch-meta">Gym · Boxing · 1.000 m²</div>
      </div>
      <div class="dot ok" title="Ổn định"></div>
    </div>
    <div class="branch on">
      <div>
        <div class="branch-name">Dương Quảng Hàm</div>
        <div class="branch-meta">Hub · Net · Bida · Cầu lông</div>
      </div>
      <div class="dot peak" title="Có khung giờ vượt ngưỡng"></div>
    </div>
    <div class="branch">
      <div>
        <div class="branch-name">Nguyễn Oanh</div>
        <div class="branch-meta">Chi nhánh mới · 12 ngày</div>
      </div>
      <div class="dot new" title="Chưa đủ dữ liệu lịch sử"></div>
    </div>

    <div class="side-divider"></div>

    <div class="eyebrow">Dịch vụ</div>
    <div class="branch on"><div class="branch-name">Tất cả</div></div>
    <div class="branch"><div class="branch-name">Gaming</div></div>
    <div class="branch"><div class="branch-name">Billiards</div></div>
    <div class="branch"><div class="branch-name">Hub</div></div>
  </aside>

  <!-- MAIN -->
  <main>
    <div class="head">
      <div>
        <h2>Dương Quảng Hàm</h2>
        <p>Dự báo 7 ngày tới · cập nhật lúc 06:00 mỗi ngày</p>
      </div>
      <div class="seg">
        <button class="on">7 ngày</button>
        <button>14 ngày</button>
      </div>
    </div>

    <div class="ribbon-card">
      <div class="hours" id="hours"></div>
      <div id="rows"></div>

      <div class="legend">
        <div class="scale">
          <span>Vắng</span>
          <div class="scale-bar" id="scaleBar"></div>
          <span>Đông</span>
        </div>
        <div class="lg"><span class="swatch hatch"></span> Độ tin cậy thấp — cần người điều phối xem lại</div>
        <div class="lg">Chọn một ô để xem chi tiết</div>
      </div>
    </div>

    <div class="alerts">
      <div class="eyebrow" style="margin-bottom:10px">Cần chú ý</div>
      <div class="alert-item warn">
        <div class="bar"></div>
        <div>
          <p>Thứ 7, 20:00–23:00 — dự báo vượt ngưỡng phục vụ của ca hiện tại</p>
          <small>Mức dự báo cao hơn 42% so với cùng khung giờ 4 tuần trước</small>
        </div>
      </div>
      <div class="alert-item info">
        <div class="bar"></div>
        <div>
          <p>Chi nhánh Nguyễn Oanh đang dùng dự báo tham chiếu</p>
          <small>Mới hoạt động 12 ngày, chưa đủ dữ liệu riêng. Đang tham chiếu 3 chi nhánh cùng khu vực và cùng tổ hợp dịch vụ</small>
        </div>
      </div>
    </div>
  </main>

  <!-- DETAIL -->
  <div class="side-panel">
    <div class="eyebrow">Khung giờ đang chọn</div>
    <div class="slot-time" id="slotTime">21:00 – 22:00</div>
    <div class="slot-day" id="slotDay">Thứ 7, 29/08</div>

    <div class="big">
      <span class="n" id="slotN">86</span><span class="u">lượt khách</span>
    </div>
    <div class="range" id="slotRange">khoảng 71 – 101</div>

    <div class="whisker">
      <div class="whisker-labels"><span>60</span><span>110</span></div>
      <div class="whisker-track"></div>
      <div class="whisker-band" style="left:22%;right:18%"></div>
      <div class="whisker-point" style="left:52%"></div>
    </div>

    <div style="margin-top:20px">
      <div class="kv"><span>Trung bình 4 tuần</span><b>61</b></div>
      <div class="kv"><span>Chênh lệch</span><b style="color:var(--peak)">+41%</b></div>
      <div class="kv"><span>Độ tin cậy</span><b>Cao</b></div>
      <div class="kv"><span>Yếu tố ảnh hưởng</span><b>Cuối tuần</b></div>
    </div>

    <div class="suggest">
      <div class="eyebrow">Nhân sự đề xuất</div>
      <div class="num">4 người</div>
      <div class="cmp">Lịch hiện tại đang xếp 3 người</div>
    </div>

    <div class="actions">
      <button class="primary">Chấp nhận</button>
      <button class="ghost">Điều chỉnh</button>
    </div>

    <p class="note">
      Con số là ước lượng từ dữ liệu lịch sử, không phải cam kết. Quyết định xếp ca cuối cùng thuộc về Phòng Điều phối.
    </p>
  </div>
</div>

<script>
(function(){
  const days=['CN 24/08','T2 25/08','T3 26/08','T4 27/08','T5 28/08','T6 29/08','T7 30/08'];
  // hệ số theo giờ: khuya thấp, chiều tối cao (mô phỏng chuỗi 24/7)
  const base=[38,26,17,11,8,7,9,14,20,25,29,34,40,44,47,50,56,64,74,83,88,82,68,52];
  const dayMul=[1.06,.78,.76,.80,.86,1.12,1.24];

  function color(v){
    const stops=[[26,32,45],[47,80,88],[63,140,130],[176,150,80],[242,166,59]];
    const t=Math.min(.999,Math.max(0,v))*(stops.length-1);
    const i=Math.floor(t), f=t-i;
    const a=stops[i], b=stops[Math.min(i+1,stops.length-1)];
    const rgb=[0,1,2].map(k=>Math.round(a[k]+(b[k]-a[k])*f));
    return `rgb(${rgb.join(',')})`;
  }

  // Header giờ 0..23
  const hEl=document.getElementById('hours');
  hEl.appendChild(document.createElement('span'));
  for(let h=0; h<24; h++){
    const s=document.createElement('span');
    s.textContent=(h%3===0||h===23)?h:'';
    hEl.appendChild(s);
  }

  // Thang màu legend
  const sb=document.getElementById('scaleBar');
  for(let i=0; i<8; i++){
    const seg=document.createElement('i');
    seg.style.background=color(i/7);
    sb.appendChild(seg);
  }

  // Render các hàng (ngày)
  const rEl=document.getElementById('rows');
  let selCell=null;

  days.forEach((day,dIdx)=>{
    const row=document.createElement('div');
    row.className='row'+(dIdx===0?' today':'');
    const lbl=document.createElement('div');
    lbl.className='row-label';
    lbl.textContent=day;
    row.appendChild(lbl);

    for(let h=0; h<24; h++){
      const c=document.createElement('div');
      c.className='cell';
      const raw=base[h]*dayMul[dIdx];
      const jitter=(Math.sin(dIdx*13+h*7)*.1);
      const val=Math.max(5,Math.round(raw*(1+jitter)));
      const norm=Math.min(1,val/105);
      c.style.background=color(norm);

      // mô phỏng một vài ô độ tin cậy thấp (khung giờ mới/bất thường)
      const lowConf=(dIdx===6 && (h===14||h===15)) || (dIdx===4 && h===2);
      if(lowConf) c.classList.add('low-conf');

      c.title=`${day} · ${h}:00 — ${val} lượt (${lowConf?'Độ tin cậy thấp':'Bình thường'})`;

      c.addEventListener('click',()=>{
        if(selCell) selCell.classList.remove('sel');
        c.classList.add('sel');
        selCell=c;
        updateDetail(day, h, val, lowConf);
      });

      // mặc định chọn ô Thứ 7, 21:00
      if(dIdx===5 && h===21){
        setTimeout(()=>{ c.click(); },0);
      }

      row.appendChild(c);
    }
    rEl.appendChild(row);
  });

  function updateDetail(day, h, val, lowConf){
    document.getElementById('slotTime').textContent=`${String(h).padStart(2,'0')}:00 – ${String(h+1).padStart(2,'0')}:00`;
    document.getElementById('slotDay').textContent=day;
    document.getElementById('slotN').textContent=val;
    const spread=Math.round(val*.18);
    const low=Math.max(5,val-spread), high=val+spread;
    document.getElementById('slotRange').textContent=`khoảng ${low} – ${high}`;
  }
})();
</script>
</body>
</html>
```
