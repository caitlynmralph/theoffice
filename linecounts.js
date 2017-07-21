var w = 600;
var h = 500;
var barPadding = 10;
var padding = 30;

//Create svg element
var div4 = d3.select(".line-counts-container")
  .append("div");

var formatAsPercentage = d3.format(".1%");

d3.csv("spreadsheets/linecountsnew_cleaned.csv", function(data) {
  data.forEach(function(d) {
      d.count = +d.count;
      // console.log(d.Line1);
      // console.log(d.Line1[1]);
      // console.log(d.Line1[3]);
      // console.log(d.Line1.slice(6,-2));
      // console.log(d);

  });

    var yScale = d3.scaleBand()
      .rangeRound([padding,h-padding])
      .padding(0.5);
    var xScale = d3.scaleLinear()
      .range([padding, w-padding]);

    yScale.domain(data.map(function(d) { return d.character; }));
    xScale.domain([0, d3.max(data, function(d) { return d.count; })]);

    var svg4 = div4
        .append("svg")
        .attr("width",w)
        .attr("height",h);

    svg4.selectAll("rect")
        .data(data)
        .enter()
        .append("rect")
        .attr("x",padding)
        .attr("y",function(d) {
          return yScale(d.character);
        })
        .attr("width",function(d) {
          return xScale(d.count);
        })
        .attr("height",function(d) {
          return yScale.bandwidth();
        });

    var xaxisScale = d3.scaleLinear()
      .domain([d3.max(data,function(d) {d.count;}),0])
      .range([padding, w-padding]);
    var xAxis = d3.axisBottom(xScale)
      .ticks();

    svg4.append("g")
    .attr("class","axis-line")
    .attr("transform","translate(0," + (h-padding) + ")")
    .call(xAxis)
    .selectAll("text")
      .attr("class","axis-text")
      .attr("dx", "-.8em")
      .attr("dy", "-.55em");

    var yAxis = d3.axisLeft(yScale);

    svg2.append("g")
      // .attr("class","axis-line")
      .attr("transform","translate(" + (w) + ",0)")
      .call(yAxis)
      .selectAll("text")
        .attr("class","axis-text")
        .attr("dx", "-.8em")
        .attr("dy", "-.55em");

  });
