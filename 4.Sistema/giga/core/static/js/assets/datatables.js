// Call the dataTables jQuery plugin
$(document).ready(function() {
  $('#dataTable').DataTable(
      {
           language: {
               url: 'https://cdn.datatables.net/plug-ins/1.10.25/i18n/Portuguese-Brasil.json'
           },
           responsive: true
       }
  );
});
