// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#292b2c';

// Bar Chart Example

let stateData = [];
let stateLabels = [];

$.ajax({
    method: 'GET',
    url: '/crop/api-data/',
    success: function (data) {
        console.log(data);
        stateData = data.land_area;
        stateLabels = data.states;
        const ctx = document.getElementById('myBarChart').getContext('2d');
        var myChart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: stateLabels,
        datasets: [{
            label: 'State wide cultivatable land',
            data: stateData,
            backgroundColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)'
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
            ],
            borderWidth: 1
        }]
    },
    options: {
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero: true
                }
            }]
        }
    }
});
    },

    error: function (error_data) {
        console.log('ERROR');
        console.log(error_data)
    }
})