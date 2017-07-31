var w8 = 600;
var h8 = 400;
var p8 = 60;

//Create svg element
var div8 = d3.select(".dialogue-over-time-container")
  .append("div");

d3.csv("spreadsheets/percentdialogue_season_maincharacters_transpose.csv", function(d, i, columns) {
  for (var i = 1, n = columns.length; i < n; ++i) d[columns[i]] = +d[columns[i]];
    console.log(d);
    return d;
  }, function(error, data) {
    if (error) throw error;

  var xScale = d3.scaleBand()
    .rangeRound([p8,w8-p8])
    .padding(0.1);
  var yScale = d3.scaleLinear()
    .range([h8-p8, p8]);
  var xAxis = d3.axisBottom(xScale);
  var yAxis = d3.axisLeft(yScale)
    .tickFormat(d3.format(".0%"))
    .tickSizeOuter(0);

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

  var valueline6 = d3.line()
      .x(function(d) { return xScale(d.seasons); })
      .y(function(d) { return yScale(d.Angela); })
      .curve(d3.curveMonotoneX);

  var valueline7 = d3.line()
      .x(function(d) { return xScale(d.seasons); })
      .y(function(d) { return yScale(d.Kevin); })
      .curve(d3.curveMonotoneX);

  var valueline8 = d3.line()
      .x(function(d) { return xScale(d.seasons); })
      .y(function(d) { return yScale(d.Erin); })
      .curve(d3.curveMonotoneX);

  var valueline9 = d3.line()
      .x(function(d) { return xScale(d.seasons); })
      .y(function(d) { return yScale(d.Oscar); })
      .curve(d3.curveMonotoneX);

  var valueline10 = d3.line()
      .x(function(d) { return xScale(d.seasons); })
      .y(function(d) { return yScale(d.Ryan); })
      .curve(d3.curveMonotoneX);

  var svg8 = div8
      .append("svg")
      .attr("width",w8)
      .attr("height",h8)
      .attr("class","dialogue-over-time-line-chart");

  var path = svg8.append("path")
      .data([data])
      .attr("class", "line")
      .style("stroke","blue")
      .attr("d", valueline);

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

  var path = svg8.append("path")
      .data([data])
      .attr("class", "line")
      .style("stroke","blue")
      .attr("d", valueline2)

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

  var path = svg8.append("path")
      .data([data])
      .attr("class", "line")
      .style("stroke","blue")
      .attr("d", valueline3)

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

  var path = svg8.append("path")
      .data([data])
      .attr("class", "line")
      .style("stroke","blue")
      .attr("d", valueline4)

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

  var path = svg8.append("path")
      .data([data])
      .attr("class", "line")
      .style("stroke","blue")
      .attr("d", valueline5)

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

  var path = svg8.append("path")
      .data([data])
      .attr("class", "line")
      .style("stroke","blue")
      .attr("d", valueline6)

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

  var path = svg8.append("path")
      .data([data])
      .attr("class", "line")
      .style("stroke","blue")
      .attr("d", valueline7)

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

  var path = svg8.append("path")
      .data([data])
      .attr("class", "line")
      .style("stroke","blue")
      .attr("d", valueline8)

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

  var path = svg8.append("path")
      .data([data])
      .attr("class", "line")
      .style("stroke","blue")
      .attr("d", valueline9)

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

  var path = svg8.append("path")
      .data([data])
      .attr("class", "line")
      .style("stroke","blue")
      .attr("d", valueline10)

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

  svg8.append("g")
    .attr("class","axis-line")
    .attr("transform","translate(0," + (h8 - p8) + ")")
    .call(xAxis)
    .selectAll("text")
      .attr("class","axis-text")
      .attr("dx", "0em")
      .attr("dy", ".75em");

  svg8.append("g")
    .attr("class","axis-line")
    .attr("transform","translate(" + p8 + ",0)")
    .call(yAxis)
    .selectAll("text")
      .attr("class","axis-text");

  svg8.append("text")
    .attr("transform","rotate(-90)")
    .attr("y",p8-50)
    .attr("x",0-(h8/2))
    .attr("class","axis-label")
    .attr("text-anchor","middle")
    .text("DIALOGUE");

  svg8.append("text")
    // .attr("transform","rotate(-90)")
    .attr("y",w8/2+p8+20)
    .attr("x",h8/2+p8)
    .attr("class","axis-label")
    .attr("text-anchor","middle")
    .text("TIME");

  var legend = svg8
    // .append("rect")
    // .attr("transform","rotate(-90)")
    // .attr("width","100px")
    // .attr("height","100px")
    // .style("color","black")
    // .attr("class","legend-dialogue")
    .append("g");

    legend.append("text")
      .attr("transform","translate(" + (w8-p8) + "," + (50) + ")")
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

  d3.csv("spreadsheets/percentdialogue_episode_maincharacters_transpose.csv", function(d, i, columns) {
    for (var i = 1, n = columns.length; i < n; ++i) d[columns[i]] = +d[columns[i]];
      console.log(d);
      return d;
    }, function(error, data) {
      if (error) throw error;

      xScale.domain(data.map(function(d) { return d.episodes; }));

      svg8.selectAll("circle")
          .data(data)
          .enter()
          .append("circle")
          .style("fill","black")
          .attr("cx",function(d) {
              return xScale(d.episodes);
          })
          .attr("cy",function(d) {
              return yScale(d.Michael);
          })
          .attr("r", 2)
          .transition()
            .duration(4000)
            .delay(4000)
            .attr("cy",function(d) {
                return yScale(d.Dwight);
            })
            .transition()
              .duration(4000)
              .attr("cy",function(d) {
                  return yScale(d.Jim);
              })
              .transition()
                .duration(4000)
                .attr("cy",function(d) {
                    return yScale(d.Pam);
                })
                .transition()
                  .duration(4000)
                  .attr("cy",function(d) {
                      return yScale(d.Andy);
                  })
                  .transition()
                    .duration(4000)
                    .attr("cy",function(d) {
                        return yScale(d.Angela);
                      })
                        .transition()
                          .duration(4000)
                          .attr("cy",function(d) {
                              return yScale(d.Kevin);
                            })
                              .transition()
                                .duration(4000)
                                .attr("cy",function(d) {
                                    return yScale(d.Erin);
                                  })
                                    .transition()
                                      .duration(4000)
                                      .attr("cy",function(d) {
                                          return yScale(d.Oscar)
                                        })
                                          .transition()
                                            .duration(4000)
                                            .attr("cy",function(d) {
                                                return yScale(d.Ryan);
                                              })
                                              .transition()
                                                .duration(500)
                                                .style("fill","transparent");
    });
  });
