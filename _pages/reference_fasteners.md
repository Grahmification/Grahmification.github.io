---
title: Metric Socket Head Screw Dimensions
layout: page
permalink: /reference/engineering/fasteners/
---

<style>
  .dim-group { cursor: help; transition: opacity 0.2s; }
  .dim-group:hover { opacity: 0.6; }
  #custom-tooltip {
    position: fixed;
    display: none;
    background: #343a40;
    color: #fff;
    padding: 8px 12px;
    border-radius: 4px;
    font-size: 0.85rem;
    pointer-events: none;
    z-index: 2000;
    box-shadow: 0 4px 12px rgba(0,0,0,0.15);
    max-width: 250px;
    line-height: 1.4;
    border: 1px solid #495057;
  }
</style>

<!-- Tooltip Element -->
<div id="custom-tooltip"></div>

This interactive tool provides the complete dimensions and tolerances for metric socket head cap screws. Select the screw type, size, and length to update the diagram and data tables.

<div class="row mt-4">
  <div class="col-12">
    <div class="card p-3 shadow-sm mb-4">
      <!-- Top Row: Selections -->
      <div class="row mb-3 text-left">
        <div class="col-md-4 mb-2 mb-md-0">
          <label for="screw-type" class="font-weight-bold small">Screw Type:</label>
          <select id="screw-type" class="form-control form-control-sm">
            <option value="din912" selected>Socket Head Cap Screw (DIN 912)</option>
            <option value="din7991">Countersunk Socket Head Screw (DIN 7991)</option>
          </select>
        </div>
        <div class="col-md-4 mb-2 mb-md-0">
          <label for="screw-size" class="font-weight-bold small">Screw Size (d):</label>
          <select id="screw-size" class="form-control form-control-sm"></select>
        </div>
        <div class="col-md-4">
          <label for="screw-length" class="font-weight-bold small">Length (L):</label>
          <select id="screw-length" class="form-control form-control-sm"></select>
        </div>
      </div>
      
      <!-- Diagram -->
      <div id="svg-container" class="text-center">
      </div>
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

<template id="svg-template-912">
<svg id="screw-svg" viewBox="0 0 850 650" preserveAspectRatio="xMidYMid meet" style="width: 100%; height: auto; min-height: 500px; background-color: #f8f9fa; border-radius: 4px;">
        <defs>
          <marker id="arrow-start" markerWidth="9" markerHeight="9" refX="0" refY="4.5" orient="auto">
            <path d="M9,0 L0,4.5 L9,9 Z" fill="#dc3545" />
          </marker>
          <marker id="arrow-end" markerWidth="9" markerHeight="9" refX="9" refY="4.5" orient="auto">
            <path d="M0,0 L9,4.5 L0,9 Z" fill="#dc3545" />
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
          <g class="dim-group" data-title="Socket Size (s): Distance across the flats of the hexagon socket.">
            <line x1="-120" y1="-40" x2="-120" y2="40" stroke="#dc3545" stroke-width="2" marker-start="url(#arrow-start)" marker-end="url(#arrow-end)" />
            <text id="top-dim-s-text" x="-128" y="5" text-anchor="end" fill="#dc3545" font-size="14" font-weight="bold">s</text>
          </g>
          <g class="dim-group" data-title="Corner Width (e): Minimum distance across the corners of the hexagon socket.">
            <line x1="-46.2" y1="120" x2="46.2" y2="120" stroke="#dc3545" stroke-width="2" marker-start="url(#arrow-start)" marker-end="url(#arrow-end)" />
            <text id="top-dim-e-text" x="0" y="142" text-anchor="middle" fill="#dc3545" font-size="14" font-weight="bold">e</text>
          </g>
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

          <g id="dimensions-group" stroke="#dc3545" stroke-width="2" fill="#dc3545" font-size="14" font-weight="bold">
            <g class="dim-group" data-title="Head Diameter (dk): The maximum diameter of the cylindrical screw head.">
              <line id="dim-dk-line" marker-start="url(#arrow-start)" marker-end="url(#arrow-end)" />
              <text id="dim-dk-text" text-anchor="middle" stroke="none">dk</text>
            </g>
            <g class="dim-group" data-title="Nominal Diameter (d): The major diameter of the thread.">
              <line id="dim-d-line" marker-start="url(#arrow-start)" marker-end="url(#arrow-end)" />
              <text id="dim-d-text" text-anchor="middle" stroke="none">d</text>
            </g>
            <g class="dim-group" data-title="Transition Diameter (da): The maximum diameter of the transition under the head.">
              <line id="dim-da-line" marker-start="url(#arrow-start)" marker-end="url(#arrow-end)" />
              <text id="dim-da-text" text-anchor="middle" stroke="none">da</text>
            </g>
            <g class="dim-group" data-title="Head Height (k): The height of the cylindrical head.">
              <line id="dim-k-line" marker-start="url(#arrow-start)" marker-end="url(#arrow-end)" />
              <text id="dim-k-text" text-anchor="start" stroke="none">k</text>
            </g>
            <g class="dim-group" data-title="Length (L): The length of the screw shank, measured from under the head.">
              <line id="dim-L-line" marker-start="url(#arrow-start)" marker-end="url(#arrow-end)" />
              <text id="dim-L-text" text-anchor="start" stroke="none">L</text>
            </g>
            <g class="dim-group" data-title="Socket Depth (t): Minimum engagement depth for the hex key.">
              <line id="dim-t-line" marker-end="url(#arrow-end)" />
              <line id="dim-t-line-2" marker-end="url(#arrow-end)" />
              <text id="dim-t-text" text-anchor="end" stroke="none">t</text>
            </g>
            <g id="b-dim-group" class="dim-group" data-title="Thread Length (b): The minimum length of the threaded portion.">
              <line id="dim-b-line" marker-start="url(#arrow-start)" marker-end="url(#arrow-end)" />
              <text id="dim-b-text" text-anchor="start" stroke="none">b</text>
            </g>
            <g class="dim-group" data-title="Fillet Radius (r): The minimum radius under the head.">
              <line id="dim-r-line" marker-end="url(#arrow-end)" />
              <text id="dim-r-text" text-anchor="end" stroke="none">r</text>
            </g>
          </g>
        </g>
      </svg>
</template>
<template id="svg-template-7991">
<svg id="screw-svg" viewBox="0 0 850 650" preserveAspectRatio="xMidYMid meet" style="width: 100%; height: auto; min-height: 500px; background-color: #f8f9fa; border-radius: 4px;">
        <defs>
          <marker id="arrow-start" markerWidth="9" markerHeight="9" refX="0" refY="4.5" orient="auto">
            <path d="M9,0 L0,4.5 L9,9 Z" fill="#dc3545" />
          </marker>
          <marker id="arrow-end" markerWidth="9" markerHeight="9" refX="9" refY="4.5" orient="auto">
            <path d="M0,0 L9,4.5 L0,9 Z" fill="#dc3545" />
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
          <g class="dim-group" data-title="Socket Size (s): Distance across the flats of the hexagon socket.">
            <line x1="-120" y1="-40" x2="-120" y2="40" stroke="#dc3545" stroke-width="2" marker-start="url(#arrow-start)" marker-end="url(#arrow-end)" />
            <text id="top-dim-s-text" x="-128" y="5" text-anchor="end" fill="#dc3545" font-size="14" font-weight="bold">s</text>
          </g>
          <g class="dim-group" data-title="Corner Width (e): Minimum distance across the corners of the hexagon socket.">
            <line x1="-46.2" y1="120" x2="46.2" y2="120" stroke="#dc3545" stroke-width="2" marker-start="url(#arrow-start)" marker-end="url(#arrow-end)" />
            <text id="top-dim-e-text" x="0" y="142" text-anchor="middle" fill="#dc3545" font-size="14" font-weight="bold">e</text>
          </g>
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
            <line id="ext-a-left" /><line id="ext-a-right" />
          </g>

          <g id="dimensions-group" stroke="#dc3545" stroke-width="2" fill="#dc3545" font-size="14" font-weight="bold">
            <g class="dim-group" data-title="Head Diameter (dk): The maximum diameter of the countersunk head.">
              <line id="dim-dk-line" marker-start="url(#arrow-start)" marker-end="url(#arrow-end)" />
              <text id="dim-dk-text" text-anchor="middle" stroke="none">dk</text>
            </g>
            <g class="dim-group" data-title="Nominal Diameter (d): The major diameter of the thread.">
              <line id="dim-d-line" marker-start="url(#arrow-start)" marker-end="url(#arrow-end)" />
              <text id="dim-d-text" text-anchor="middle" stroke="none">d</text>
            </g>
            <g class="dim-group" data-title="Head Height (k): Maximum distance from the top of the head to the shank.">
              <line id="dim-k-line" marker-start="url(#arrow-start)" marker-end="url(#arrow-end)" />
              <text id="dim-k-text" text-anchor="start" stroke="none">k</text>
            </g>
            <g class="dim-group" data-title="Total Length (L): The overall length including the countersunk head.">
              <line id="dim-L-line" marker-start="url(#arrow-start)" marker-end="url(#arrow-end)" />
              <text id="dim-L-text" text-anchor="start" stroke="none">L</text>
            </g>
            <g class="dim-group" data-title="Socket Depth (t): Minimum engagement depth for the hex key.">
              <line id="dim-t-line" marker-end="url(#arrow-end)" />
              <line id="dim-t-line-2" marker-end="url(#arrow-end)" />
              <text id="dim-t-text" text-anchor="end" stroke="none">t</text>
            </g>
            <g id="b-dim-group" class="dim-group" data-title="Thread Length (b): The minimum length of the threaded portion.">
              <line id="dim-b-line" marker-start="url(#arrow-start)" marker-end="url(#arrow-end)" />
              <text id="dim-b-text" text-anchor="start" stroke="none">b</text>
            </g>
            <g class="dim-group" data-title="Countersink Angle: Typically 90 degrees for standard screws.">
              <path id="dim-a-line" stroke="#dc3545" stroke-width="2" marker-start="url(#arrow-start)" marker-end="url(#arrow-end)" fill="none" />
              <text id="dim-a-text" text-anchor="middle" stroke="none">Angle</text>
            </g>
          </g>
        </g>
      </svg>
</template>

<script>
document.addEventListener('DOMContentLoaded', function() {
  const screwData912 = {
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
  const screwData7991 = {
    'M3': { P: 0.50, dk: 6.0, k: 1.7, s: 2.0, t: 1.2, e: 2.30, b: 12, angle: 90, d: 3.0, lengths: [6, 8, 10, 12, 14, 16, 18, 20, 22, 25, 30] },
    'M4': { P: 0.70, dk: 8.0, k: 2.3, s: 2.5, t: 1.8, e: 2.87, b: 14, angle: 90, d: 4.0, lengths: [8, 10, 12, 14, 16, 18, 20, 22, 25, 30, 35, 40] },
    'M5': { P: 0.80, dk: 10.0, k: 2.8, s: 3.0, t: 2.3, e: 3.44, b: 16, angle: 90, d: 5.0, lengths: [10, 12, 14, 16, 18, 20, 22, 25, 30, 35, 40, 45, 50] },
    'M6': { P: 1.00, dk: 12.0, k: 3.3, s: 4.0, t: 2.5, e: 4.58, b: 18, angle: 90, d: 6.0, lengths: [10, 12, 14, 16, 18, 20, 22, 25, 30, 35, 40, 45, 50, 55, 60] },
    'M8': { P: 1.25, dk: 16.0, k: 4.4, s: 5.0, t: 3.5, e: 5.72, b: 22, angle: 90, d: 8.0, lengths: [12, 14, 16, 18, 20, 22, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70] },
    'M10': { P: 1.50, dk: 20.0, k: 5.5, s: 6.0, t: 4.4, e: 6.86, b: 26, angle: 90, d: 10.0, lengths: [16, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80] },
    'M12': { P: 1.75, dk: 24.0, k: 6.5, s: 8.0, t: 4.6, e: 9.15, b: 30, angle: 90, d: 12.0, lengths: [20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 90, 100] }
  };

  const typeSelect = document.getElementById('screw-type');
  const sizeSelect = document.getElementById('screw-size');
  const lengthSelect = document.getElementById('screw-length');
  const svgContainer = document.getElementById('svg-container');

  function getTolerance912(dim, value) {
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


  function getTolerance7991(dim, value) {
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



  function updateDiagram912() {
    const data = screwData912[sizeSelect.value];
    const size = sizeSelect.value;
    const length = parseFloat(lengthSelect.value);
    
    // Update Tables
    document.getElementById('table-thread').innerHTML = `
      <tr><td>d (Nom.)</td><td>${data.d}</td><td>${getTolerance912('d', data.d)}</td></tr>
      <tr><td>P (Pitch)</td><td>${data.P}</td><td>-</td></tr>
      <tr><td>L (Len.)</td><td>${length}</td><td>${getTolerance912('L', length)}</td></tr>
      <tr><td>b (Thread)</td><td>${data.b}</td><td>min</td></tr>
    `;
    document.getElementById('table-head').innerHTML = `
      <tr><td>dk (Head)</td><td>${data.dk}</td><td>${getTolerance912('dk', data.dk)}</td></tr>
      <tr><td>k (Height)</td><td>${data.k}</td><td>${getTolerance912('k', data.k)}</td></tr>
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
    document.getElementById('dim-dk-text').textContent = `dk: ${data.dk} (${getTolerance912('dk', data.dk)})`;

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
    document.getElementById('dim-k-text').textContent = `k: ${data.k} (${getTolerance912('k', data.k)})`;

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
    document.getElementById('dim-L-text').textContent = `L: ${length} (${getTolerance912('L', length)})`;

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

  function updateDiagram7991() {
    const data = screwData7991[sizeSelect.value];
    const size = sizeSelect.value;
    const length = parseFloat(lengthSelect.value);
    
    // Update Tables
    document.getElementById('table-thread').innerHTML = `
      <tr><td>d (Nom.)</td><td>${data.d}</td><td>${getTolerance7991('d', data.d)}</td></tr>
      <tr><td>P (Pitch)</td><td>${data.P}</td><td>-</td></tr>
      <tr><td>L (Len.)</td><td>${length}</td><td>${getTolerance7991('L', length)}</td></tr>
      <tr><td>b (Thread)</td><td>${data.b}</td><td>min</td></tr>
    `;
    document.getElementById('table-head').innerHTML = `
      <tr><td>dk (Head)</td><td>${data.dk}</td><td>${getTolerance7991('dk', data.dk)}</td></tr>
      <tr><td>k (Height)</td><td>${data.k}</td><td>${getTolerance7991('k', data.k)}</td></tr>
      <tr><td>Angle</td><td>${data.angle}°</td><td>-</td></tr>
    `;
    document.getElementById('table-socket').innerHTML = `
      <tr><td>s (Socket)</td><td>${data.s}</td><td>-</td></tr>
      <tr><td>e (Corners)</td><td>${data.e}</td><td>min</td></tr>
      <tr><td>t (Depth)</td><td>${data.t}</td><td>min</td></tr>
    `;

    // Static geometry base dimensions for the diagram (scales to look roughly like M3)
    const startX = 450;
    const startY = 80;
    const visHeadW = 180; 
    const visShankW = 70; 
    
    // Countersunk Head Logic with vertical rim (dk section)
    const rimHeight = 12; 
    const taperHeight = (visHeadW - visShankW) / 2; // 90 degree taper
    const visHeadH = rimHeight + taperHeight;
    
    const visShankH = 260;
    const visSocketW = 60;
    const visSocketH = 35;
    const chamferH = 12;
    
    // Points for 6-point polygon
    const headPoints = `
      ${startX - visHeadW/2},${startY} 
      ${startX + visHeadW/2},${startY} 
      ${startX + visHeadW/2},${startY + rimHeight}
      ${startX + visShankW/2},${startY + visHeadH}
      ${startX - visShankW/2},${startY + visHeadH}
      ${startX - visHeadW/2},${startY + rimHeight}
    `.trim();
    document.getElementById('svg-head').setAttribute('points', headPoints);

    document.getElementById('svg-shank').setAttribute('x', startX - visShankW/2);
    document.getElementById('svg-shank').setAttribute('y', startY + visHeadH);
    document.getElementById('svg-shank').setAttribute('width', visShankW);
    document.getElementById('svg-shank').setAttribute('height', visShankH);

    document.getElementById('svg-socket').setAttribute('x', startX - visSocketW/2);
    document.getElementById('svg-socket').setAttribute('y', startY);
    document.getElementById('svg-socket').setAttribute('width', visSocketW);
    document.getElementById('svg-socket').setAttribute('height', visSocketH);

    const isFullyThreaded = length <= data.b;
    const visThreadStart = 100;
    const threadY = isFullyThreaded ? (startY + visHeadH + 10) : (startY + visHeadH + visThreadStart);
    const endY = startY + visHeadH + visShankH;
    const totalBottomY = endY + chamferH;

    document.getElementById('svg-threads').setAttribute('d', `M ${startX - visShankW/2 + 5} ${threadY} L ${startX - visShankW/2 + 5} ${endY} M ${startX + visShankW/2 - 5} ${threadY} L ${startX + visShankW/2 - 5} ${endY}`);
    document.getElementById('svg-chamfer').setAttribute('d', `M ${startX - visShankW/2} ${endY} L ${startX - visShankW/2 + 7} ${totalBottomY} L ${startX + visShankW/2 - 7} ${totalBottomY} L ${startX + visShankW/2} ${endY} Z`);

    // Top view static dims
    const top_e = 90;
    const top_s = 78;
    document.getElementById('top-outer').setAttribute('r', visHeadW/2);
    document.getElementById('top-inner').setAttribute('r', visShankW/2);
    
    document.getElementById('top-dim-s-text').textContent = `s: ${data.s}`;
    document.getElementById('top-dim-e-text').textContent = `e: ${data.e} (min)`;

    const ext = 10;
    const T_off = 45;
    document.getElementById('ext-dk-left').setAttribute('x1', startX - visHeadW/2); document.getElementById('ext-dk-left').setAttribute('y1', startY);
    document.getElementById('ext-dk-left').setAttribute('x2', startX - visHeadW/2); document.getElementById('ext-dk-left').setAttribute('y2', startY - T_off - ext);
    document.getElementById('ext-dk-right').setAttribute('x1', startX + visHeadW/2); document.getElementById('ext-dk-right').setAttribute('y1', startY);
    document.getElementById('ext-dk-right').setAttribute('x2', startX + visHeadW/2); document.getElementById('ext-dk-right').setAttribute('y2', startY - T_off - ext);
    document.getElementById('dim-dk-line').setAttribute('x1', startX - visHeadW/2); document.getElementById('dim-dk-line').setAttribute('y1', startY - T_off);
    document.getElementById('dim-dk-line').setAttribute('x2', startX + visHeadW/2); document.getElementById('dim-dk-line').setAttribute('y2', startY - T_off);
    document.getElementById('dim-dk-text').setAttribute('x', startX); document.getElementById('dim-dk-text').setAttribute('y', startY - T_off - 12);
    document.getElementById('dim-dk-text').textContent = `dk: ${data.dk} (${getTolerance7991('dk', data.dk)})`;

    const B_off = 55;
    document.getElementById('ext-d-left').setAttribute('x1', startX - visShankW/2); document.getElementById('ext-d-left').setAttribute('y1', totalBottomY);
    document.getElementById('ext-d-left').setAttribute('x2', startX - visShankW/2); document.getElementById('ext-d-left').setAttribute('y2', totalBottomY + B_off + ext);
    document.getElementById('ext-d-right').setAttribute('x1', startX + visShankW/2); document.getElementById('ext-d-right').setAttribute('y1', totalBottomY);
    document.getElementById('ext-d-right').setAttribute('x2', startX + visShankW/2); document.getElementById('ext-d-right').setAttribute('y2', totalBottomY + B_off + ext);
    document.getElementById('dim-d-line').setAttribute('x1', startX - visShankW/2); document.getElementById('dim-d-line').setAttribute('y1', totalBottomY + B_off);
    document.getElementById('dim-d-line').setAttribute('x2', startX + visShankW/2); document.getElementById('dim-d-line').setAttribute('y2', totalBottomY + B_off);
    document.getElementById('dim-d-text').setAttribute('x', startX); document.getElementById('dim-d-text').setAttribute('y', totalBottomY + B_off + 28);
    document.getElementById('dim-d-text').textContent = `d: ${data.d}`;

    const side_dist = 60; 
    document.getElementById('ext-k-top').setAttribute('x1', startX + visHeadW/2); document.getElementById('ext-k-top').setAttribute('y1', startY);
    document.getElementById('ext-k-top').setAttribute('x2', startX + visHeadW/2 + side_dist + ext); document.getElementById('ext-k-top').setAttribute('y2', startY);
    document.getElementById('ext-k-bottom').setAttribute('x1', startX + visShankW/2); document.getElementById('ext-k-bottom').setAttribute('y1', startY + visHeadH);
    document.getElementById('ext-k-bottom').setAttribute('x2', startX + visHeadW/2 + side_dist + ext); document.getElementById('ext-k-bottom').setAttribute('y2', startY + visHeadH);
    document.getElementById('dim-k-line').setAttribute('x1', startX + visHeadW/2 + side_dist); document.getElementById('dim-k-line').setAttribute('y1', startY);
    document.getElementById('dim-k-line').setAttribute('x2', startX + visHeadW/2 + side_dist); document.getElementById('dim-k-line').setAttribute('y2', startY + visHeadH);
    document.getElementById('dim-k-text').setAttribute('x', startX + visHeadW/2 + side_dist + 12); document.getElementById('dim-k-text').setAttribute('y', startY + visHeadH/2 + 5);
    document.getElementById('dim-k-text').textContent = `k: ${data.k} (${getTolerance7991('k', data.k)})`;

    const L_dist = 180; 
    document.getElementById('ext-L-top').setAttribute('x1', startX + visHeadW/2 + side_dist); document.getElementById('ext-L-top').setAttribute('y1', startY);
    document.getElementById('ext-L-top').setAttribute('x2', startX + visHeadW/2 + L_dist + ext); document.getElementById('ext-L-top').setAttribute('y2', startY);
    document.getElementById('ext-L-bottom').setAttribute('x1', startX + visShankW/2); document.getElementById('ext-L-bottom').setAttribute('y1', totalBottomY);
    document.getElementById('ext-L-bottom').setAttribute('x2', startX + visHeadW/2 + L_dist + ext); document.getElementById('ext-L-bottom').setAttribute('y2', totalBottomY);
    document.getElementById('dim-L-line').setAttribute('x1', startX + visHeadW/2 + L_dist); document.getElementById('dim-L-line').setAttribute('y1', startY);
    document.getElementById('dim-L-line').setAttribute('x2', startX + visHeadW/2 + L_dist); document.getElementById('dim-L-line').setAttribute('y2', totalBottomY);
    document.getElementById('dim-L-text').setAttribute('x', startX + visHeadW/2 + L_dist + 12); document.getElementById('dim-L-text').setAttribute('y', startY + (totalBottomY - startY)/2 + 5);
    document.getElementById('dim-L-text').textContent = `L: ${length} (${getTolerance7991('L', length)})`;

    const bGroupIds = ['ext-b-top', 'ext-b-bottom', 'dim-b-line', 'dim-b-text'];
    bGroupIds.forEach(id => { document.getElementById(id).style.display = isFullyThreaded ? 'none' : 'block'; });
    if (!isFullyThreaded) {
      document.getElementById('ext-b-top').setAttribute('x1', startX + visShankW/2); document.getElementById('ext-b-top').setAttribute('y1', threadY);
      document.getElementById('ext-b-top').setAttribute('x2', startX + visHeadW/2 + side_dist + ext); document.getElementById('ext-b-top').setAttribute('y2', threadY);
      document.getElementById('ext-b-bottom').setAttribute('x1', startX + visShankW/2); document.getElementById('ext-b-bottom').setAttribute('y1', totalBottomY);
      document.getElementById('ext-b-bottom').setAttribute('x2', startX + visHeadW/2 + side_dist + ext); document.getElementById('ext-b-bottom').setAttribute('y2', totalBottomY);
      document.getElementById('dim-b-line').setAttribute('x1', startX + visHeadW/2 + side_dist); document.getElementById('dim-b-line').setAttribute('y1', threadY);
      document.getElementById('dim-b-line').setAttribute('x2', startX + visHeadW/2 + side_dist); document.getElementById('dim-b-line').setAttribute('y2', totalBottomY);
      document.getElementById('dim-b-text').setAttribute('x', startX + visHeadW/2 + side_dist + 12); document.getElementById('dim-b-text').setAttribute('y', threadY + (totalBottomY - threadY)/2 + 5);
      document.getElementById('dim-b-text').textContent = `b: ${data.b} (min)`;
    }

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
    document.getElementById('dim-t-text').setAttribute('x', t_x - 12); document.getElementById('dim-t-text').setAttribute('y', startY + visSocketH/2 + 5);
    document.getElementById('dim-t-text').textContent = `t: ${data.t} (min)`;

    const midX = startX - visHeadW/4 - visShankW/4;
    const midY = startY + rimHeight/2 + visHeadH/2;
    
    document.getElementById('ext-a-left').style.display = 'none';
    document.getElementById('ext-a-right').style.display = 'none';
    document.getElementById('dim-a-line').style.display = 'none';

    document.getElementById('dim-a-text').setAttribute('x', midX - 25); 
    document.getElementById('dim-a-text').setAttribute('y', midY + 15);
    document.getElementById('dim-a-text').textContent = `${data.angle}°`;
  }
  

  function bindTooltips() {
    const tooltip = document.getElementById('custom-tooltip');
    const dimGroups = document.querySelectorAll('.dim-group');
    
    dimGroups.forEach(group => {
      group.addEventListener('mouseenter', (e) => {
        const titleText = group.getAttribute('data-title');
        tooltip.textContent = titleText;
        tooltip.style.display = 'block';
      });
      
      group.addEventListener('mousemove', (e) => {
        tooltip.style.left = (e.clientX + 15) + 'px';
        tooltip.style.top = (e.clientY + 15) + 'px';
      });
      
      group.addEventListener('mouseleave', () => {
        tooltip.style.display = 'none';
      });
    });
  }

  function updateType() {
    const type = typeSelect.value;
    svgContainer.innerHTML = document.getElementById('svg-template-' + type.replace('din', '')).innerHTML;
    
    const dataObj = type === 'din912' ? screwData912 : screwData7991;
    sizeSelect.innerHTML = '';
    Object.keys(dataObj).forEach(size => {
      const option = document.createElement('option');
      option.value = size;
      option.textContent = size;
      sizeSelect.appendChild(option);
    });
    
    // Select default sizes (M3 for 912, M6 for 7991)
    if(type === 'din912') sizeSelect.value = 'M3';
    if(type === 'din7991') sizeSelect.value = 'M6';
    
    bindTooltips();
    populateLengths();
  }

  function populateLengths() {
    const type = typeSelect.value;
    const size = sizeSelect.value;
    const dataObj = type === 'din912' ? screwData912 : screwData7991;
    const data = dataObj[size];
    
    lengthSelect.innerHTML = '';
    data.lengths.forEach(l => {
      const option = document.createElement('option');
      option.value = l;
      option.textContent = l + ' mm';
      
      let defaultLen = type === 'din912' ? 12 : 20;
      if (l === defaultLen || (l > defaultLen && !Array.from(lengthSelect.options).some(o => o.value == defaultLen))) {
         option.selected = true;
      }
      lengthSelect.appendChild(option);
    });
    if (lengthSelect.selectedIndex === -1) { lengthSelect.selectedIndex = 0; }
    
    if (type === 'din912') { updateDiagram912(); } else { updateDiagram7991(); }
  }

  typeSelect.addEventListener('change', updateType);
  sizeSelect.addEventListener('change', populateLengths);
  lengthSelect.addEventListener('change', () => {
    if (typeSelect.value === 'din912') updateDiagram912(); else updateDiagram7991();
  });
  
  // Initial setup
  updateType();
});
</script>

## Standard References
- **DIN 912 (ISO 4762)**: Hexagon socket head cap screws.
- **DIN 7991 (ISO 10642)**: Hexagon socket countersunk head cap screws.
- **Mechanical Properties**: Available in classes 8.8, 10.9, 12.9.
- **da**: Maximum transition diameter under head (DIN 912).
- **e**: Minimum width across corners of hex socket.
- **b**: Minimum thread length. Screws are fully threaded if $L \le b$.

---
*Note: Dimensions are for reference only. Always consult official DIN/ISO standards for critical engineering applications.*
