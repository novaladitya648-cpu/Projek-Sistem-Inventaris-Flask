Chart.defaults.global.defaultFontFamily = 'Nunito', '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#858796';

function number_format(number, decimals, dec_point, thousands_sep) {
  number = (number + '').replace(',', '').replace(' ', '');
  let n = !isFinite(+number) ? 0 : +number,
    prec = !isFinite(+decimals) ? 0 : Math.abs(decimals),
    sep = (typeof thousands_sep === 'undefined') ? ',' : thousands_sep,
    dec = (typeof dec_point === 'undefined') ? '.' : dec_point,
    s = '',
    toFixedFix = function (n, prec) {
      let k = Math.pow(10, prec);
      return '' + Math.round(n * k) / k;
    };
  s = (prec ? toFixedFix(n, prec) : '' + Math.round(n)).split('.');
  if (s[0].length > 3) {
    s[0] = s[0].replace(/\B(?=(\d{3})+(?!\d))/g, sep);
  }
  if ((s[1] || '').length < prec) {
    s[1] = s[1] || '';
    s[1] += new Array(prec + 1 - s[1].length).join('0');
  }
  return s.join(dec);
}

// Area Chart - Grafik Keluar Masuk Barang (Agustus - Oktober 2026)
// Data dikirim dari Flask (index.html) lewat variabel window.*
let ctx = document.getElementById("myAreaChart");
let myLineChart = new Chart(ctx, {
  type: 'line',
  data: {
    labels: window.labelBulanGrafik || [],
    datasets: [
      {
        label: "Barang Masuk",
        lineTension: 0.3,
        backgroundColor: "rgba(78, 115, 223, 0.05)",
        borderColor: "rgba(78, 115, 223, 1)",
        pointRadius: 3,
        pointBackgroundColor: "rgba(78, 115, 223, 1)",
        pointBorderColor: "rgba(78, 115, 223, 1)",
        pointHoverRadius: 3,
        pointHoverBackgroundColor: "rgba(78, 115, 223, 1)",
        pointHoverBorderColor: "rgba(78, 115, 223, 1)",
        pointHitRadius: 10,
        pointBorderWidth: 2,
        data: window.grafikBarangMasuk || [],
      },
      {
        label: "Barang Keluar",
        lineTension: 0.3,
        backgroundColor: "rgba(28, 200, 138, 0.05)",
        borderColor: "rgba(28, 200, 138, 1)",
        pointRadius: 3,
        pointBackgroundColor: "rgba(28, 200, 138, 1)",
        pointBorderColor: "rgba(28, 200, 138, 1)",
        pointHoverRadius: 3,
        pointHoverBackgroundColor: "rgba(28, 200, 138, 1)",
        pointHoverBorderColor: "rgba(28, 200, 138, 1)",
        pointHitRadius: 10,
        pointBorderWidth: 2,
        data: window.grafikBarangKeluar || [],
      }
    ],
  },
  options: {
    maintainAspectRatio: false,
    layout: {
      padding: { left: 10, right: 25, top: 25, bottom: 0 }
    },
    scales: {
      xAxes: [{
        time: { unit: 'date' },
        gridLines: { display: false, drawBorder: false },
        ticks: { maxTicksLimit: 3 }
      }],
      yAxes: [{
        ticks: {
          beginAtZero: true,
          maxTicksLimit: 5,
          padding: 10,
          callback: function (value) {
            // Jumlah barang berupa bilangan bulat, jadi sembunyikan tick desimal
            if (Math.floor(value) !== value) {
              return null;
            }
            return number_format(value) + ' Unit';
          }
        },
        gridLines: {
          color: "rgb(234, 236, 244)",
          zeroLineColor: "rgb(234, 236, 244)",
          drawBorder: false,
          borderDash: [2],
          zeroLineBorderDash: [2]
        }
      }],
    },
    legend: { display: true },
    tooltips: {
      backgroundColor: "rgb(255,255,255)",
      bodyFontColor: "#858796",
      titleMarginBottom: 10,
      titleFontColor: '#6e707e',
      titleFontSize: 14,
      borderColor: '#dddfeb',
      borderWidth: 1,
      xPadding: 15,
      yPadding: 15,
      displayColors: true,
      intersect: false,
      mode: 'index',
      caretPadding: 10,
      callbacks: {
        label: function (tooltipItem, chart) {
          let datasetLabel = chart.datasets[tooltipItem.datasetIndex].label || '';
          return datasetLabel + ': ' + number_format(tooltipItem.yLabel) + ' Unit';
        }
      }
    }
  }
});