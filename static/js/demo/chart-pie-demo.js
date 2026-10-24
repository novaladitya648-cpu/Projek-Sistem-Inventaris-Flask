// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = 'Nunito', '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#858796';

// Pie Chart Kategori Inventaris
// Label dan jumlah dikirim dari Flask (jumlah JENIS barang per kategori)
let labelKategori = window.labelKategori || [];
let dataKategori = window.dataKategori || [];

// Palet warna bawaan template; diulang jika kategori lebih banyak dari warna
const warnaKategori = ['#4e73df', '#1cc88a', '#36b9cc', '#f6c23e', '#e74a3b', '#858796', '#5a5c69', '#fd7e14'];
const warnaHoverKategori = ['#2e59d9', '#17a673', '#2c9faf', '#dda20a', '#c0392b', '#6b6d7d', '#3d3e47', '#d96a02'];

let ctxPie = document.getElementById("myPieChart");
let myPieChart = new Chart(ctxPie, {
  type: 'doughnut',
  data: {
    labels: labelKategori,
    datasets: [{
      data: dataKategori,
      backgroundColor: labelKategori.map(function (_, i) { return warnaKategori[i % warnaKategori.length]; }),
      hoverBackgroundColor: labelKategori.map(function (_, i) { return warnaHoverKategori[i % warnaHoverKategori.length]; }),
      hoverBorderColor: "rgba(234, 236, 244, 1)",
    }],
  },
  options: {
    maintainAspectRatio: false,
    tooltips: {
      backgroundColor: "rgb(255,255,255)",
      bodyFontColor: "#858796",
      borderColor: '#dddfeb',
      borderWidth: 1,
      xPadding: 15,
      yPadding: 15,
      displayColors: false,
      caretPadding: 10,
      callbacks: {
        label: function (tooltipItem, data) {
          let nama = data.labels[tooltipItem.index] || '';
          let jumlah = data.datasets[tooltipItem.datasetIndex].data[tooltipItem.index];
          return nama + ': ' + jumlah + ' jenis barang';
        }
      }
    },
    legend: {
      display: true,
      position: 'bottom'
    },
    cutoutPercentage: 80,
  }
});