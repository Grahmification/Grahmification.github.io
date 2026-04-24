---
title: DIN 912 Socket Head Cap Screw Dimensions
layout: page
permalink: /reference/din912/
---

This interactive tool provides the complete dimensions and tolerances for metric socket head cap screws as defined by **DIN 912** (ISO 4762). Select the screw size and length to update the diagram and data tables.

<div class="row mt-4">
  <!-- Top Row: Selection and Diagram -->
  <div class="col-lg-3 col-md-4">
    <div class="card p-3 shadow-sm mb-4 h-100">
      <h5 class="card-title h6 mb-3">Screw Selection</h5>
      <div class="form-group">
        <label for="screw-size" class="font-weight-bold small">Screw Size (d):</label>
        <select id="screw-size" class="form-control form-control-sm mb-3">
          <option value="M1.6">M1.6</option>
          <option value="M2">M2</option>
          <option value="M2.5">M2.5</option>
          <option value="M3" selected>M3</option>
          <option value="M4">M4</option>
          <option value="M5">M5</option>
          <option value="M6">M6</option>
          <option value="M8">M8</option>
          <option value="M10">M10</option>
          <option value="M12">M12</option>
          <option value="M14">M14</option>
          <option value="M16">M16</option>
          <option value="M20">M20</option>
          <option value="M24">M24</option>
          <option value="M30">M30</option>
        </select>
      </div>
      <div class="form-group mb-0">
        <label for="screw-length" class="font-weight-bold small">Length (L):</label>
        <select id="screw-length" class="form-control form-control-sm">
          <!-- Populated by JS -->
        </select>
      </div>
    </div>
  </div>
  
  <div class="col-lg-9 col-md-8">
    <div class="card p-3 shadow-sm text-center">
      <svg id="screw-svg" viewBox="0 0 850 550" preserveAspectRatio="xMidYMid meet" style="width: 100%; height: auto; min-height: 500px; background-color: #f8f9fa; border-radius: 4px;">
        <defs>
          <marker id="arrow-start" markerWidth="12" markerHeight="12" refX="0" refY="6" orient="auto">
            <path d="M12,0 L0,6 L12,12 Z" fill="#dc3545" />
          </marker>
          <marker id="arrow-end" markerWidth="12" markerHeight="12" refX="12" refY="6" orient="auto">
            <path d="M0,0 L12,6 L0,12 Z" fill="#dc3545" />
          </marker>
        </defs>
        
        <g id="screw-group">
          <rect id="svg-head" fill="#adb5bd" stroke="#495057" stroke-width="2.5" />
          <polygon id="svg-da" fill="#dee2e6" stroke="#495057" stroke-width="1.5" />
          <rect id="svg-shank" fill="#ced4da" stroke="#495057" stroke-width="2.5" />
          <path id="svg-threads" fill="none" stroke="#6c757d" stroke-width="1.5" stroke-dasharray="3,3" />
          <path id="svg-chamfer" fill="#adb5bd" stroke="#495057" stroke-width="2.5" />
          <rect id="svg-socket" fill="#e9ecef" stroke="#495057" stroke-width="1.5" />
        </g>
        
        <g id="top-view-group" transform="translate(200, 420)">
          <circle r="80" fill="#adb5bd" stroke="#495057" stroke-width="2.5" />
          <polygon id="svg-top-hex" points="46.2,0 23.1,40 -23.1,40 -46.2,0 -23.1,-40 23.1,-40" fill="#e9ecef" stroke="#495057" stroke-width="1.5" />
          <g stroke="#6c757d" stroke-width="1" stroke-opacity="0.6">
            <line id="top-ext-s-1" x1="-30" y1="-40" x2="-130" y2="-40" />
            <line id="top-ext-s-2" x1="-30" y1="40" x2="-130" y2="40" />
            <line id="top-ext-e-1" x1="-46.2" y1="10" x2="-46.2" y2="130" />
            <line id="top-ext-e-2" x1="46.2" y1="10" x2="46.2" y2="130" />
          </g>
          <line x1="-120" y1="-40" x2="-120" y2="40" stroke="#dc3545" stroke-width="2" marker-start="url(#arrow-start)" marker-end="url(#arrow-end)" />
          <text id="top-dim-s-text" x="-128" y="5" text-anchor="end" fill="#dc3545" font-size="14" font-weight="bold">s</text>
          <line x1="-46.2" y1="120" x2="46.2" y2="120" stroke="#dc3545" stroke-width="2" marker-start="url(#arrow-start)" marker-end="url(#arrow-end)" />
          <text id="top-dim-e-text" x="0" y="142" text-anchor="middle" fill="#dc3545" font-size="14" font-weight="bold">e</text>
          <text y="-95" text-anchor="middle" font-size="13" fill="#495057" font-weight="bold">Top View</text>
        </g>

        <g id="labels-group">
          <g id="extension-lines" stroke="#6c757d" stroke-width="1" stroke-opacity="0.6">
            <line id="ext-dk-left" /><line id="ext-dk-right" />
            <line id="ext-d-left" /><line id="ext-d-right" />
            <line id="ext-k-top" /><line id="ext-k-bottom" />
            <line id="ext-L-top" /><line id="ext-L-bottom" />
            <line id="ext-t-top" /><line id="ext-t-bottom" />
            <line id="ext-b-top" /><line id="ext-b-bottom" />
          </g>

          <g id="dim-lines" stroke="#dc3545" stroke-width="2">
            <line id="dim-dk-line" marker-start="url(#arrow-start)" marker-end="url(#arrow-end)" />
            <line id="dim-d-line" marker-start="url(#arrow-start)" marker-end="url(#arrow-end)" />
            <line id="dim-da-line" marker-start="url(#arrow-start)" marker-end="url(#arrow-end)" />
            <line id="dim-k-line" marker-start="url(#arrow-start)" marker-end="url(#arrow-end)" />
            <line id="dim-L-line" marker-start="url(#arrow-start)" marker-end="url(#arrow-end)" />
            <line id="dim-t-line" marker-end="url(#arrow-end)" />
            <line id="dim-t-line-2" marker-end="url(#arrow-end)" stroke="#dc3545" stroke-width="2" />
            <line id="dim-b-line" marker-start="url(#arrow-start)" marker-end="url(#arrow-end)" />
            <line id="dim-r-line" marker-end="url(#arrow-end)" />
          </g>

          <g id="dim-texts" fill="#dc3545" font-size="14" font-weight="bold">
            <text id="dim-dk-text" text-anchor="middle">dk</text>
            <text id="dim-d-text" text-anchor="middle">d</text>
            <text id="dim-da-text" text-anchor="middle">da</text>
            <text id="dim-k-text" text-anchor="start">k</text>
            <text id="dim-L-text" text-anchor="start">L</text>
            <text id="dim-t-text" text-anchor="end">t</text>
            <text id="dim-b-text" text-anchor="start">b</text>
            <text id="dim-r-text" text-anchor="end">r</text>
          </g>
        </g>
      </svg>
    </div>
  </div>
</div>

<!-- Bottom Row: Grouped Tables -->
<div class="row mt-4" style="font-size: 0.8rem;">
  <div class="col-lg-4 col-md-6 mb-3">
    <div class="card shadow-sm h-100">
      <div class="card-header bg-light py-2"><h6 class="mb-0 small font-weight-bold">Thread & General</h6></div>
      <div class="card-body p-0 table-responsive">
        <table class="table table-sm table-bordered mb-0">
          <thead class="thead-light"><tr><th>Dim</th><th>Nominal</th><th>Tolerance</th></tr></thead>
          <tbody id="table-thread"></tbody>
        </table>
      </div>
    </div>
  </div>
  <div class="col-lg-4 col-md-6 mb-3">
    <div class="card shadow-sm h-100">
      <div class="card-header bg-light py-2"><h6 class="mb-0 small font-weight-bold">Head Geometry</h6></div>
      <div class="card-body p-0 table-responsive">
        <table class="table table-sm table-bordered mb-0">
          <thead class="thead-light"><tr><th>Dim</th><th>Nominal</th><th>Tolerance</th></tr></thead>
          <tbody id="table-head"></tbody>
        </table>
      </div>
    </div>
  </div>
  <div class="col-lg-4 col-md-12 mb-3">
    <div class="card shadow-sm h-100">
      <div class="card-header bg-light py-2"><h6 class="mb-0 small font-weight-bold">Socket Interface</h6></div>
      <div class="card-body p-0 table-responsive">
        <table class="table table-sm table-bordered mb-0">
          <thead class="thead-light"><tr><th>Dim</th><th>Nominal</th><th>Tolerance</th></tr></thead>
          <tbody id="table-socket"></tbody>
        </table>
      </div>
    </div>
  </div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  const screwData = {
    'M1.6': { P: 0.35, dk: 3.0, da: 2.0, k: 1.6, s: 1.5, t: 0.7, e: 1.73, b: 15, r: 0.1, d: 1.6, lengths: [3, 4, 5, 6, 8, 10, 12, 16] },
    'M2': { P: 0.40, dk: 3.8, da: 2.6, k: 2.0, s: 1.5, t: 1.0, e: 1.73, b: 16, r: 0.1, d: 2.0, lengths: [3, 4, 5, 6, 8, 10, 12, 14, 16, 20] },
    'M2.5': { P: 0.45, dk: 4.5, da: 3.1, k: 2.5, s: 2.0, t: 1.1, e: 2.30, b: 17, r: 0.1, d: 2.5, lengths: [4, 5, 6, 8, 10, 12, 14, 16, 18, 20, 25] },
    'M3': { P: 0.50, dk: 5.5, da: 3.6, k: 3.0, s: 2.5, t: 1.3, e: 2.87, b: 18, r: 0.1, d: 3.0, lengths: [4, 5, 6, 8, 10, 12, 14, 16, 18, 20, 22, 25, 30, 35, 40, 45, 50] },
    'M4': { P: 0.70, dk: 7.0, da: 4.7, k: 4.0, s: 3.0, t: 2.0, e: 3.44, b: 20, r: 0.2, d: 4.0, lengths: [5, 6, 8, 10, 12, 14, 16, 18, 20, 22, 25, 30, 35, 40, 45, 50, 55, 60, 70, 80] },
    'M5': { P: 0.80, dk: 8.5, da: 5.7, k: 5.0, s: 4.0, t: 2.5, e: 4.58, b: 22, r: 0.2, d: 5.0, lengths: [6, 8, 10, 12, 14, 16, 18, 20, 22, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 80, 90, 100] },
    'M6': { P: 1.00, dk: 10.0, da: 6.8, k: 6.0, s: 5.0, t: 3.0, e: 5.72, b: 24, r: 0.25, d: 6.0, lengths: [8, 10, 12, 14, 16, 18, 20, 22, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 90, 100, 110, 120] },
    'M8': { P: 1.25, dk: 13.0, da: 9.2, k: 8.0, s: 6.0, t: 4.0, e: 6.86, b: 28, r: 0.4, d: 8.0, lengths: [10, 12, 14, 16, 18, 20, 22, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 90, 100, 110, 120, 130, 140, 150] },
    'M10': { P: 1.50, dk: 16.0, da: 11.2, k: 10.0, s: 8.0, t: 5.0, e: 9.15, b: 32, r: 0.4, d: 10.0, lengths: [12, 14, 16, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 90, 100, 110, 120, 130, 140, 150, 160, 180, 200] },
    'M12': { P: 1.75, dk: 18.0, da: 13.7, k: 12.0, s: 10.0, t: 6.0, e: 11.43, b: 36, r: 0.6, d: 12.0, lengths: [16, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 90, 100, 110, 120, 130, 140, 150, 160, 180, 200, 220, 240, 250] },
    'M14': { P: 2.00, dk: 21.0, da: 15.7, k: 14.0, s: 12.0, t: 7.0, e: 13.72, b: 40, r: 0.6, d: 14.0, lengths: [20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 90, 100, 110, 120, 130, 140, 150] },
    'M16': { P: 2.00, dk: 24.0, da: 17.7, k: 16.0, s: 14.0, t: 8.0, e: 16.00, b: 44, r: 0.6, d: 16.0, lengths: [25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 90, 100, 110, 120, 130, 140, 150, 160, 180, 200, 220, 240, 260, 280, 300] },
    'M20': { P: 2.50, dk: 30.0, da: 22.4, k: 20.0, s: 17.0, t: 10.0, e: 19.44, b: 52, r: 0.8, d: 20.0, lengths: [30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 90, 100, 110, 120, 130, 140, 150, 160, 180, 200, 250, 300] },
    'M24': { P: 3.00, dk: 36.0, da: 26.4, k: 24.0, s: 19.0, t: 12.0, e: 21.73, b: 60, r: 0.8, d: 24.0, lengths: [40, 45, 50, 55, 60, 65, 70, 75, 80, 90, 100, 110, 120, 130, 140, 150, 160, 180, 200, 250, 300] },
    'M30': { P: 3.50, dk: 45.0, da: 33.4, k: 30.0, s: 22.0, t: 15.5, e: 25.15, b: 72, r: 1.0, d: 30.0, lengths: [50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 180, 200, 250, 300] }
  };

  const sizeSelect = document.getElementById('screw-size');
  const lengthSelect = document.getElementById('screw-length');
  
  function populateLengths() {
    const currentSize = sizeSelect.value;
    const data = screwData[currentSize];
    lengthSelect.innerHTML = '';
    data.lengths.forEach(l => {
      const option = document.createElement('option');
      option.value = l;
      option.textContent = l + ' mm';
      if (l === 12 || (l > 12 && !Array.from(lengthSelect.options).some(o => o.value == 12))) {
         option.selected = true;
      }
      lengthSelect.appendChild(option);
    });
    if (lengthSelect.selectedIndex === -1) { lengthSelect.selectedIndex = 0; }
    updateDiagram();
  }

  function getTolerance(dim, value) {
    if (dim === 'dk' || dim === 'k') {
      if (value <= 3) return "+0 / -0.25";
      if (value <= 6) return "+0 / -0.30";
      if (value <= 10) return "+0 / -0.36";
      if (value <= 18) return "+0 / -0.43";
      if (value <= 30) return "+0 / -0.52";
      return "+0 / -0.62";
    }
    if (dim === 'd') return "6g (std)";
    if (dim === 'L') {
      if (value <= 6) return "±0.24";
      if (value <= 30) return "±0.42";
      if (value <= 120) return "±0.70";
    }
    return "-";
  }

  function updateDiagram() {
    const size = sizeSelect.value;
    const length = parseFloat(lengthSelect.value);
    const data = screwData[size];
    
    // Update Tables
    document.getElementById('table-thread').innerHTML = `
      <tr><td>d (Nom.)</td><td>${data.d}</td><td>${getTolerance('d', data.d)}</td></tr>
      <tr><td>P (Pitch)</td><td>${data.P}</td><td>-</td></tr>
      <tr><td>L (Len.)</td><td>${length}</td><td>${getTolerance('L', length)}</td></tr>
      <tr><td>b (Thread)</td><td>${data.b}</td><td>min</td></tr>
    `;
    document.getElementById('table-head').innerHTML = `
      <tr><td>dk (Head)</td><td>${data.dk}</td><td>${getTolerance('dk', data.dk)}</td></tr>
      <tr><td>k (Height)</td><td>${data.k}</td><td>${getTolerance('k', data.k)}</td></tr>
      <tr><td>da (Trans.)</td><td>${data.da}</td><td>max</td></tr>
      <tr><td>r (Fillet)</td><td>${data.r}</td><td>min</td></tr>
    `;
    document.getElementById('table-socket').innerHTML = `
      <tr><td>s (Socket)</td><td>${data.s}</td><td>-</td></tr>
      <tr><td>e (Corners)</td><td>${data.e}</td><td>min</td></tr>
      <tr><td>t (Depth)</td><td>${data.t}</td><td>min</td></tr>
    `;
    
    const startX = 450; 
    const startY = 80;
    const visHeadW = 160;
    const visHeadH = 65;
    const visDaW = 105; 
    const visShankW = 90;
    const visShankH = 280;
    const visSocketW = 80;
    const visSocketH = 45;
    const visThreadStart = 120;
    const chamferH = 14;

    document.getElementById('svg-head').setAttribute('x', startX - visHeadW / 2);
    document.getElementById('svg-head').setAttribute('y', startY);
    document.getElementById('svg-head').setAttribute('width', visHeadW);
    document.getElementById('svg-head').setAttribute('height', visHeadH);
    
    const daTopY = startY + visHeadH;
    const daBotY = startY + visHeadH + 10;
    const daPoints = `${startX - visDaW/2},${daTopY} ${startX + visDaW/2},${daTopY} ${startX + visShankW/2},${daBotY} ${startX - visShankW/2},${daBotY}`;
    document.getElementById('svg-da').setAttribute('points', daPoints);

    document.getElementById('svg-shank').setAttribute('x', startX - visShankW / 2);
    document.getElementById('svg-shank').setAttribute('y', startY + visHeadH + 10);
    document.getElementById('svg-shank').setAttribute('width', visShankW);
    document.getElementById('svg-shank').setAttribute('height', visShankH - 10);

    document.getElementById('svg-socket').setAttribute('x', startX - visSocketW / 2);
    document.getElementById('svg-socket').setAttribute('y', startY);
    document.getElementById('svg-socket').setAttribute('width', visSocketW);
    document.getElementById('svg-socket').setAttribute('height', visSocketH);

    const isFullyThreaded = length <= data.b;
    const threadY = isFullyThreaded ? (startY + visHeadH + 10) : (startY + visHeadH + visThreadStart);
    const endY = startY + visHeadH + visShankH;
    const totalBottomY = endY + chamferH;

    document.getElementById('svg-threads').setAttribute('d', `M ${startX - visShankW/2 + 5} ${threadY} L ${startX - visShankW/2 + 5} ${endY} M ${startX + visShankW/2 - 5} ${threadY} L ${startX + visShankW/2 - 5} ${endY}`);
    document.getElementById('svg-chamfer').setAttribute('d', `M ${startX - visShankW/2} ${endY} L ${startX - visShankW/2 + 7} ${totalBottomY} L ${startX + visShankW/2 - 7} ${totalBottomY} L ${startX + visShankW/2} ${endY} Z`);

    const ext = 10;
    const shankBottomY = startY + visHeadH + visShankH;

    // dk
    const T_off = 55;
    document.getElementById('ext-dk-left').setAttribute('x1', startX - visHeadW/2); document.getElementById('ext-dk-left').setAttribute('y1', startY);
    document.getElementById('ext-dk-left').setAttribute('x2', startX - visHeadW/2); document.getElementById('ext-dk-left').setAttribute('y2', startY - T_off - ext);
    document.getElementById('ext-dk-right').setAttribute('x1', startX + visHeadW/2); document.getElementById('ext-dk-right').setAttribute('y1', startY);
    document.getElementById('ext-dk-right').setAttribute('x2', startX + visHeadW/2); document.getElementById('ext-dk-right').setAttribute('y2', startY - T_off - ext);
    document.getElementById('dim-dk-line').setAttribute('x1', startX - visHeadW/2); document.getElementById('dim-dk-line').setAttribute('y1', startY - T_off);
    document.getElementById('dim-dk-line').setAttribute('x2', startX + visHeadW/2); document.getElementById('dim-dk-line').setAttribute('y2', startY - T_off);
    document.getElementById('dim-dk-text').setAttribute('x', startX); document.getElementById('dim-dk-text').setAttribute('y', startY - T_off - 12);
    document.getElementById('dim-dk-text').textContent = `dk: ${data.dk} (${getTolerance('dk', data.dk)})`;

    // d
    const B_off = 55;
    document.getElementById('ext-d-left').setAttribute('x1', startX - visShankW / 2); document.getElementById('ext-d-left').setAttribute('y1', totalBottomY);
    document.getElementById('ext-d-left').setAttribute('x2', startX - visShankW / 2); document.getElementById('ext-d-left').setAttribute('y2', totalBottomY + B_off + ext);
    document.getElementById('ext-d-right').setAttribute('x1', startX + visShankW / 2); document.getElementById('ext-d-right').setAttribute('y1', totalBottomY);
    document.getElementById('ext-d-right').setAttribute('x2', startX + visShankW / 2); document.getElementById('ext-d-right').setAttribute('y2', totalBottomY + B_off + ext);
    document.getElementById('dim-d-line').setAttribute('x1', startX - visShankW / 2); document.getElementById('dim-d-line').setAttribute('y1', totalBottomY + B_off);
    document.getElementById('dim-d-line').setAttribute('x2', startX + visShankW / 2); document.getElementById('dim-d-line').setAttribute('y2', totalBottomY + B_off);
    document.getElementById('dim-d-text').setAttribute('x', startX); document.getElementById('dim-d-text').setAttribute('y', totalBottomY + B_off + 28);
    document.getElementById('dim-d-text').textContent = `d: ${data.d}`;

    // da
    const daY = startY + visHeadH + 5;
    document.getElementById('dim-da-line').setAttribute('x1', startX - visDaW/2); document.getElementById('dim-da-line').setAttribute('y1', daY + 20);
    document.getElementById('dim-da-line').setAttribute('x2', startX + visDaW/2); document.getElementById('dim-da-line').setAttribute('y2', daY + 20);
    document.getElementById('dim-da-text').setAttribute('x', startX); document.getElementById('dim-da-text').setAttribute('y', daY + 44);
    document.getElementById('dim-da-text').textContent = `da: ${data.da} (max)`;

    // Side Dimensions Right
    const side_dist = 145;
    document.getElementById('ext-k-top').setAttribute('x1', startX + visHeadW/2); document.getElementById('ext-k-top').setAttribute('y1', startY);
    document.getElementById('ext-k-top').setAttribute('x2', startX + visHeadW/2 + side_dist + ext); document.getElementById('ext-k-top').setAttribute('y2', startY);
    document.getElementById('ext-k-bottom').setAttribute('x1', startX + visHeadW/2); document.getElementById('ext-k-bottom').setAttribute('y1', startY + visHeadH);
    document.getElementById('ext-k-bottom').setAttribute('x2', startX + visHeadW/2 + side_dist + ext); document.getElementById('ext-k-bottom').setAttribute('y2', startY + visHeadH);
    document.getElementById('dim-k-line').setAttribute('x1', startX + visHeadW/2 + side_dist); document.getElementById('dim-k-line').setAttribute('y1', startY);
    document.getElementById('dim-k-line').setAttribute('x2', startX + visHeadW/2 + side_dist); document.getElementById('dim-k-line').setAttribute('y2', startY + visHeadH);
    document.getElementById('dim-k-text').setAttribute('x', startX + visHeadW/2 + side_dist + 12); document.getElementById('dim-k-text').setAttribute('y', startY + visHeadH/2 + 7);
    document.getElementById('dim-k-text').textContent = `k: ${data.k} (${getTolerance('k', data.k)})`;

    const b_dist = 60;
    const bGroupIds = ['ext-b-top', 'ext-b-bottom', 'dim-b-line', 'dim-b-text'];
    bGroupIds.forEach(id => { document.getElementById(id).style.display = isFullyThreaded ? 'none' : 'block'; });
    if (!isFullyThreaded) {
      document.getElementById('ext-b-top').setAttribute('x1', startX + visShankW/2); document.getElementById('ext-b-top').setAttribute('y1', threadY);
      document.getElementById('ext-b-top').setAttribute('x2', startX + visHeadW/2 + b_dist + ext); document.getElementById('ext-b-top').setAttribute('y2', threadY);
      document.getElementById('ext-b-bottom').setAttribute('x1', startX + visShankW/2); document.getElementById('ext-b-bottom').setAttribute('y1', totalBottomY);
      document.getElementById('ext-b-bottom').setAttribute('x2', startX + visHeadW/2 + b_dist + ext); document.getElementById('ext-b-bottom').setAttribute('y2', totalBottomY);
      document.getElementById('dim-b-line').setAttribute('x1', startX + visHeadW/2 + b_dist); document.getElementById('dim-b-line').setAttribute('y1', threadY);
      document.getElementById('dim-b-line').setAttribute('x2', startX + visHeadW/2 + b_dist); document.getElementById('dim-b-line').setAttribute('y2', totalBottomY);
      document.getElementById('dim-b-text').setAttribute('x', startX + visHeadW / 2 + b_dist + 12); document.getElementById('dim-b-text').setAttribute('y', threadY + (totalBottomY - threadY)/2 + 7);
      document.getElementById('dim-b-text').textContent = `b: ${data.b} (min)`;
    }

    document.getElementById('ext-L-top').setAttribute('x1', startX + visHeadW/2); document.getElementById('ext-L-top').setAttribute('y1', startY + visHeadH);
    document.getElementById('ext-L-top').setAttribute('x2', startX + visHeadW/2 + side_dist + ext); document.getElementById('ext-L-top').setAttribute('y2', startY + visHeadH);
    document.getElementById('ext-L-bottom').setAttribute('x1', startX + visShankW/2); document.getElementById('ext-L-bottom').setAttribute('y1', totalBottomY);
    document.getElementById('ext-L-bottom').setAttribute('x2', startX + visHeadW/2 + side_dist + ext); document.getElementById('ext-L-bottom').setAttribute('y2', totalBottomY);
    document.getElementById('dim-L-line').setAttribute('x1', startX + visHeadW/2 + side_dist); document.getElementById('dim-L-line').setAttribute('y1', startY + visHeadH);
    document.getElementById('dim-L-line').setAttribute('x2', startX + visHeadW/2 + side_dist); document.getElementById('dim-L-line').setAttribute('y2', totalBottomY);
    document.getElementById('dim-L-text').setAttribute('x', startX + visHeadW / 2 + side_dist + 12); document.getElementById('dim-L-text').setAttribute('y', startY + visHeadH + (totalBottomY - (startY + visHeadH)) / 2 + 7);
    document.getElementById('dim-L-text').textContent = `L: ${length} (${getTolerance('L', length)})`;

    const t_dist = 110;
    const t_x = startX - visHeadW/2 - t_dist;
    document.getElementById('ext-t-top').setAttribute('x1', startX); document.getElementById('ext-t-top').setAttribute('y1', startY);
    document.getElementById('ext-t-top').setAttribute('x2', t_x - 35); document.getElementById('ext-t-top').setAttribute('y2', startY);
    document.getElementById('ext-t-bottom').setAttribute('x1', startX); document.getElementById('ext-t-bottom').setAttribute('y1', startY + visSocketH);
    document.getElementById('ext-t-bottom').setAttribute('x2', t_x - 35); document.getElementById('ext-t-bottom').setAttribute('y2', startY + visSocketH);
    document.getElementById('dim-t-line').setAttribute('x1', t_x); document.getElementById('dim-t-line').setAttribute('y1', startY - 45);
    document.getElementById('dim-t-line').setAttribute('x2', t_x); document.getElementById('dim-t-line').setAttribute('y2', startY);
    document.getElementById('dim-t-line-2').setAttribute('x1', t_x); document.getElementById('dim-t-line-2').setAttribute('y1', startY + visSocketH + 45);
    document.getElementById('dim-t-line-2').setAttribute('x2', t_x); document.getElementById('dim-t-line-2').setAttribute('y2', startY + visSocketH);
    document.getElementById('dim-t-text').setAttribute('x', t_x - 12); document.getElementById('dim-t-text').setAttribute('y', startY + visSocketH/2 + 7);
    document.getElementById('dim-t-text').textContent = `t: ${data.t} (min)`;

    const rStartX = startX - visHeadW/2 + 2;
    const rStartY = startY + visHeadH + 2;
    const dimRLine = document.getElementById('dim-r-line');
    dimRLine.setAttribute('x1', rStartX - 35); dimRLine.setAttribute('y1', rStartY + 35);
    dimRLine.setAttribute('x2', rStartX); dimRLine.setAttribute('y2', rStartY);
    document.getElementById('dim-r-text').setAttribute('x', rStartX - 38); document.getElementById('dim-r-text').setAttribute('y', rStartY + 50);
    document.getElementById('dim-r-text').textContent = `r: ${data.r} (min)`;

    document.getElementById('top-dim-s-text').textContent = `s: ${data.s}`;
    document.getElementById('top-dim-e-text').textContent = `e: ${data.e} (min)`;
  }

  sizeSelect.addEventListener('change', populateLengths);
  lengthSelect.addEventListener('change', updateDiagram);
  populateLengths(); 
});
</script>

## Standard References
- **DIN 912**: Hexagon socket head cap screws.
- **ISO 4762**: Hexagon socket head cap screws (Metric).
- **Mechanical Properties**: Available in classes 8.8, 10.9, 12.9.
- **da**: Maximum transition diameter under head.
- **e**: Minimum width across corners of hex socket.
- **b**: Minimum thread length. Screws are fully threaded if $L \le b$.

---
*Note: Dimensions are for reference only. Always consult official DIN/ISO standards for critical engineering applications.*
