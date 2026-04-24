---
title: DIN 7991 Countersunk Socket Head Screw Dimensions
layout: page
permalink: /reference/din7991/
---

This interactive tool provides the complete dimensions and tolerances for metric hexagon socket countersunk head cap screws as defined by **DIN 7991** (and mostly equivalent to ISO 10642). Select the screw size and length to update the diagram and data tables.

<div class="row mt-4">
  <!-- Top Row: Selection and Diagram -->
  <div class="col-lg-3 col-md-4">
    <div class="card p-3 shadow-sm mb-4 h-100">
      <h5 class="card-title h6 mb-3">Screw Selection</h5>
      <div class="form-group">
        <label for="screw-size" class="font-weight-bold small">Screw Size (d):</label>
        <select id="screw-size" class="form-control form-control-sm mb-3">
          <option value="M3">M3</option>
          <option value="M4">M4</option>
          <option value="M5">M5</option>
          <option value="M6" selected>M6</option>
          <option value="M8">M8</option>
          <option value="M10">M10</option>
          <option value="M12">M12</option>
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
          <!-- Countersunk head polygon -->
          <polygon id="svg-head" fill="#adb5bd" stroke="#495057" stroke-width="2.5" />
          <rect id="svg-shank" fill="#ced4da" stroke="#495057" stroke-width="2.5" />
          <path id="svg-threads" fill="none" stroke="#6c757d" stroke-width="1.5" stroke-dasharray="3,3" />
          <path id="svg-chamfer" fill="#adb5bd" stroke="#495057" stroke-width="2.5" />
          <rect id="svg-socket" fill="#e9ecef" stroke="#495057" stroke-width="1.5" />
        </g>
        
        <g id="top-view-group" transform="translate(200, 420)">
          <circle id="top-outer" r="80" fill="#adb5bd" stroke="#495057" stroke-width="2.5" />
          <!-- Inner circle representing the shank diameter, dashed -->
          <circle id="top-inner" r="45" fill="none" stroke="#495057" stroke-width="1.5" stroke-dasharray="4,4" />
          <polygon id="svg-top-hex" points="46.2,0 23.1,40 -23.1,40 -46.2,0 -23.1,-40 23.1,-40" fill="#e9ecef" stroke="#495057" stroke-width="1.5" />
          <g stroke="#6c757d" stroke-width="1" stroke-opacity="0.6">
            <line id="top-ext-s-1" x1="-30" y1="-40" x2="-130" y2="-40" />
            <line id="top-ext-s-2" x1="-30" y1="40" x2="-130" y2="40" />
            <line id="top-ext-e-1" x1="-46.2" y1="10" x2="-46.2" y2="130" />
            <line id="top-ext-e-2" x1="46.2" y1="10" x2="46.2" y2="130" />
          </g>
          <line id="top-dim-s-line-mid" stroke="#dc3545" stroke-width="2" />
          <line id="top-dim-s-line-1" stroke="#dc3545" stroke-width="2" marker-end="url(#arrow-end)" />
          <line id="top-dim-s-line-2" stroke="#dc3545" stroke-width="2" marker-end="url(#arrow-end)" />
          <text id="top-dim-s-text" x="-128" y="5" text-anchor="end" fill="#dc3545" font-size="14" font-weight="bold">s</text>
          <line id="top-dim-e-line-mid" stroke="#dc3545" stroke-width="2" />
          <line id="top-dim-e-line-1" stroke="#dc3545" stroke-width="2" marker-end="url(#arrow-end)" />
          <line id="top-dim-e-line-2" stroke="#dc3545" stroke-width="2" marker-end="url(#arrow-end)" />
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
            <line id="dim-k-line-mid" />
            <line id="dim-k-line-1" marker-end="url(#arrow-end)" />
            <line id="dim-k-line-2" marker-end="url(#arrow-end)" />
            <line id="dim-L-line" marker-start="url(#arrow-start)" marker-end="url(#arrow-end)" />
            <line id="dim-t-line" marker-end="url(#arrow-end)" />
            <line id="dim-t-line-2" marker-end="url(#arrow-end)" stroke="#dc3545" stroke-width="2" />
            <line id="dim-b-line" marker-start="url(#arrow-start)" marker-end="url(#arrow-end)" />
            <line id="dim-a-line" marker-start="url(#arrow-start)" marker-end="url(#arrow-end)" />
          </g>

          <g id="dim-texts" fill="#dc3545" font-size="14" font-weight="bold">
            <text id="dim-dk-text" text-anchor="middle">dk</text>
            <text id="dim-d-text" text-anchor="middle">d</text>
            <text id="dim-k-text" text-anchor="start">k</text>
            <text id="dim-L-text" text-anchor="start">L</text>
            <text id="dim-t-text" text-anchor="end">t</text>
            <text id="dim-b-text" text-anchor="start">b</text>
            <text id="dim-a-text" text-anchor="middle">Angle</text>
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
    'M3': { P: 0.50, dk: 6.0, k: 1.7, s: 2.0, t: 1.2, e: 2.30, b: 12, angle: 90, d: 3.0, lengths: [6, 8, 10, 12, 14, 16, 18, 20, 22, 25, 30] },
    'M4': { P: 0.70, dk: 8.0, k: 2.3, s: 2.5, t: 1.8, e: 2.87, b: 14, angle: 90, d: 4.0, lengths: [8, 10, 12, 14, 16, 18, 20, 22, 25, 30, 35, 40] },
    'M5': { P: 0.80, dk: 10.0, k: 2.8, s: 3.0, t: 2.3, e: 3.44, b: 16, angle: 90, d: 5.0, lengths: [10, 12, 14, 16, 18, 20, 22, 25, 30, 35, 40, 45, 50] },
    'M6': { P: 1.00, dk: 12.0, k: 3.3, s: 4.0, t: 2.5, e: 4.58, b: 18, angle: 90, d: 6.0, lengths: [10, 12, 14, 16, 18, 20, 22, 25, 30, 35, 40, 45, 50, 55, 60] },
    'M8': { P: 1.25, dk: 16.0, k: 4.4, s: 5.0, t: 3.5, e: 5.72, b: 22, angle: 90, d: 8.0, lengths: [12, 14, 16, 18, 20, 22, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70] },
    'M10': { P: 1.50, dk: 20.0, k: 5.5, s: 6.0, t: 4.4, e: 6.86, b: 26, angle: 90, d: 10.0, lengths: [16, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80] },
    'M12': { P: 1.75, dk: 24.0, k: 6.5, s: 8.0, t: 4.6, e: 9.15, b: 30, angle: 90, d: 12.0, lengths: [20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 90, 100] }
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
      if (l === 20 || (l > 20 && !Array.from(lengthSelect.options).some(o => o.value == 20))) {
         option.selected = true;
      }
      lengthSelect.appendChild(option);
    });
    if (lengthSelect.selectedIndex === -1) { lengthSelect.selectedIndex = 0; }
    updateDiagram();
  }

  function getTolerance(dim, value) {
    if (dim === 'dk') return "max";
    if (dim === 'k') return "max";
    if (dim === 'd') return "6g (std)";
    if (dim === 'L') {
      if (value <= 6) return "±0.24";
      if (value <= 30) return "±0.42";
      if (value <= 120) return "±0.70";
      return "±1.00";
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
      <tr><td>Angle</td><td>${data.angle}°</td><td>-</td></tr>
    `;
    document.getElementById('table-socket').innerHTML = `
      <tr><td>s (Socket)</td><td>${data.s}</td><td>-</td></tr>
      <tr><td>e (Corners)</td><td>${data.e}</td><td>min</td></tr>
      <tr><td>t (Depth)</td><td>${data.t}</td><td>min</td></tr>
    `;
    
    const drawData = screwData['M3'];
    const drawLength = 20;

    const startX = 450; 
    const startY = 80;
    const visShankW = 90;
    const scale = visShankW / drawData.d;
    const visHeadW = drawData.dk * scale;
    const visHeadH = drawData.k * scale;
    
    // Taper depth depends on angle.
    const halfAngleRad = (drawData.angle / 2) * Math.PI / 180;
    const taperDepth = ((visHeadW - visShankW) / 2) / Math.tan(halfAngleRad);
    
    // The vertical part of the head (the top rim)
    const visVertH = Math.max(0, visHeadH - taperDepth);

    const visShankH = 280;
    const visSocketW = drawData.s * scale * 1.2; // slight scale up for visibility
    const visSocketH = drawData.t * scale;
    const visThreadStart = 120;
    const chamferH = 14;

    // Draw Countersunk Head (polygon) with the vertical rim section
    const headPoints = `${startX - visHeadW/2},${startY} ${startX + visHeadW/2},${startY} ${startX + visHeadW/2},${startY + visVertH} ${startX + visShankW/2},${startY + visHeadH} ${startX - visShankW/2},${startY + visHeadH} ${startX - visHeadW/2},${startY + visVertH}`;
    document.getElementById('svg-head').setAttribute('points', headPoints);

    document.getElementById('svg-shank').setAttribute('x', startX - visShankW / 2);
    document.getElementById('svg-shank').setAttribute('y', startY + visHeadH);
    document.getElementById('svg-shank').setAttribute('width', visShankW);
    document.getElementById('svg-shank').setAttribute('height', visShankH);

    document.getElementById('svg-socket').setAttribute('x', startX - visSocketW / 2);
    document.getElementById('svg-socket').setAttribute('y', startY);
    document.getElementById('svg-socket').setAttribute('width', visSocketW);
    document.getElementById('svg-socket').setAttribute('height', visSocketH);

    // DIN 7991 L includes the head!
    const drawIsFullyThreaded = drawLength <= drawData.b;
    const threadY = drawIsFullyThreaded ? (startY + visHeadH) : (startY + visHeadH + visThreadStart);
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
    document.getElementById('dim-dk-text').textContent = `dk: ${data.dk} (max)`;

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

    // Side Dimensions Right
    const side_dist = 60; // Brought in closer
    document.getElementById('ext-k-top').setAttribute('x1', startX + visHeadW/2); document.getElementById('ext-k-top').setAttribute('y1', startY);
    document.getElementById('ext-k-top').setAttribute('x2', startX + visHeadW/2 + side_dist + ext); document.getElementById('ext-k-top').setAttribute('y2', startY);
    document.getElementById('ext-k-bottom').setAttribute('x1', startX + visShankW/2); document.getElementById('ext-k-bottom').setAttribute('y1', startY + visHeadH);
    document.getElementById('ext-k-bottom').setAttribute('x2', startX + visHeadW/2 + side_dist + ext); document.getElementById('ext-k-bottom').setAttribute('y2', startY + visHeadH);
    
    // Inward facing arrows for k
    document.getElementById('dim-k-line-1').setAttribute('x1', startX + visHeadW/2 + side_dist); document.getElementById('dim-k-line-1').setAttribute('x2', startX + visHeadW/2 + side_dist);
    document.getElementById('dim-k-line-1').setAttribute('y1', startY - 35); document.getElementById('dim-k-line-1').setAttribute('y2', startY);
    document.getElementById('dim-k-line-2').setAttribute('x1', startX + visHeadW/2 + side_dist); document.getElementById('dim-k-line-2').setAttribute('x2', startX + visHeadW/2 + side_dist);
    document.getElementById('dim-k-line-2').setAttribute('y1', startY + visHeadH + 35); document.getElementById('dim-k-line-2').setAttribute('y2', startY + visHeadH);
    
    document.getElementById('dim-k-text').setAttribute('x', startX + visHeadW/2 + side_dist + 12); document.getElementById('dim-k-text').setAttribute('y', startY + visHeadH/2 + 7);
    document.getElementById('dim-k-text').textContent = `k: ${data.k} (max)`;

    const b_dist = 60;
    const bGroupIds = ['ext-b-top', 'ext-b-bottom', 'dim-b-line', 'dim-b-text'];
    const isFullyThreaded = length <= data.b;
    bGroupIds.forEach(id => { document.getElementById(id).style.display = isFullyThreaded ? 'none' : 'block'; });
    
    // Always draw the elements based on drawIsFullyThreaded so they are correctly positioned if visible
    if (!drawIsFullyThreaded) {
      document.getElementById('ext-b-top').setAttribute('x1', startX + visShankW/2); document.getElementById('ext-b-top').setAttribute('y1', threadY);
      document.getElementById('ext-b-top').setAttribute('x2', startX + visHeadW/2 + b_dist + ext); document.getElementById('ext-b-top').setAttribute('y2', threadY);
      document.getElementById('ext-b-bottom').setAttribute('x1', startX + visShankW/2); document.getElementById('ext-b-bottom').setAttribute('y1', totalBottomY);
      document.getElementById('ext-b-bottom').setAttribute('x2', startX + visHeadW/2 + b_dist + ext); document.getElementById('ext-b-bottom').setAttribute('y2', totalBottomY);
      document.getElementById('dim-b-line').setAttribute('x1', startX + visHeadW/2 + b_dist); document.getElementById('dim-b-line').setAttribute('y1', threadY);
      document.getElementById('dim-b-line').setAttribute('x2', startX + visHeadW/2 + b_dist); document.getElementById('dim-b-line').setAttribute('y2', totalBottomY);
      document.getElementById('dim-b-text').setAttribute('x', startX + visHeadW / 2 + b_dist + 12); document.getElementById('dim-b-text').setAttribute('y', threadY + (totalBottomY - threadY)/2 + 7);
      document.getElementById('dim-b-text').textContent = `b: ${data.b} (min)`;
    }

    // L dimension, from startY to totalBottomY because it's a countersunk head
    const L_dist = 110; // Keep L in the same absolute spot (60+110=170)
    document.getElementById('ext-L-top').setAttribute('x1', startX + visHeadW/2); document.getElementById('ext-L-top').setAttribute('y1', startY);
    document.getElementById('ext-L-top').setAttribute('x2', startX + visHeadW/2 + side_dist + ext + L_dist); document.getElementById('ext-L-top').setAttribute('y2', startY);
    document.getElementById('ext-L-bottom').setAttribute('x1', startX + visShankW/2); document.getElementById('ext-L-bottom').setAttribute('y1', totalBottomY);
    document.getElementById('ext-L-bottom').setAttribute('x2', startX + visHeadW/2 + side_dist + ext + L_dist); document.getElementById('ext-L-bottom').setAttribute('y2', totalBottomY);
    document.getElementById('dim-L-line').setAttribute('x1', startX + visHeadW/2 + side_dist + L_dist); document.getElementById('dim-L-line').setAttribute('y1', startY);
    document.getElementById('dim-L-line').setAttribute('x2', startX + visHeadW/2 + side_dist + L_dist); document.getElementById('dim-L-line').setAttribute('y2', totalBottomY);
    document.getElementById('dim-L-text').setAttribute('x', startX + visHeadW / 2 + side_dist + L_dist + 12); document.getElementById('dim-L-text').setAttribute('y', startY + (totalBottomY - startY) / 2 + 7);
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

    // Angle text placement
    document.getElementById('dim-a-line').style.display = 'none';
    document.getElementById('dim-a-text').setAttribute('x', startX - visHeadW/2 - 30);
    document.getElementById('dim-a-text').setAttribute('y', startY + visHeadH/2 + 5);
    document.getElementById('dim-a-text').textContent = `Angle: ${data.angle}°`;

    // Inner circle scale for top view
    document.getElementById('top-inner').setAttribute('r', 80 * (visShankW / visHeadW));

    document.getElementById('top-dim-s-text').textContent = `s: ${data.s}`;
    document.getElementById('top-dim-e-text').textContent = `e: ${data.e} (min)`;
    
    // Update top hexagon based on 's' relative to 'dk' roughly
    // 80 is the radius for 'dk'. 
    // real 's' / real 'dk' = top_s / 160 => top_s = 160 * s / dk
    // hex points are derived from top_s
    const top_s = 160 * drawData.s / drawData.dk;
    const R = top_s / Math.sqrt(3); // distance to corner
    const hexPoints = `${R},0 ${R/2},${top_s/2} ${-R/2},${top_s/2} ${-R},0 ${-R/2},${-top_s/2} ${R/2},${-top_s/2}`;
    document.getElementById('svg-top-hex').setAttribute('points', hexPoints);
    
    document.getElementById('top-ext-s-1').setAttribute('y1', -top_s/2);
    document.getElementById('top-ext-s-1').setAttribute('y2', -top_s/2);
    document.getElementById('top-ext-s-2').setAttribute('y1', top_s/2);
    document.getElementById('top-ext-s-2').setAttribute('y2', top_s/2);
    
    document.getElementById('top-dim-s-line-1').setAttribute('x1', -120); document.getElementById('top-dim-s-line-1').setAttribute('x2', -120);
    document.getElementById('top-dim-s-line-1').setAttribute('y1', -top_s/2 - 35); document.getElementById('top-dim-s-line-1').setAttribute('y2', -top_s/2);
    document.getElementById('top-dim-s-line-2').setAttribute('x1', -120); document.getElementById('top-dim-s-line-2').setAttribute('x2', -120);
    document.getElementById('top-dim-s-line-2').setAttribute('y1', top_s/2 + 35); document.getElementById('top-dim-s-line-2').setAttribute('y2', top_s/2);
    
    const top_e = 160 * drawData.e / drawData.dk;
    document.getElementById('top-ext-e-1').setAttribute('x1', -top_e/2);
    document.getElementById('top-ext-e-1').setAttribute('x2', -top_e/2);
    document.getElementById('top-ext-e-2').setAttribute('x1', top_e/2);
    document.getElementById('top-ext-e-2').setAttribute('x2', top_e/2);

    document.getElementById('top-dim-e-line-1').setAttribute('y1', 120); document.getElementById('top-dim-e-line-1').setAttribute('y2', 120);
    document.getElementById('top-dim-e-line-1').setAttribute('x1', -top_e/2 - 35); document.getElementById('top-dim-e-line-1').setAttribute('x2', -top_e/2);
    document.getElementById('top-dim-e-line-2').setAttribute('y1', 120); document.getElementById('top-dim-e-line-2').setAttribute('y2', 120);
    document.getElementById('top-dim-e-line-2').setAttribute('x1', top_e/2 + 35); document.getElementById('top-dim-e-line-2').setAttribute('x2', top_e/2);

  }

  sizeSelect.addEventListener('change', populateLengths);
  lengthSelect.addEventListener('change', updateDiagram);
  populateLengths(); 
});
</script>

## Standard References
- **DIN 7991**: Hexagon socket countersunk head cap screws.
- **ISO 10642**: Hexagon socket countersunk head screws (supersedes DIN 7991).
- **Mechanical Properties**: Often available in classes 8.8, 10.9, 12.9, or stainless steel (A2, A4).
- **Critical Cross-Section**: Due to the head geometry and socket, the critical cross-section is located under the head. These screws are not recommended for applications requiring high axial preloading.
- **L**: Total length of the screw, including the countersunk head.
- **k**: Maximum head height.
- **Angle**: Typically 90° for sizes up to M20, and 60° for sizes above M20 (like M24).

---
*Note: Dimensions are for reference only. Always consult official DIN/ISO standards for critical engineering applications.*
