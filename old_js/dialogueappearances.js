var w = 1000;
var h = 800;
var padding = 60;

//Create svg element
var div2 = d3.select(".dialogue-appearances-container")
  .append("div");

d3.csv("spreadsheets/linecountsnew_cleaned_maincharacters.csv", function(d, i, columns) {

  for (var i = 1, n = columns.length; i < n; ++i) d[columns[i]] = +d[columns[i]];
    console.log(d);
    return d;
  }, function(error, data) {
    if (error) throw error;

  var yScaleRight = d3.scaleBand()
    .rangeRound([padding,h-padding])
    .padding(0.5);
  var xScaleRight = d3.scaleLinear()
    .domain([0,d3.max(data,function(d) {d.count;})])
    .range([(w/2)+10, padding]);

  yScaleRight.domain(data.map(function(d) { return d.character; }));
  xScaleRight.domain([0, d3.max(data, function(d) { return d.count; })]);

  var svg2 = div2
    .append("svg")
    .attr("width",w)
    .attr("height",h);

  svg2.selectAll("rect.right")
    .data(data)
    .enter()
    .append("rect")
    .attr("class","bar")
    .attr("x",(w/2)+10)
    .attr("y",function(d) {
      return yScaleRight(d.character);
    })
    .attr("width",function(d) {
      return ((w/2)+10) - xScaleRight(d.count);
    })
    .attr("height",function(d,i) {
      return yScaleRight.bandwidth();
    });

  var xaxisScaleRight = d3.scaleLinear()
    .domain([d3.max(data,function(d) {d.count;}),0])
    .range([(w/2)+10, padding]);
  var xAxisRight = d3.axisBottom(xaxisScaleRight)
    .ticks();

  xaxisScaleRight.domain([d3.max(data, function(d) { return d.count; }),0]);

  svg2.append("g")
    .attr("class","axis-line")
    .attr("transform","translate(" + (((w/2)+10) - padding) + "," + (h - padding) + ")")
    .call(xAxisRight)
    .selectAll("text")
      .attr("class","axis-text")
      .attr("dx", "-.8em")
      .attr("dy", "-.55em")
      .attr("transform", "rotate(-60)" );

  var yScaleLeft = d3.scaleBand()
    .rangeRound([padding,h-padding])
    .padding(0.5);
  var xScaleLeft = d3.scaleLinear()
    .domain([0,d3.max(data,function(d) {d.appearance;})])
    .range([padding,(w/2)-10]);

  yScaleLeft.domain(data.map(function(d) { return d.character; }));
  xScaleLeft.domain([d3.max(data, function(d) { return d.appearance; }),0]);

  svg2.selectAll("rect.left")
    .data(data)
    .enter()
    .append("rect")
    .attr("class","bar")
    .attr("x",function(d) {
      return ((w/2)-10) - xScaleLeft(d.appearance);
    })
    .attr("y",function(d) {
      return yScaleLeft(d.character);
    })
    .attr("width",function(d) {
      return xScaleLeft(d.appearance);
    })
    .attr("height",function(d,i) {
      return yScaleLeft.bandwidth();
    });

  var xaxisScaleLeft = d3.scaleLinear()
    .domain([d3.max(data,function(d) {d.appearance;}),0])
    .range([padding,(w/2)-10]);
  var xAxisLeft = d3.axisBottom(xaxisScaleLeft)
    .ticks();

  xaxisScaleLeft.domain([d3.max(data, function(d) { return d.appearance; }),0]);

  svg2.append("g")
    .attr("class","axis-line")
    .attr("transform","translate(0," + (h - padding) + ")")
    .call(xAxisLeft)
    .selectAll("text")
      .attr("class","axis-text")
      .attr("dx", "-.8em")
      .attr("dy", "-.55em")
      .attr("transform", "rotate(-60)" );

  var yaxisScale = d3.scaleBand()
    .rangeRound([padding,h-padding])
    .padding(0.5);
  var yAxis = d3.axisLeft(yaxisScale);
  yaxisScale.domain(data.map(function(d) { return d.character; }));

  svg2.append("g")
    // .attr("class","axis-line")
    .attr("transform","translate(" + (w/2 - (padding/2) + 30) + ",0)")
    .call(yAxis)
    .selectAll("text")
      .attr("class","axis-text")
      .attr("dx", "-.8em")
      .attr("dy", "-.55em");

  // svg.append("text")
  //   .attr("transform","rotate(-90)")
  //   .attr("y",padding-35)
  //   .attr("x",0-(h/2))
  //   .attr("class","yAxis-label")
  //   .attr("text-anchor","middle")
  //   .text("Line counts");

  });