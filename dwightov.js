var w5 = 600;
var h5 = 500;
// var padding = 50;
var transitionDuration = 1000;

var div5 = d3.select(".dwightov-container")
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

    document.getElementById("generate").onclick = function() {
      response = "\n" + " " + dataset[getRandomInt(0,dataset.length)].line
      document.getElementById("response").innerHTML = response;
    }

  });
