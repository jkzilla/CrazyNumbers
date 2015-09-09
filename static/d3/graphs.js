// Chart1
	var dateTime_array = []
	{% for item in date_time %}
	var dateTime = new Date({{ item|safe }})
	dateTime_array.push(dateTime)
	{% endfor %}
	console.log(dateTime_array)
	var number = {{ number }}

	var width = 400,
	barHeight = 20;

	var x = d3.scale.linear()
		.domain([0, d3.max(number)])
		.range([0, width]);

	// select the chart container using class selector
	var chart = d3.select(".chart1")
		.attr("width", width)
		.attr("height", barHeight * number.length);

	// initiate data join.
	var bar =  chart.selectAll("#chart1")
		.data(number)
		.enter().append(".chart1")
		.attr("transform", function(d, i) { return "translate(0," + barHeight + ")"; });

	bar.append("rect")
		.attr("width", x)
		.attr("height", barHeight - 1);

	bar.append("text")
		.attr("x", function(d) { return x(d) - 3; })
		.attr("y", barHeight/2)
		.attr("dy", ".35em")
		.text(function(d) { return d; });

// Chart2
InitChart();

function InitChart() {

var d = dateTime_array
console.log(d)
var number = {{ number }}
var obj = {}
var dict_constr = function(d, number){
	console.log(d.length, number.length)
	i = 0;
	j = 0;
	for (i; i < d.length; i++) {
		console.log(d[i]);

		for (j; j < number.length; i++){
			console.log(number[j]);	
			obj[d[i]] = number[j];
		}
	}
}
dict_constr(d, number)
console.log(obj)
var lineData = [{x:1, y:2}]
var vis = d3.select("#chart2"), 
	WIDTH = 500,
    HEIGHT = 200,
    MARGINS = {
      top: 20,
      right: 20,
      bottom: 20,
      left: 50
    },
xRange = d3.scale.linear().range([MARGINS.left, WIDTH - MARGINS.right]).domain([d3.min(lineData, function (d) {
    return d.x;
    }),

d3.max(lineData, function (d) {
    return d.x;
    })
]),

yRange = d3.scale.linear().range([HEIGHT - MARGINS.top, MARGINS.bottom]).domain([d3.min(lineData, function (d) {
    return d.y;
	}),

d3.max(lineData, function (d) {
    return d.y;
    })
]),

xAxis = d3.svg.axis()
    .scale(xRange)
    // .tickSize(5)
    .tickSubdivide(true),

yAxis = d3.svg.axis()
    .scale(yRange)
    // .tickSize(5)
    .orient("left")
    .tickSubdivide(true);


vis.append("svg:g")
    .attr("class", "x axis")
    .attr("transform", "translate(0," + (HEIGHT - MARGINS.bottom) + ")")
    .call(xAxis);

vis.append("svg:g")
    .attr("class", "y axis")
    .attr("transform", "translate(" + (MARGINS.left) + ",0)")
    .call(yAxis);

var lineFunc = d3.svg.line()
	.x(function (d) {
    return xRange(d.x);
  })
	.y(function (d) {
    return yRange(d.y);
  })
	.interpolate('linear');

vis.append("svg:path")
	.attr("d", lineFunc(lineData))
	.attr("stroke", "blue")
	.attr("stroke-width", 2)
	.attr("fill", "none");
}

// Chart3
