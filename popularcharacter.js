var w3 = 1000;
var h3 = 400;
var p3 = 30;

//Create SVG element
var div3 = d3.select(".popular-character-container")
  .append("div");

var formatAsPercentage = d3.format(".1%");

d3.tsv("spreadsheets/characters_rating_cleaned_new.tsv", function(data) {
  data.forEach(function(d) {
      d.ENumber = +d.ENumber;
      d.Rating = +d.Rating;
      console.log(d.ENumber);
      console.log(d.Rating);
  });

    var xScale = d3.scaleLinear()
        .domain([0,d3.max(data, function(d) { return d.ENumber;})])
        .range([p3,w3-p3]);
    var yScale = d3.scaleLinear()
        .domain([0.6,d3.max(data, function(d) {return d.Rating;})])
        .range([h3-p3,p3]);
    var rScale = d3.scaleLinear()
        .domain([0,d3.max(data, function(d) { return d.Rating;})])
        .range([2,5]);
    var xAxis = d3.axisBottom(xScale)
        .ticks(18);
    var yAxis = d3.axisLeft(yScale)
        .ticks(5);

    var svg3 = div3
        .append("svg")
        .attr("width",w3)
        .attr("height",h3)
        .attr("class","popular-character-scatterplot");

    var tool_tip = d3.tip()
      .attr("class", "d3-tip")
      .offset([-8, 0])
      .html(function(d) { return "<strong>Episode</strong>: " + d.Episode_Number + ", " + d.Episode + "</br>" + "<strong>Character with most dialogue</strong>: " + d.Character + "</br>" + "<strong>Rating</strong>: " + d.Rating; });
    svg3.call(tool_tip);

    svg3.selectAll("circle")
        .data(data)
        .enter()
        .append("circle")
        .attr("cx",function(d) {
            return xScale(d.ENumber);
        })
        .attr("cy",function(d) {
            return yScale(d.Rating);
        })
        .attr("r", function(d) {
          return rScale(d.Rating);
        })
        .style("fill",function(d) {
          if (d.Character == "Jim") {
            return "steelblue";
          }
          else if (d.Character == "Pam") {
            return "rgba(0, 0, 139, 0.79)";
          }
          else if (d.Character == "Dwight") {
            return "darkturquoise";
          }
          else if (d.Character == "Andy") {
            return "gray";
          }
          else {
            return "black";
          }
        })
        .on('mouseover', tool_tip.show)
        .on('mouseout', tool_tip.hide);

    svg3.append("g")
        .attr("class","axis-line") //Assign "axis" class
        .attr("transform","translate(0," + (h3 - p3) + ")")
        .call(xAxis)
        .attr("class","axis-text");

    svg3.append("text")      // text label for the x axis
        .attr("x", w3/2 )
        .attr("y",  h3-p3+50  )
        .style("text-anchor", "middle")
        .attr("class","axis-label")
        .text("EPISODE");

    svg3.append("g")
        .attr("class","axis-line")
        .attr("transform","translate(" + p3 + ",0)")
        .call(yAxis)
        .attr("class","axis-text");

    svg3.append("text")      // text label for the x axis
        .attr("x", -200 )
        .attr("y",  -10 )
        .attr("transform","rotate(-90)")
        .style("text-anchor", "middle")
        .attr("class","axis-label")
        .text("RATING");

  });
