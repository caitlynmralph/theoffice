var wi = 600;
var he = 400;
var padding = 60;

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
        .range([padding,wi-padding*2]);
    var rScale = d3.scaleLinear()
        .domain([0,d3.max(dataset, function(d) { return d.Rating;})])
        .range([2,5]);
    var xAxis = d3.axisBottom(xScale)
        .tickSize([0])
        .tickValues(xScale.domain());

    var svg2 = div2
        .append("svg")
        .attr("width",wi)
        .attr("height",he);

    svg2.append("g")
        .attr("transform","translate(0," + (he - padding) + ")")
        .call(xAxis);

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
            .attr("height",he/4);

        Andy.selectAll("circle")
            .data(AndyData)
            .enter()
            .append("circle")
            .attr("cx",function(d) {
                return xScale(d.Rating); //Bar width of 20 plus 1 for padding
            })
            .attr("cy",he)
            .attr("r", function(d) {
              return rScale(d.Rating);
            });

      });

      // Jim
      // d3.tsv("spreadsheets/jim_rating.tsv", function(d, i, columns) {
      //   for (var i = 0, n = columns.length; i < n; ++i) {
      //     if (i == 0 || i == 2) {
      //       d[columns[i]] = +d[columns[i]];
      //     }
      //     console.log(d);
      //     return d;
      //   }
      // }, function(error, AndyData) {
      //     if (error) throw error;
      //
      //     var Jim = svg2
      //         .append("g")
      //         .attr("width",wi)
      //         .attr("height",(he/4)-5);
      //
      //     Jim.selectAll("circle")
      //         .data(AndyData)
      //         .enter()
      //         .append("circle")
      //         .attr("cx",function(d) {
      //             return xScale(d.Rating); //Bar width of 20 plus 1 for padding
      //         })
      //         .attr("cy",he-padding*2)
      //         .attr("r", function(d) {
      //           return rScale(d.Rating);
      //         });
      //
      //   });
  });
