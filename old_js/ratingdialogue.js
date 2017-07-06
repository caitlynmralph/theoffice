var wi = 600;
var he = 400;
var padding = 30;

//Create SVG element
var div3 = d3.select(".rating-dialogue-container")
  .append("div");

var formatAsPercentage = d3.format(".1%");
d3.csv("spreadsheets/michael_percentdialogue_episode.csv", function(d, i, columns) {
  for (var i = 1, n = columns.length; i < n; ++i) d[columns[i]] = +d[columns[i]];
    console.log(d);
    return d;
  }, function(error, dataset) {
    if (error) throw error;

    var xScale = d3.scaleLinear()
        .domain([0,d3.max(dataset, function(d) { return d.Michael;})])
        .range([padding,wi-padding*2]);
    var yScale = d3.scaleLinear()
        .domain([0,d3.max(dataset, function(d) {return d.Rating;})])
        .range([he-padding*2,padding]);
    var rScale = d3.scaleLinear()
        .domain([0,d3.max(dataset, function(d) { return d.Rating;})])
        .range([2,5]);
    var xAxis = d3.axisBottom(xScale)
        .ticks(5)
        .tickFormat(formatAsPercentage);
    var yAxis = d3.axisLeft(yScale)
        .ticks(5);

    var svg3 = div3
        .append("svg")
        .attr("width",wi)
        .attr("height",he);

    svg3.selectAll("circle")
        .data(dataset)
        .enter()
        .append("circle")
        .attr("cx",function(d) {
            return xScale(d.Michael); //Bar width of 20 plus 1 for padding
        })
        .attr("cy",function(d) {
            console.log(d.Rating)
            return yScale(d.Rating);
        })
        .attr("r", function(d) {
          return rScale(d.Rating);
        })

    svg3.append("g")
        .attr("class","axis") //Assign "axis" class
        .attr("transform","translate(0," + (he - padding) + ")")
        .call(xAxis)
    svg3.append("g")
        .attr("class","axis")
        .attr("transform","translate(" + padding + ",0)")
        .call(yAxis);

  });
