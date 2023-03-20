var ctx = document.getElementById('site-chart').getContext('2d');
const chartData = {{chart_data|safe}};
const colors = [
  '#FFB3BA',
  '#FFDFBA',
  '#FFFFBA',
  '#BAFFC9',
  '#BAE1FF',
  '#CBA5FF',
  '#FFC6E7',
  '#BAA5FF',
  '#BAFFFA',
  '#FFE1BA'
];
var backgroundColors = [];
for (var i = 0; i < chartData.labels.length; i++) {
    var colorIndex = Math.floor(Math.random() * colors.length);
    backgroundColors.push(colors[colorIndex]);
}
var chart = new Chart(ctx, {
type: 'doughnut',
data: {
labels: chartData.labels,
datasets: [{
    label: 'Site Counts',
    data: chartData.data,
    backgroundColor: backgroundColors,
    borderColor: 'white',
    borderWidth: 1
}]
},
options: {
rotation: -0.5 * Math.PI,
animation: {
    animateScale: true,
    animateRotate: true
},
cutoutPercentage: 70, // Adjust this value to change the size of the inner circle
tooltips: {
    enabled: false
},
plugins: {
    // Show labels inside the doughnut chart segments
    datalabels: {
        color: 'white',
        font: {
            size: '18'
        },
        formatter: function(value, context) {
            return context.chart.data.labels[context.dataIndex];
        }
    }
}
}
});