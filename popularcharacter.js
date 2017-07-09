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
        .domain([1,d3.max(dataset, function(d) { return d.ENumber;})])
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

        var tool_tip = d3.tip()
          .attr("class", "d3-tip")
          .offset([-8, 0])
          .html(function(d) { return "Epiosode: " + d.ENumber + ", " + d.EName + "</br>" + "Rating: " + d.Rating; });
        Andy.call(tool_tip);

        Andy.selectAll("circle")
            .data(AndyData)
            .enter()
            .append("circle")
            .attr("cx",function(d) {
                return xScale(d.Rating); //Bar width of 20 plus 1 for padding
            })
            .attr("cy",he-(padding*2))
            .attr("r", function(d) {
              return rScale(d.ENumber);
            })
            .on('mouseover', tool_tip.show)
            .on('mouseout', tool_tip.hide);

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

          var tool_tip = d3.tip()
            .attr("class", "d3-tip")
            .offset([-8, 0])
            .html(function(d) { return "Epiosode: " + d.ENumber + ", " + d.EName + "</br>" + "Rating: " + d.Rating; });
          Dwight.call(tool_tip);

          Dwight.selectAll("circle")
              .data(DwightData)
              .enter()
              .append("circle")
              .attr("cx",function(d) {
                  return xScale(d.Rating); //Bar width of 20 plus 1 for padding
              })
              .attr("cy",he-(padding*4))
              .attr("r", function(d) {
                return rScale(d.ENumber);
              })
              .on('mouseover', tool_tip.show)
              .on('mouseout', tool_tip.hide);;

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

            var tool_tip = d3.tip()
              .attr("class", "d3-tip")
              .offset([-8, 0])
              .html(function(d) { return "Epiosode: " + d.ENumber + ", " + d.EName + "</br>" + "Rating: " + d.Rating; });
            Pam.call(tool_tip);

            Pam.selectAll("circle")
                .data(PamData)
                .enter()
                .append("circle")
                .attr("cx",function(d) {
                    return xScale(d.Rating); //Bar width of 20 plus 1 for padding
                })
                .attr("cy",he-(padding*6))
                .attr("r", function(d) {
                  return rScale(d.ENumber);
                })
                .on('mouseover', tool_tip.show)
                .on('mouseout', tool_tip.hide);;

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

          var tool_tip = d3.tip()
            .attr("class", "d3-tip")
            .offset([-8, 0])
            .html(function(d) { return "Epiosode: " + d.ENumber + ", " + d.EName + "</br>" + "Rating: " + d.Rating; });
          Jim.call(tool_tip);

          Jim.selectAll("circle")
              .data(JimData)
              .enter()
              .append("circle")
              .attr("cx",function(d) {
                  return xScale(d.Rating); //Bar width of 20 plus 1 for padding
              })
              .attr("cy",he-padding*8)
              .attr("r", function(d) {
                return rScale(d.ENumber);
              })
              .on('mouseover', tool_tip.show)
              .on('mouseout', tool_tip.hide);;

          Jim.append("g")
              .append("text")
              .attr("transform","translate(" + (wi-((padding*2)+445)) + "," + (he-(padding*8)) + ")")
              .text("Jim");

        });
  });
