var w7 = 600;
var h7 = 400;
var p7 = 60;

//Create svg element
var div7 = d3.select(".dialogue-over-time-container")
  .append("div");

d3.csv("spreadsheets/percentdialogue_episode_maincharacters_transpose.csv", function(d, i, columns) {
  for (var i = 1, n = columns.length; i < n; ++i) d[columns[i]] = +d[columns[i]];
    console.log(d);
    return d;
  }, function(error, data) {
    if (error) throw error;

  var xScale = d3.scaleBand()
    .rangeRound([p7/2,w7-p7*2])
    .padding(0.1);
  var yScale = d3.scaleLinear()
    .range([h7-p7, p7]);
  var xAxis = d3.axisBottom(xScale)
    .tickSize(0)
    .tickFormat("");
  var yAxis = d3.axisLeft(yScale)
    .tickFormat(d3.format(".0%"))
    .tickSizeOuter(0);

  xScale.domain(data.map(function(d) { return d.episodes; }));
  yScale.domain([0, d3.max(data, function(d) { return Math.max(d.Michael, d.Dwight,d.Jim,
    d.Pam,d.Andy );})]);

  var valueLine = d3.line()
      .x(function(d) { return xScale(d.episodes); })
      .y(function(d) { return yScale(d.Michael); })
      .curve(d3.curveMonotoneX);

  var valueLine2 = d3.line()
      .x(function(d) { return xScale(d.episodes); })
      .y(function(d) { return yScale(d.Dwight); })
      .curve(d3.curveMonotoneX);;

  var valueLine3 = d3.line()
      .x(function(d) { return xScale(d.episodes); })
      .y(function(d) { return yScale(d.Jim); })
      .curve(d3.curveMonotoneX);;

  var valueLine4 = d3.line()
      .x(function(d) { return xScale(d.episodes); })
      .y(function(d) { return yScale(d.Pam); })
      .curve(d3.curveMonotoneX);;

  var valueLine5 = d3.line()
      .x(function(d) { return xScale(d.episodes); })
      .y(function(d) { return yScale(d.Andy); })
      .curve(d3.curveMonotoneX);

  var valueLine6 = d3.line()
      .x(function(d) { return xScale(d.episodes); })
      .y(function(d) { return yScale(d.Angela); })
      .curve(d3.curveMonotoneX);

  var valueLine7 = d3.line()
      .x(function(d) { return xScale(d.episodes); })
      .y(function(d) { return yScale(d.Kevin); })
      .curve(d3.curveMonotoneX);

  var valueLine8 = d3.line()
      .x(function(d) { return xScale(d.episodes); })
      .y(function(d) { return yScale(d.Erin); })
      .curve(d3.curveMonotoneX);

  var valueLine9 = d3.line()
      .x(function(d) { return xScale(d.episodes); })
      .y(function(d) { return yScale(d.Oscar); })
      .curve(d3.curveMonotoneX);

  var valueLine10 = d3.line()
      .x(function(d) { return xScale(d.episodes); })
      .y(function(d) { return yScale(d.Ryan); })
      .curve(d3.curveMonotoneX);

  var svg7 = div7
      .append("svg")
      .attr("width",w7)
      .attr("height",h7)
      .attr("class","dialogue-over-time-line-chart");

  var path = svg7.append("path")
      .data([data])
      .attr("class", "line")
      .style("stroke","blue")
      .attr("d", valueLine);

  var totalLength = path.node().getTotalLength();

  path
    .attr("stroke-dasharray", totalLength + " " + totalLength)
    .attr("stroke-dashoffset", totalLength)
    .attr("id", "path1")
    .transition()
      .duration(4000)
      .attr("stroke-dashoffset", 0)
      .style("stroke-opacity",0.3)
      .style("stroke","rgb(169, 169, 169)")
      .transition()
        .delay(16000)
        .duration(500)
        .style("stroke-opacity",0);

  var path = svg7.append("path")
      .data([data])
      .attr("class", "line")
      .style("stroke","blue")
      .attr("d", valueLine2)

  var totalLength = path.node().getTotalLength();

  path
    .attr("stroke-dasharray", totalLength + " " + totalLength)
    .attr("stroke-dashoffset", totalLength)
    .transition()
      .duration(4000)
      .delay(4000)
      .attr("stroke-dashoffset", 0)
      .style("stroke-opacity",0.3)
      .style("stroke","rgb(169, 169, 169)")
      .transition()
        .delay(12000)
        .duration(500)
        .style("stroke-opacity",0);

  var path = svg7.append("path")
      .data([data])
      .attr("class", "line")
      .style("stroke","blue")
      .attr("d", valueLine3)

  var totalLength = path.node().getTotalLength();

  path
    .attr("stroke-dasharray", totalLength + " " + totalLength)
    .attr("stroke-dashoffset", totalLength)
    .transition()
      .duration(4000)
      .delay(8000)
      .attr("stroke-dashoffset", 0)
      .style("stroke-opacity",0.3)
      .style("stroke","rgb(169, 169, 169)")
      .transition()
        .delay(8000)
        .duration(500)
        .style("stroke-opacity",0);

  var path = svg7.append("path")
      .data([data])
      .attr("class", "line")
      .style("stroke","blue")
      .attr("d", valueLine4)

  var totalLength = path.node().getTotalLength();

  path
    .attr("stroke-dasharray", totalLength + " " + totalLength)
    .attr("stroke-dashoffset", totalLength)
    .transition()
      .duration(4000)
      .delay(12000)
      .attr("stroke-dashoffset", 0)
      .style("stroke-opacity",0.3)
      .style("stroke","rgb(169, 169, 169)")
      .transition()
        .delay(4000)
        .duration(500)
        .style("stroke-opacity",0);

  var path = svg7.append("path")
      .data([data])
      .attr("class", "line")
      .style("stroke","blue")
      .attr("d", valueLine5)

  var totalLength = path.node().getTotalLength();

  path
    .attr("stroke-dasharray", totalLength + " " + totalLength)
    .attr("stroke-dashoffset", totalLength)
    .transition()
      .duration(4000)
      .delay(16000)
      .attr("stroke-dashoffset", 0)
      .style("stroke-opacity",0.3)
      .style("stroke","rgb(169, 169, 169)")
      .transition()
        .duration(500)
        .style("stroke-opacity",0);

  var path = svg7.append("path")
      .data([data])
      .attr("class", "line")
      .style("stroke","blue")
      .attr("d", valueLine6)

  var totalLength = path.node().getTotalLength();

  path
    .attr("stroke-dasharray", totalLength + " " + totalLength)
    .attr("stroke-dashoffset", totalLength)
    .transition()
      .duration(4000)
      .delay(20500)
      .attr("stroke-dashoffset", 0)
      .style("stroke-opacity",0.3)
      .style("stroke","rgb(169, 169, 169)")
      .transition()
        .duration(500)
        .delay(16000)
        .style("stroke-opacity",0);

  var path = svg7.append("path")
      .data([data])
      .attr("class", "line")
      .style("stroke","blue")
      .attr("d", valueLine7)

  var totalLength = path.node().getTotalLength();

  path
    .attr("stroke-dasharray", totalLength + " " + totalLength)
    .attr("stroke-dashoffset", totalLength)
    .transition()
      .duration(4000)
      .delay(24500)
      .attr("stroke-dashoffset", 0)
      .style("stroke-opacity",0.3)
      .style("stroke","rgb(169, 169, 169)")
      .transition()
        .duration(500)
        .delay(12000)
        .style("stroke-opacity",0);

  var path = svg7.append("path")
      .data([data])
      .attr("class", "line")
      .style("stroke","blue")
      .attr("d", valueLine8)

  var totalLength = path.node().getTotalLength();

  path
    .attr("stroke-dasharray", totalLength + " " + totalLength)
    .attr("stroke-dashoffset", totalLength)
    .transition()
      .duration(4000)
      .delay(28500)
      .attr("stroke-dashoffset", 0)
      .style("stroke-opacity",0.3)
      .style("stroke","rgb(169, 169, 169)")
      .transition()
        .duration(500)
        .delay(8000)
        .style("stroke-opacity",0);

  var path = svg7.append("path")
      .data([data])
      .attr("class", "line")
      .style("stroke","blue")
      .attr("d", valueLine9)

  var totalLength = path.node().getTotalLength();

  path
    .attr("stroke-dasharray", totalLength + " " + totalLength)
    .attr("stroke-dashoffset", totalLength)
    .transition()
      .duration(4000)
      .delay(32500)
      .attr("stroke-dashoffset", 0)
      .style("stroke-opacity",0.3)
      .style("stroke","rgb(169, 169, 169)")
      .transition()
        .duration(500)
        .delay(4000)
        .style("stroke-opacity",0);

  var path = svg7.append("path")
      .data([data])
      .attr("class", "line")
      .style("stroke","blue")
      .attr("d", valueLine10)

  var totalLength = path.node().getTotalLength();

  path
    .attr("stroke-dasharray", totalLength + " " + totalLength)
    .attr("stroke-dashoffset", totalLength)
    .transition()
      .duration(4000)
      .delay(36500)
      .attr("stroke-dashoffset", 0)
      .style("stroke-opacity",0.3)
      .style("stroke","rgb(169, 169, 169)")
      .transition()
        .duration(500)
        .style("stroke-opacity",0);

  svg7.append("g")
    .attr("class","axis-line")
    .attr("transform","translate(" + (p7/2) + "," + (h7 - p7) + ")")
    .call(xAxis);

  svg7.append("g")
    .attr("class","axis-line")
    .attr("transform","translate(" + p7 + ",0)")
    .call(yAxis)
    .selectAll("text")
      .attr("class","axis-text");

  svg7.append("text")
    .attr("transform","rotate(-90)")
    .attr("y",p7-50)
    .attr("x",0-(h7/2))
    .attr("class","axis-label")
    .attr("text-anchor","middle")
    .text("DIALOGUE");

  svg7.append("text")
    // .attr("transform","rotate(-90)")
    .attr("y",w7/2+p7+20)
    .attr("x",h7/2+p7)
    .attr("class","axis-label")
    .attr("text-anchor","middle")
    .text("EPISODE");

  var legend = svg7
    // .append("rect")
    // .attr("transform","rotate(-90)")
    // .attr("width","100px")
    // .attr("height","100px")
    // .style("color","black")
    // .attr("class","legend-dialogue")
    .append("g");

    legend.append("text")
      .attr("transform","translate(" + (w7-p7) + "," + (50) + ")")
      .attr("class","axis-label")
      // .attr("text-anchor","middle")
      .text("Michael")
      .transition()
        .duration(4000)
        .delay(4000)
        .text("Dwight")
        .transition()
          .duration(4000)
          .text("Jim")
          .transition()
            .duration(4000)
            .text("Pam")
            .transition()
              .duration(4000)
              .text("Andy")
              .transition()
                .duration(4000)
                .text("Angela")
                .transition()
                  .duration(4000)
                  .text("Kevin")
                  .transition()
                    .duration(4000)
                    .text("Erin")
                    .transition()
                      .duration(4000)
                      .text("Oscar")
                      .transition()
                        .duration(4000)
                        .text("Ryan")
                        .transition()
                          .duration(500)
                          .style("opacity",0);

  });
