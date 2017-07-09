var wi = 600;
var he = 500;
var padding = 50;

//Create svg element
var div2 = d3.select(".popular-character-container")
  .append("div");

var formatAsPercentage = d3.format(".1%");

d3.tsv("spreadsheets/characters_rating.tsv", function(d, i, columns) {
  for (var i = 0, n = columns.length; i < n; ++i) {
    if (i == 0 || i == 2 || i == 3) {
      d[columns[i]] = +d[columns[i]];
    }
    console.log(d);
    return d;
  }
  }, function(error, dataset) {
    if (error) throw error;

    var xScale = d3.scaleLinear()
        .domain([.6,d3.max(dataset, function(d) { return d.Rating;})])
        .range([padding,wi-padding]);
    var rScale = d3.scaleLinear()
        .domain([.6,d3.max(dataset, function(d) { return d.Rating;})])
        .range([1,6]);
    var xAxis = d3.axisBottom(xScale)
        .tickSize([0])
        .ticks(0);

    var svg2 = div2
        .append("svg")
        .attr("width",wi)
        .attr("height",he);

    svg2.append("g")
        .attr("transform","translate(0," + (he - padding) + ")")
        .call(xAxis);

    var xaxislabel = svg2
        .append("g");

    xaxislabel.append("text")
        .attr("transform","translate(" + ((wi-(padding*2))/2) + "," + (he-(padding/5)) + ")")
        .text("Episode Rating");

    xaxislabel.append("text")
        .attr("transform","translate(" + (wi-((padding*2)+450)) + "," + (he-(padding/2)) + ")")
        .text("Low");

    xaxislabel.append("text")
        .attr("transform","translate(" + (wi-padding-30) + "," + (he-(padding/2)) + ")")
        .text("High");

    var div = svg2
        .append("div")
        .attr("class", "tooltip")
        .style("opacity", 0);

    // Andy
    d3.tsv("spreadsheets/andy_rating.tsv", function(d, i, columns) {
      for (var i = 0, n = columns.length; i < n; ++i) {
        if (i == 0 || i == 2) {
          d[columns[i]] = +d[columns[i]];
        }
        console.log(d);
        return d;
      }
    }, function(error, AndyData) {
        if (error) throw error;

        var Andy = svg2
            .append("g")
            .attr("width",wi)
            .attr("height",(he-(padding*2))/4);

        Andy.selectAll("circle")
            .data(AndyData)
            .enter()
            .append("circle")
            .attr("cx",function(d) {
                return xScale(d.Rating); //Bar width of 20 plus 1 for padding
            })
            .attr("cy",he-(padding*2))
            .attr("r", function(d) {
              return rScale(d.Rating);
            })
            .on("mouseover", function(d) {
              div.transition()
                .duration(200)
                .style("opacity", .9);
              div.html(d.Rating)
                .style("left", (d3.event.pageX) + "px")
                .style("top", (d3.event.pageY - 28) + "px");
              })
            .on("mouseout", function(d) {
              div.transition()
                .duration(500)
                .style("opacity", 0);
              });

        Andy.append("g")
            .append("text")
            .attr("transform","translate(" + (wi-((padding*2)+445)) + "," + (he-(padding*2)) + ")")
            .text("Andy");

      });

      //Dwight
      d3.tsv("spreadsheets/dwight_rating.tsv", function(d, i, columns) {
        for (var i = 0, n = columns.length; i < n; ++i) {
          if (i == 0 || i == 2) {
            d[columns[i]] = +d[columns[i]];
          }
          console.log(d);
          return d;
        }
      }, function(error, DwightData) {
          if (error) throw error;

          var Dwight = svg2
              .append("g")
              .attr("width",wi)
              .attr("height",(he-(padding*2))/4);

          Dwight.selectAll("circle")
              .data(DwightData)
              .enter()
              .append("circle")
              .attr("cx",function(d) {
                  return xScale(d.Rating); //Bar width of 20 plus 1 for padding
              })
              .attr("cy",he-(padding*4))
              .attr("r", function(d) {
                return rScale(d.Rating);
              });

          Dwight.append("g")
              .append("text")
              .attr("transform","translate(" + (wi-((padding*2)+445)) + "," + (he-(padding*4)) + ")")
              .text("Dwight");

        });

        //Pam
        d3.tsv("spreadsheets/pam_rating.tsv", function(d, i, columns) {
          for (var i = 0, n = columns.length; i < n; ++i) {
            if (i == 0 || i == 2) {
              d[columns[i]] = +d[columns[i]];
            }
            console.log(d);
            return d;
          }
        }, function(error, PamData) {
            if (error) throw error;

            var Pam = svg2
                .append("g")
                .attr("width",wi)
                .attr("height",(he-(padding*2))/4);

            Pam.selectAll("circle")
                .data(PamData)
                .enter()
                .append("circle")
                .attr("cx",function(d) {
                    return xScale(d.Rating); //Bar width of 20 plus 1 for padding
                })
                .attr("cy",he-(padding*6))
                .attr("r", function(d) {
                  return rScale(d.Rating);
                });

            Pam.append("g")
                .append("text")
                .attr("transform","translate(" + (wi-((padding*2)+445)) + "," + (he-(padding*6)) + ")")
                .text("Pam");

          });

      // Jim
      d3.tsv("spreadsheets/jim_rating.tsv", function(d, i, columns) {
        for (var i = 0, n = columns.length; i < n; ++i) {
          if (i == 0 || i == 2) {
            d[columns[i]] = +d[columns[i]];
          }
          console.log(d);
          return d;
        }
      }, function(error, JimData) {
          if (error) throw error;

          var Jim = svg2
              .append("g")
              .attr("width",wi)
              .attr("height",(he/4)-5);

          Jim.selectAll("circle")
              .data(JimData)
              .enter()
              .append("circle")
              .attr("cx",function(d) {
                  return xScale(d.Rating); //Bar width of 20 plus 1 for padding
              })
              .attr("cy",he-padding*8)
              .attr("r", function(d) {
                return rScale(d.Rating);
              });

          Jim.append("g")
              .append("text")
              .attr("transform","translate(" + (wi-((padding*2)+445)) + "," + (he-(padding*8)) + ")")
              .text("Jim");

        });
  });
