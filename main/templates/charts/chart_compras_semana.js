const config = {
    type: 'bar',
    data: {
        datasets:[{
            data:{{ data_compras|safe }},
            backgroundColor: ['rgba(255, 99, 132, 0.2)','rgba(255, 159, 64, 0.2)','rgba(255, 205, 86, 0.2)','rgba(75, 192, 192, 0.2)','rgba(54, 162, 235, 0.2)'],
            borderColor: ['rgb(255, 99, 132)','rgb(255, 159, 64)','rgb(255, 205, 86)','rgb(75, 192, 192)','rgb(54, 162, 235)'],
            label:'stock',
            borderWidth:1
        }],
        labels: {{ labels_compras|safe }}
    },
    options: {
        scales:{
            yAxes:[{
                ticks: {
                    beginAtZero: true
                }
            }],
        },
        responsive: true,
        plugins: {
            legend: {
                position: 'top',
            },
            title: {
            display: true,
            text: 'Grafica de compras semanales'
            }
        }
    },
};

var comprasChart = new Chart($('#compras_canvas'),config)
