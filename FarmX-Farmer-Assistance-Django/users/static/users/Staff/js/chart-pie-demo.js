// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#292b2c';

let cropData = [];
let cropLabels = [];

$.ajax({
  method: 'GET',
  url: '/crop/api-data/',
  success: function (data) {
          console.log(data);
          cropData = data.yields;
          cropLabels = data.crops;
          var ctx = document.getElementById("myPieChart");
          var myPieChart = new Chart(ctx, {
            type: 'pie',
            data: {
              labels: cropLabels,
              datasets: [{
                data: cropData,
                backgroundColor: [
                'rgba(255, 0, 0, 0.8)',
                'rgba(54, 162, 235, 0.8)',
                'rgba(255, 206, 86, 0.8)',
                'rgba(0, 0, 192, 0.8)',
                'rgba(153, 102, 255, 0.8)',
                'rgba(255, 159, 64, 0.8)'
            ],
            borderWidth: 1
              }],
            },
          });
  },
  error: function (error_data) {
          console.log('ERROR DATA');
          console.log(error_data)
  }
});

// Pie Chart Example

