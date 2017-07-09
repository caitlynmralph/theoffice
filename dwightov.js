var wi = 600;
var he = 500;
var padding = 50;

var div3 = d3.select(".dwightov-container")
  .append("div");

function getRandomInt(min, max) {
  min = Math.ceil(min);
  max = Math.floor(max);
  return Math.floor(Math.random() * (max - min)) + min;
}

d3.tsv("spreadsheets/dwight_markov_tweets.tsv", function(d, i, columns) {
  for (var i = 0, n = columns.length; i < n; ++i) {
    // console.log(d.line);
    return d;
  }
  }, function(error, dataset) {
    if (error) throw error;

    var svg3 = div3
        .append("svg")
        .attr("width",wi)
        .attr("height",he);

    var response = svg3
        .append("g");

    var button = svg3
        .append("rect")
        .attr("x", wi-((padding*2)+500))
        .attr("y",padding/2+10)
        .attr("rx", 6)
        .attr("ry", 6)
        .attr("width",90)
        .attr("height",35)
        .attr("class","button");

    var buttontext = svg3
        .append("g");

    buttontext.append("text")
        .attr("x", wi-((padding*2)+493))
        .attr("y",padding/2+32)
        .attr("width",90)
        .attr("height",35)
        .attr("class","button-text")
        .text("GENERATE")
        .on('click', function() {
          response.append("text")
            .attr("x", wi-((padding*2)+500))
            .attr("y",padding/2+80)
            .attr("width",600)
            .attr("height",40)
            .attr("class","response-text")
            .style("background-color","white")
            .text(dataset[getRandomInt(0,dataset.length)].line);
        });


    // var block = div3
    //   .append("p")
    //   .selectAll("span")
    //   .data(dataset)
    //   .enter()
    //   .append("span")
    //   .text(function(d) {
    //     return d.line;
    //   });

  });
