var w2 = 600;
var h2 = 500;
var barPadding = 5;
var p2 = 5;

//Create svg element
var div2 = d3.select(".line-counts-container")
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
      .rangeRound([p2,h2-p2])
      .padding(0.1);
    var xScale = d3.scaleLinear()
      .range([p2, w2-p2]);

    yScale.domain(data.map(function(d) { return d.character; }));
    xScale.domain([0, d3.max(data, function(d) { return d.count; })]);

    var svg2 = div2
        .append("svg")
        .attr("width",w2)
        .attr("height",h2)
        .attr("class","line-counts-histogram");

    svg2.selectAll("rect")
        .data(data)
        .enter()
        .append("rect")
        .attr("x",p2)
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
      .domain([0,d3.max(data,function(d) {d.count;})])
      .range([p2, w2-p2]);
    var xAxis = d3.axisBottom(xScale)
      .tickSizeOuter(0);

    svg2.append("g")
      .attr("class","axis-line")
      .attr("transform","translate(0," + (h2-p2) + ")")
      .call(xAxis)
      .selectAll("text")
        .attr("class","axis-text")
        .attr("dx", "-0.5em")
        .attr("dy", "1em");

    svg2.append("text")      // text label for the x axis
        .attr("x", w2/2 )
        .attr("y",  h2-p2+50  )
        .style("text-anchor", "middle")
        .attr("class","axis-label")
        .text("NUMBER OF LINES");

    var yAxis = d3.axisLeft(yScale)
      .tickSizeOuter(0);

    svg2.append("g")
      .attr("class","axis-line")
      .attr("transform","translate(" + (p2) + "," + (0) + ")")
      .call(yAxis)
      .selectAll("text")
        .attr("class","axis-text")
        .attr("dx", "-.7em")
        .attr("dy", "0.4em");

  });
