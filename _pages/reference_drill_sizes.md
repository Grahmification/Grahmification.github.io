---
title: Tap and Clearance Drill Sizes
layout: page
permalink: /reference/engineering/drill-sizes/
dynamic_title: true
---

This tool provides standard tap drill and clearance drill sizes for common metric threads.

<div class="card p-4 shadow-sm mb-4 mt-4">
  <div class="row">
    <div class="col-md-6 mb-3">
      <label for="screw-size" class="font-weight-bold">Select Screw Size:</label>
      <select id="screw-size" class="form-control form-control-lg">
        <!-- Options populated by JS -->
      </select>
    </div>
  </div>

  <div class="table-responsive mt-3">
    <table class="table table-bordered text-center align-middle" style="font-size: 0.9rem;">
      <thead class="thead-dark">
        <tr>
          <th rowspan="2" class="align-middle">Thread Pitch<br><small class="font-weight-normal">(mm)</small></th>
          <th colspan="2" class="align-middle border-bottom-0" style="background-color: #0d6efd; color: white;">75% Thread Tap Drill<br><small class="font-weight-normal">(Aluminum, Brass, Plastics)</small></th>
          <th colspan="2" class="align-middle border-bottom-0" style="background-color: #198754; color: white;">50% Thread Tap Drill<br><small class="font-weight-normal">(Steel, Stainless, Iron)</small></th>
          <th colspan="4" class="align-middle border-bottom-0" style="background-color: #6c757d; color: white;">Clearance Drill</th>
        </tr>
        <tr>
          <th style="background-color: #0d6efd; color: white;">Size (mm)</th>
          <th style="background-color: #0d6efd; color: white;">Closest American</th>
          <th style="background-color: #198754; color: white;">Size (mm)</th>
          <th style="background-color: #198754; color: white;">Closest American</th>
          <th style="background-color: #6c757d; color: white;">Close Fit (mm)</th>
          <th style="background-color: #6c757d; color: white;">Close American</th>
          <th style="background-color: #6c757d; color: white;">Standard Fit (mm)</th>
          <th style="background-color: #6c757d; color: white;">Standard American</th>
        </tr>
      </thead>
      <tbody id="table-body">
        <!-- Rows populated by JS -->
      </tbody>
    </table>
  </div>
  <small class="text-muted mt-2 d-block">* indicates a non-standard or fine thread pitch</small>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  const rawData = [
  {"tapSize": "M1.5x0.35", "75_metric": "1.15", "75_amer": "56", "50_metric": "1.25", "50_amer": "55", "close_metric": "1.60", "close_amer": "1/16", "std_metric": "1.65", "std_amer": "52"},
  {"tapSize": "M1.6x0.35", "75_metric": "1.25", "75_amer": "55", "50_metric": "1.35", "50_amer": "54", "close_metric": "1.70", "close_amer": "51", "std_metric": "1.75", "std_amer": "50"},
  {"tapSize": "M1.8x0.35", "75_metric": "1.45", "75_amer": "53", "50_metric": "1.55", "50_amer": "1/16", "close_metric": "1.90", "close_amer": "49", "std_metric": "2.00", "std_amer": "5/64"},
  {"tapSize": "M2x0.45", "75_metric": "1.55", "75_amer": "1/16", "50_metric": "1.70", "50_amer": "51", "close_metric": "2.10", "close_amer": "45", "std_metric": "2.20", "std_amer": "44"},
  {"tapSize": "M2x0.40", "75_metric": "1.60", "75_amer": "52", "50_metric": "1.75", "50_amer": "50", "close_metric": "2.10", "close_amer": "45", "std_metric": "2.20", "std_amer": "44"},
  {"tapSize": "M2.2x0.45", "75_metric": "1.75", "75_amer": "50", "50_metric": "1.90", "50_amer": "48", "close_metric": "2.30", "close_amer": "3/32", "std_metric": "2.40", "std_amer": "41"},
  {"tapSize": "M2.5x0.45", "75_metric": "2.05", "75_amer": "46", "50_metric": "2.20", "50_amer": "44", "close_metric": "2.65", "close_amer": "37", "std_metric": "2.75", "std_amer": "7/64"},
  {"tapSize": "M3x0.60", "75_metric": "2.40", "75_amer": "41", "50_metric": "2.60", "50_amer": "37", "close_metric": "3.15", "close_amer": "1/8", "std_metric": "3.30", "std_amer": "30"},
  {"tapSize": "M3x0.50", "75_metric": "2.50", "75_amer": "39", "50_metric": "2.70", "50_amer": "36", "close_metric": "3.15", "close_amer": "1/8", "std_metric": "3.30", "std_amer": "30"},
  {"tapSize": "M3.5x0.60", "75_metric": "2.90", "75_amer": "32", "50_metric": "3.10", "50_amer": "31", "close_metric": "3.70", "close_amer": "27", "std_metric": "3.85", "std_amer": "24"},
  {"tapSize": "M4x0.75", "75_metric": "3.25", "75_amer": "30", "50_metric": "3.50", "50_amer": "28", "close_metric": "4.20", "close_amer": "19", "std_metric": "4.40", "std_amer": "17"},
  {"tapSize": "M4x0.70", "75_metric": "3.30", "75_amer": "30", "50_metric": "3.50", "50_amer": "28", "close_metric": "4.20", "close_amer": "19", "std_metric": "4.40", "std_amer": "17"},
  {"tapSize": "M4.5x0.75", "75_metric": "3.75", "75_amer": "25", "50_metric": "4.00", "50_amer": "22", "close_metric": "4.75", "close_amer": "13", "std_metric": "5.00", "std_amer": "9"},
  {"tapSize": "M5x1.00", "75_metric": "4.00", "75_amer": "21", "50_metric": "4.40", "50_amer": "11/64", "close_metric": "5.25", "close_amer": "5", "std_metric": "5.50", "std_amer": "7/32"},
  {"tapSize": "M5x0.90", "75_metric": "4.10", "75_amer": "20", "50_metric": "4.40", "50_amer": "17", "close_metric": "5.25", "close_amer": "5", "std_metric": "5.50", "std_amer": "7/32"},
  {"tapSize": "M5x0.80", "75_metric": "4.20", "75_amer": "19", "50_metric": "4.50", "50_amer": "16", "close_metric": "5.25", "close_amer": "5", "std_metric": "5.50", "std_amer": "7/32"},
  {"tapSize": "M5.5x0.90", "75_metric": "4.60", "75_amer": "14", "50_metric": "4.90", "50_amer": "10", "close_metric": "5.80", "close_amer": "1", "std_metric": "6.10", "std_amer": "B"},
  {"tapSize": "M6x1.00", "75_metric": "5.00", "75_amer": "8", "50_metric": "5.40", "50_amer": "4", "close_metric": "6.30", "close_amer": "E", "std_metric": "6.60", "std_amer": "G"},
  {"tapSize": "M6x0.75", "75_metric": "5.25", "75_amer": "4", "50_metric": "5.50", "50_amer": "7/32", "close_metric": "6.30", "close_amer": "E", "std_metric": "6.60", "std_amer": "G"},
  {"tapSize": "M7x1.00", "75_metric": "6.00", "75_amer": "B", "50_metric": "6.40", "50_amer": "E", "close_metric": "7.40", "close_amer": "L", "std_metric": "7.70", "std_amer": "N"},
  {"tapSize": "M7x0.75", "75_metric": "6.25", "75_amer": "D", "50_metric": "6.50", "50_amer": "F", "close_metric": "7.40", "close_amer": "L", "std_metric": "7.70", "std_amer": "N"},
  {"tapSize": "M8x1.25", "75_metric": "6.80", "75_amer": "H", "50_metric": "7.20", "50_amer": "J", "close_metric": "8.40", "close_amer": "Q", "std_metric": "8.80", "std_amer": "S"},
  {"tapSize": "M8x1.00", "75_metric": "7.00", "75_amer": "J", "50_metric": "7.40", "50_amer": "L", "close_metric": "8.40", "close_amer": "Q", "std_metric": "8.80", "std_amer": "S"},
  {"tapSize": "M9x1.25", "75_metric": "7.80", "75_amer": "N", "50_metric": "8.20", "50_amer": "P", "close_metric": "9.50", "close_amer": "3/8", "std_metric": "9.90", "std_amer": "25/64"},
  {"tapSize": "M9x1.00", "75_metric": "8.00", "75_amer": "O", "50_metric": "8.40", "50_amer": "21/64", "close_metric": "9.50", "close_amer": "3/8", "std_metric": "9.90", "std_amer": "25/64"},
  {"tapSize": "M10x1.50", "75_metric": "8.50", "75_amer": "R", "50_metric": "9.00", "50_amer": "T", "close_metric": "10.50", "close_amer": "Z", "std_metric": "11.00", "std_amer": "7/16"},
  {"tapSize": "M10x1.25", "75_metric": "8.80", "75_amer": "11/32", "50_metric": "9.20", "50_amer": "23/64", "close_metric": "10.50", "close_amer": "Z", "std_metric": "11.00", "std_amer": "7/16"},
  {"tapSize": "M10x1.00", "75_metric": "9.00", "75_amer": "T", "50_metric": "9.40", "50_amer": "U", "close_metric": "10.50", "close_amer": "Z", "std_metric": "11.00", "std_amer": "7/16"},
  {"tapSize": "M11x1.50", "75_metric": "9.50", "75_amer": "3/8", "50_metric": "10.00", "50_amer": "X", "close_metric": "11.60", "close_amer": "29/64", "std_metric": "12.10", "std_amer": "15/32"},
  {"tapSize": "M12x1.75", "75_metric": "10.30", "75_amer": "13/32", "50_metric": "10.90", "50_amer": "27/64", "close_metric": "12.60", "close_amer": "1/2", "std_metric": "13.20", "std_amer": "33/64"},
  {"tapSize": "M12x1.50", "75_metric": "10.50", "75_amer": "Z", "50_metric": "11.00", "50_amer": "7/16", "close_metric": "12.60", "close_amer": "1/2", "std_metric": "13.20", "std_amer": "33/64"},
  {"tapSize": "M12x1.25", "75_metric": "10.80", "75_amer": "27/64", "50_metric": "11.20", "50_amer": "7/16", "close_metric": "12.60", "close_amer": "1/2", "std_metric": "13.20", "std_amer": "33/64"},
  {"tapSize": "M14x2.00", "75_metric": "12.10", "75_amer": "15/32", "50_metric": "12.70", "50_amer": "1/2", "close_metric": "14.75", "close_amer": "37/64", "std_metric": "15.50", "std_amer": "39/64"},
  {"tapSize": "M14x1.50", "75_metric": "12.50", "75_amer": "1/2", "50_metric": "13.00", "50_amer": "33/64", "close_metric": "14.75", "close_amer": "37/64", "std_metric": "15.50", "std_amer": "39/64"},
  {"tapSize": "M14x1.25", "75_metric": "12.80", "75_amer": "1/2", "50_metric": "13.20", "50_amer": "33/64", "close_metric": "14.75", "close_amer": "37/64", "std_metric": "15.50", "std_amer": "39/64"},
  {"tapSize": "M15x1.50", "75_metric": "13.50", "75_amer": "17/32", "50_metric": "14.00", "50_amer": "35/64", "close_metric": "15.75", "close_amer": "5/8", "std_metric": "16.50", "std_amer": "21/32"},
  {"tapSize": "M16x2.00", "75_metric": "14.00", "75_amer": "35/64", "50_metric": "14.75", "50_amer": "37/64", "close_metric": "16.75", "close_amer": "21/32", "std_metric": "17.50", "std_amer": "11/16"},
  {"tapSize": "M16x1.50", "75_metric": "14.50", "75_amer": "37/64", "50_metric": "15.00", "50_amer": "19/32", "close_metric": "16.75", "close_amer": "21/32", "std_metric": "17.50", "std_amer": "11/16"},
  {"tapSize": "M17x1.50", "75_metric": "15.50", "75_amer": "39/64", "50_metric": "16.00", "50_amer": "5/8", "close_metric": "18.00", "close_amer": "45/64", "std_metric": "18.50", "std_amer": "47/64"},
  {"tapSize": "M18x2.50", "75_metric": "15.50", "75_amer": "39/64", "50_metric": "16.50", "50_amer": "41/64", "close_metric": "19.00", "close_amer": "3/4", "std_metric": "20.00", "std_amer": "25/32"},
  {"tapSize": "M18x2.00", "75_metric": "16.00", "75_amer": "5/8", "50_metric": "16.75", "50_amer": "21/32", "close_metric": "19.00", "close_amer": "3/4", "std_metric": "20.00", "std_amer": "25/32"},
  {"tapSize": "M18x1.50", "75_metric": "16.50", "75_amer": "21/32", "50_metric": "17.00", "50_amer": "43/64", "close_metric": "19.00", "close_amer": "3/4", "std_metric": "20.00", "std_amer": "25/32"},
  {"tapSize": "M19x2.50", "75_metric": "16.50", "75_amer": "21/32", "50_metric": "17.50", "50_amer": "11/16", "close_metric": "20.00", "close_amer": "25/32", "std_metric": "21.00", "std_amer": "53/64"},
  {"tapSize": "M20x2.50", "75_metric": "17.50", "75_amer": "11/16", "50_metric": "18.50", "50_amer": "23/32", "close_metric": "21.00", "close_amer": "53/64", "std_metric": "22.00", "std_amer": "55/64"},
  {"tapSize": "M20x2.00", "75_metric": "18.00", "75_amer": "45/64", "50_metric": "18.50", "50_amer": "47/64", "close_metric": "21.00", "close_amer": "53/64", "std_metric": "22.00", "std_amer": "55/64"},
  {"tapSize": "M20x1.50", "75_metric": "18.50", "75_amer": "47/64", "50_metric": "19.00", "50_amer": "3/4", "close_metric": "21.00", "close_amer": "53/64", "std_metric": "22.00", "std_amer": "55/64"}
  ];

  const tapDrillData = {};
  rawData.forEach(row => {
    const parts = row.tapSize.split('x');
    const size = parts[0];
    const pitch = parts[1] || '';
    if (!tapDrillData[size]) tapDrillData[size] = [];
    tapDrillData[size].push({
      pitch: pitch,
      ...row
    });
  });

  const sizeSelect = document.getElementById('screw-size');
  const tableBody = document.getElementById('table-body');

  // Populate dropdown
  Object.keys(tapDrillData).forEach(size => {
    const option = document.createElement('option');
    option.value = size;
    option.textContent = size;
    sizeSelect.appendChild(option);
  });

  const standardPitches = {
    "M1.5": "0.35", "M1.6": "0.35", "M1.8": "0.35",
    "M2": "0.40", "M2.2": "0.45", "M2.5": "0.45",
    "M3": "0.50", "M3.5": "0.60", "M4": "0.70",
    "M4.5": "0.75", "M5": "0.80", "M5.5": "0.90",
    "M6": "1.00", "M7": "1.00", "M8": "1.25",
    "M9": "1.25", "M10": "1.50", "M11": "1.50",
    "M12": "1.75", "M14": "2.00", "M15": "1.50",
    "M16": "2.00", "M17": "1.50", "M18": "2.50",
    "M19": "2.50", "M20": "2.50"
  };

  function updateTable() {
    const size = sizeSelect.value;
    const data = tapDrillData[size];
    
    tableBody.innerHTML = '';
    const rowCount = data.length;
    data.forEach((row, index) => {
      const tr = document.createElement('tr');
      tr.style.color = "#4b4f5cff"; // Darker text color
      tr.style.fontWeight = "500";
      
      let displayPitch = row.pitch;
      if (standardPitches[size] && row.pitch !== standardPitches[size]) {
        displayPitch += '*';
      }
      
      let html = `
        <td class="font-weight-bold">${displayPitch}</td>
        <td>${row['75_metric']}</td>
        <td>${row['75_amer']}</td>
        <td>${row['50_metric']}</td>
        <td>${row['50_amer']}</td>
      `;

      if (index === 0) {
        html += `
        <td rowspan="${rowCount}" class="align-middle">${row['close_metric']}</td>
        <td rowspan="${rowCount}" class="align-middle">${row['close_amer']}</td>
        <td rowspan="${rowCount}" class="align-middle">${row['std_metric']}</td>
        <td rowspan="${rowCount}" class="align-middle">${row['std_amer']}</td>
        `;
      }
      
      tr.innerHTML = html;
      tableBody.appendChild(tr);
    });
  }

  sizeSelect.addEventListener('change', updateTable);
  
  // Set default to M5
  sizeSelect.value = 'M5';
  updateTable();
});
</script>
