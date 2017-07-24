var w1 = 1000;
var h1 = 1000;
var p1 = 60;

var div1 = d3.select(".thats-what-she-said-container");

d3.tsv("spreadsheets/thatswhatshesaid_cleaned_new.tsv", function(data) {
  data.forEach(function(d) {
      d.Number = +d.Number;
      // console.log(d.Line1);
      // console.log(d.Line1[1]);
      // console.log(d.Line1[3]);
      // console.log(d.Line1.slice(6,-2));
      // console.log(d);

  });

  var keys = data.columns.slice(1);

  var jokeDiv = d3.select(".thats-what-she-said-container")
    .selectAll("div")
    .data(data)
    .enter()
    .append("div")
    .attr("class","joke-div");

  jokeDiv.append("p")
    .attr("class","line-container")
    .selectAll("span")
    .data(function(d) {return keys.map(function(key) { return {key: key, value: d[key]}; }); })
    .enter()
    .append("span")
    .attr("class",function(d) {
      if(d.value[2] == 0) {
        return "lines";
      }
      else if (d.value[2] == 1){
        return "thats-what-she-said-text"
      }
    })
    .style("background-image",function(d) {
      if (d.value[1] == 1) {
      return 'url("pictures/michael.png")';
      }
      else if (d.value[1] == 2){
        return 'url("pictures/jim.png")';
      }
      else if (d.value[1] == 3){
        return 'url("pictures/pam.png")';
      }
      else if (d.value[1] == 4){
        return 'url("pictures/dwight.png")';
      }
      else if (d.value[1] == 5) {
        return 'url("pictures/kevin.png")';
      }
      else if (d.value[1] == 6) {
        return 'url("pictures/doctor.png")';
      }
      else if (d.value[1] == 7) {
        return 'url("pictures/oscar.png")';
      }
      else if (d.value[1] == 8) {
        return 'url("pictures/angela.png")';
      }
      else if (d.value[1] == 9) {
        return 'url("pictures/stanley.png")';
      }
      else if (d.value[1] == "&") {
        return 'url("pictures/benihana_waitress.png")';
      }
      else if (d.value[1] == "!") {
        return 'url("pictures/jan.png")';
      }
      else if (d.value[1] == "?") {
        return 'url("pictures/everyone.png")';
      }
      else if (d.value[1] == "+") {
        return 'url("pictures/lawyer.png")';
      }
      else if (d.value[1] == "=") {
        return 'url("pictures/deposition_reporter.png")';
      }
      else if (d.value[1] == "@") {
        return 'url("pictures/holly.png")';
      }
      else if (d.value[1] == "$") {
        return 'url("pictures/kelly.png")';
      }
      else if (d.value[1] == "%") {
        return 'url("pictures/david.png")';
      }
      else if (d.value[1] == "*") {
        return 'url("pictures/darryl.png")';
      }
      else if (d.value[1] == "~") {
        return 'url("pictures/gabe.png")';
      }
      else if (d.value[1] == "^") {
        return 'url("pictures/ricky.png")';
      }
      else if (d.value[1] == "|") {
        return 'url("pictures/clark.png")';
      }
      else if (d.value[1] == ">") {
        return 'url("pictures/creed.png")';
      }
    })
    .text(function(d) {
      if (d.value != 0) {
        return d.value.slice(3) + "\n";
      }
    });

});
