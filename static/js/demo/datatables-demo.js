$(document).ready(function () {
  $('#dataTable').DataTable({
    "pageLength": 5,
    "lengthMenu": [5],
    "paging": true,
    "ordering": true,
    "info": true,
    "language": {
      "lengthMenu": "Tampilkan _MENU_ barang",
      "zeroRecords": "Barang tidak ditemukan",
      "info": "Menampilkan halaman _PAGE_ dari _PAGES_",
      "infoEmpty": "Tidak ada barang tersedia",
      "infoFiltered": "(difilter dari _MAX_ total barang)",
      "search": "Cari:",
      "paginate": {
        "first": "Pertama",
        "last": "Terakhir",
        "next": "Next",
        "previous": "Previous"
      }
    }
  });
});