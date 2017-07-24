var w4 = 600;
var h4 = 500;
var p4 = 50;

//Create svg element
var div4 = d3.select(".popular-character-container")
  .append("div");

var formatAsPercentage = d3.format(".1%");

d3.tsv("spreadsheets/characters_rating.tsv", function(d, i, columns) {
  for (var i = 0, n = columns.length; i < n; ++i) {
    if (i == 0 || i == 2 || i == 3) {
      d[columns[i]] = +d[columns[i]];
    }
    // console.log(d);
    return d;
  }
  }, function(error, dataset) {
    if (error) throw error;

    var xScale = d3.scaleLinear()
        .domain([.6,d3.max(dataset, function(d) { return d.Rating;})])
        .range([p4,w4-p4]);
    var rScale = d3.scaleLinear()
        .domain([1,d3.max(dataset, function(d) { return d.ENumber;})])
        .range([2,7]);
    var xAxis = d3.axisBottom(xScale)
        .tickSize([0])
        .ticks(0);

    var svg4 = div4
        .append("svg")
        .attr("width",w4)
        .attr("height",h4);

    svg4.append("g")
        .attr("transform","translate(0," + (h4 - p4) + ")")
        .call(xAxis);

    var xaxislabel = svg4
        .append("g");

    xaxislabel.append("text")
        .attr("transform","translate(" + ((w4-(p4*2))/2-10) + "," + (h4-(p4/5)) + ")")
        .attr("class","axis-label")
        .text("EPISODE RATING");

    xaxislabel.append("text")
        .attr("transform","translate(" + (w4-((p4*2)+450)) + "," + (h4-(p4/2)) + ")")
        .attr("class","axis-text")
        .text("LOW");

    xaxislabel.append("text")
        .attr("transform","translate(" + (w4-p4-35) + "," + (h4-(p4/2)) + ")")
        .attr("class","axis-text")
        .text("HIGH");

    svg4.append("circle")
        .attr("class","circle-key")
        .attr("cx",(w4-((p4*2)+420)))
        .attr("cy",p4/2+5)
        .attr("r", 2);

    svg4.append("circle")
        .attr("class","circle-key")
        .attr("cx",(w4-((p4*2)+395)))
        .attr("cy",p4/2+5)
        .attr("r", 7);

    svg4.append("text")
        .attr("transform","translate(" + (w4-((p4*2)+500)) + "," + (p4/2+10) + ")")
        .attr("class","key-label")
        .text("SEASON 1");

    svg4.append("text")
        .attr("transform","translate(" + (w4-((p4*2)+380)) + "," + (p4/2+10) + ")")
        .attr("class","key-label")
        .text("SEASON 9");

    // Andy
    d3.tsv("spreadsheets/andy_rating.tsv", function(d, i, columns) {
      for (var i = 0, n = columns.length; i < n; ++i) {
        if (i == 0 || i == 2) {
          d[columns[i]] = +d[columns[i]];
        }
        // console.log(d);
        return d;
      }
    }, function(error, AndyData) {
        if (error) throw error;

        var Andy = svg4
            .append("g")
            .attr("width",w4)
            .attr("height",(h4-(p4*2))/4);

        var tool_tip = d3.tip()
          .attr("class", "d3-tip")
          .offset([-8, 0])
          .html(function(d) { return "<strong>Episode</strong>: " + d.ENumber + ", " + d.EName + "</br>" + "<strong>Rating</strong>: " + d.Rating; });
        Andy.call(tool_tip);

        Andy.selectAll("circle")
            .data(AndyData)
            .enter()
            .append("circle")
            .attr("cx",function(d) {
                return xScale(d.Rating);
            })
            .attr("cy",h4-(p4*2))
            .attr("r", function(d) {
              return rScale(d.ENumber);
            })
            .on('mouseover', tool_tip.show)
            .on('mouseout', tool_tip.hide);

        Andy.append("g")
            .append("text")
            .attr("transform","translate(" + (w4-((p4*2)+445)) + "," + (h4-(p4*2)) + ")")
            .attr("class","character-label")
            .text("Andy");

      });

      //Dwight
      d3.tsv("spreadsheets/dwight_rating.tsv", function(d, i, columns) {
        for (var i = 0, n = columns.length; i < n; ++i) {
          if (i == 0 || i == 2) {
            d[columns[i]] = +d[columns[i]];
          }
          // console.log(d);
          return d;
        }
      }, function(error, DwightData) {
          if (error) throw error;

          var Dwight = svg4
              .append("g")
              .attr("width",w4)
              .attr("height",(h4-(p4*2))/4);

          var tool_tip = d3.tip()
            .attr("class", "d3-tip")
            .offset([-8, 0])
            .html(function(d) { return "<strong>Episode</strong>: " + d.ENumber + ", " + d.EName + "</br>" + "<strong>Rating</strong>: " + d.Rating; });
          Dwight.call(tool_tip);

          Dwight.selectAll("circle")
              .data(DwightData)
              .enter()
              .append("circle")
              .attr("cx",function(d) {
                  return xScale(d.Rating);
              })
              .attr("cy",h4-(p4*4))
              .attr("r", function(d) {
                return rScale(d.ENumber);
              })
              .on('mouseover', tool_tip.show)
              .on('mouseout', tool_tip.hide);;

          Dwight.append("g")
              .append("text")
              .attr("transform","translate(" + (w4-((p4*2)+445)) + "," + (h4-(p4*4)) + ")")
              .attr("class","character-label")
              .text("Dwight");

        });

        //Pam
        d3.tsv("spreadsheets/pam_rating.tsv", function(d, i, columns) {
          for (var i = 0, n = columns.length; i < n; ++i) {
            if (i == 0 || i == 2) {
              d[columns[i]] = +d[columns[i]];
            }
            // console.log(d);
            return d;
          }
        }, function(error, PamData) {
            if (error) throw error;

            var Pam = svg4
                .append("g")
                .attr("width",w4)
                .attr("height",(h4-(p4*2))/4);

            var tool_tip = d3.tip()
              .attr("class", "d3-tip")
              .offset([-8, 0])
              .html(function(d) { return "<strong>Episode</strong>: " + d.ENumber + ", " + d.EName + "</br>" + "<strong>Rating</strong>: " + d.Rating; });
            Pam.call(tool_tip);

            Pam.selectAll("circle")
                .data(PamData)
                .enter()
                .append("circle")
                .attr("cx",function(d) {
                    return xScale(d.Rating);
                })
                .attr("cy",h4-(p4*6))
                .attr("r", function(d) {
                  return rScale(d.ENumber);
                })
                .on('mouseover', tool_tip.show)
                .on('mouseout', tool_tip.hide);;

            Pam.append("g")
                .append("text")
                .attr("transform","translate(" + (w4-((p4*2)+445)) + "," + (h4-(p4*6)) + ")")
                .attr("class","character-label")
                .text("Pam");

          });

      // Jim
      d3.tsv("spreadsheets/jim_rating.tsv", function(d, i, columns) {
        for (var i = 0, n = columns.length; i < n; ++i) {
          if (i == 0 || i == 2) {
            d[columns[i]] = +d[columns[i]];
          }
          // console.log(d);
          return d;
        }
      }, function(error, JimData) {
          if (error) throw error;

          var Jim = svg4
              .append("g")
              .attr("width",w4)
              .attr("height",(h4/4)-5);

          var tool_tip = d3.tip()
            .attr("class", "d3-tip")
            .offset([-8, 0])
            .html(function(d) { return "<strong>Episode</strong>: " + d.ENumber + ", " + d.EName + "</br>" + "<strong>Rating</strong>: " + d.Rating; });
          Jim.call(tool_tip);

          Jim.selectAll("circle")
              .data(JimData)
              .enter()
              .append("circle")
              .attr("cx",function(d) {
                  return xScale(d.Rating);
              })
              .attr("cy",h4-p4*8)
              .attr("r", function(d) {
                return rScale(d.ENumber);
              })
              .on('mouseover', tool_tip.show)
              .on('mouseout', tool_tip.hide);;

          Jim.append("g")
              .append("text")
              .attr("transform","translate(" + (w4-((p4*2)+445)) + "," + (h4-(p4*8)) + ")")
              .attr("class","character-label")
              .text("Jim");

        });
  });
