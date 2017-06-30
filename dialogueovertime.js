var width = 600;
var height = 400;
var padding = 60;

//Create svg element
var div1 = d3.select(".dialogue-overtime-container")
  .append("div");

d3.csv("spreadsheets/percentdialogue_season_maincharacters_transpose.csv", function(d, i, columns) {
  for (var i = 1, n = columns.length; i < n; ++i) d[columns[i]] = +d[columns[i]];
    console.log(d);
    return d;
  }, function(error, data) {
    if (error) throw error;

  var xScale = d3.scaleBand()
    .rangeRound([padding,width-padding])
    .padding(0.1);
  var yScale = d3.scaleLinear()
    .range([height-padding, padding]);
  var xAxis = d3.axisBottom(xScale);
  var yAxis = d3.axisLeft(yScale)
    .tickFormat(d3.format(".0%"));

  xScale.domain(data.map(function(d) { return d.seasons; }));
  yScale.domain([0, d3.max(data, function(d) { return Math.max(d.Michael, d.Dwight,d.Jim,
    d.Pam,d.Andy );})]);

  var valueline = d3.line()
      .x(function(d) { return xScale(d.seasons); })
      .y(function(d) { return yScale(d.Michael); })
      .curve(d3.curveMonotoneX);

  var valueline2 = d3.line()
      .x(function(d) { return xScale(d.seasons); })
      .y(function(d) { return yScale(d.Dwight); })
      .curve(d3.curveMonotoneX);;

  var valueline3 = d3.line()
      .x(function(d) { return xScale(d.seasons); })
      .y(function(d) { return yScale(d.Jim); })
      .curve(d3.curveMonotoneX);;

  var valueline4 = d3.line()
      .x(function(d) { return xScale(d.seasons); })
      .y(function(d) { return yScale(d.Pam); })
      .curve(d3.curveMonotoneX);;

  var valueline5 = d3.line()
      .x(function(d) { return xScale(d.seasons); })
      .y(function(d) { return yScale(d.Andy); })
      .curve(d3.curveMonotoneX);

  var svg1 = div1
      .append("svg")
      .attr("width",width)
      .attr("height",height);

  var path = svg1.append("path")
      .data([data])
      .attr("class", "line")
      .style("stroke","#C0C0C0")
      .attr("d", valueline);

  var totalLength = path.node().getTotalLength();

  path
    .attr("stroke-dasharray", totalLength + " " + totalLength)
    .attr("stroke-dashoffset", totalLength)
    .transition()
      .duration(1000)
      .attr("stroke-dashoffset", 0)
      .style("stroke-opacity",0.1);

  var path = svg1.append("path")
      .data([data])
      .attr("class", "line")
      .style("stroke","#A9A9A9")
      .attr("d", valueline2)

  var totalLength = path.node().getTotalLength();

  path
    .attr("stroke-dasharray", totalLength + " " + totalLength)
    .attr("stroke-dashoffset", totalLength)
    .transition()
      .duration(1000)
      .delay(1000)
      .attr("stroke-dashoffset", 0)
      .style("stroke-opacity",0.1);

  var path = svg1.append("path")
      .data([data])
      .attr("class", "line")
      .style("stroke","#808080")
      .attr("d", valueline3)

  var totalLength = path.node().getTotalLength();

  path
    .attr("stroke-dasharray", totalLength + " " + totalLength)
    .attr("stroke-dashoffset", totalLength)
    .transition()
      .duration(1000)
      .delay(2000)
      .attr("stroke-dashoffset", 0)
      .style("stroke-opacity",0.1);

  var path = svg1.append("path")
      .data([data])
      .attr("class", "line")
      .style("stroke","#696969")
      .attr("d", valueline4)

  var totalLength = path.node().getTotalLength();

  path
    .attr("stroke-dasharray", totalLength + " " + totalLength)
    .attr("stroke-dashoffset", totalLength)
    .transition()
      .duration(1000)
      .delay(3000)
      .attr("stroke-dashoffset", 0)
      .style("stroke-opacity",0.1);

  var path = svg1.append("path")
      .data([data])
      .attr("class", "line")
      .style("stroke","#708090")
      .attr("d", valueline5)

  var totalLength = path.node().getTotalLength();

  path
    .attr("stroke-dasharray", totalLength + " " + totalLength)
    .attr("stroke-dashoffset", totalLength)
    .transition()
      .duration(1000)
      .delay(4000)
      .attr("stroke-dashoffset", 0)
      .style("stroke-opacity",0.1);

  svg1.append("g")
    .attr("class","axis-line")
    .attr("transform","translate(0," + (height - padding) + ")")
    .call(xAxis)
    .selectAll("text")
      .attr("class","axis-text")
      .attr("dx", "-.8em")
      .attr("dy", "-.55em")
      .attr("transform", "rotate(-60)" );

  svg1.append("g")
    .attr("class","axis-line")
    .attr("transform","translate(" + padding + ",0)")
    .call(yAxis)
    .selectAll("text")
      .attr("class","axis-text");

  svg1.append("text")
    .attr("transform","rotate(-90)")
    .attr("y",padding-35)
    .attr("x",0-(height/2))
    .attr("class","yAxis-label")
    .attr("text-anchor","middle")
    .text("Dialogue");

  svg1.append("text")
    // .attr("transform","rotate(-90)")
    .attr("y",(width/2) + (padding*2) + 40)
    .attr("x",(height/2+padding) +40)
    .attr("class","xAxis-label")
    .attr("text-anchor","middle")
    .text("Season");

  });
