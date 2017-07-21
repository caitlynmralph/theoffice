var width = 1000;
var height = 1000;
var padding = 60;

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
      else {
        return "thats-what-she-said-text"
      }
    })
    .text(function(d) {
      if (d.value != 0) {
        return d.value.slice(3) + "\n";
      }
    });

  // var block_left = div1
  //     .append("p")
  //     .selectAll("span")
  //     .data(data)
  //     .enter()
  //     .append("span")
  //     .attr("class",function(d){
  //       if(d.Number==1){
  //         return "season-episode-name";
  //       }
  //       else if(d.Number==2){
  //         return "character-name"
  //       }
  //     })
  //     .text(function(d){
  //       if (d.Number == 1){
  //         return d.SeasonEpisode + " ";
  //       }
  //       else if (d.Number == 2){
  //         return d.Character;
  //       }
  //       else {return ": " + d.Line + " ";
  //     }});

//card design

  // var jokeDiv = d3.select(".thats-what-she-said-container")
  //   .selectAll("div")
  //   .data(data)
  //   .enter()
  //   .append("div")
  //   .attr("class","joke-div");
  //
  // var jokeSvg = jokeDiv
  //   .append('svg')
  //   .attr('width', width)
  //   .attr('height', function(d) {
  //     if(d.Line2 == 0) {
  //       return 60;
  //     }
  //     else if(d.Line3 == 0) {
  //       return 130;
  //     }
  //     else if(d.Line4 == 0) {
  //       return 180;
  //     }
  //     // else if(d.Line5 == 0) {
  //     //   return 320;
  //     // }
  //     // else if(d.Line5 == 0) {
  //     //   return 400;
  //     // }
  //     // else {
  //     //   return 480;
  //     // }
  //   });
  //
  //   jokeSvg
  //     .selectAll("circle")
  //     .data(function(d) {return keys.map(function(key) { return {key: key, value: d[key]}; }); })
  //     .enter()
  //     .append("circle")
  //     .attr("class","image")
  //     .attr("cx",40)
  //     .attr("cy",function(d) {
  //       if (d.value[1]==1) {
  //         return (d.value[1] * 40);
  //       }
  //       else if (d.value[1]==2) {
  //         return (d.value[1] * 40 + 10);
  //       }
  //       else if (d.value[1]==3) {
  //         return (d.value[1] * 40 + 20);
  //       }
  //     })
  //     .attr("r",20)
  //     .style("fill", function(d) {
  //       if (d.value == 0) {
  //         return "transparent";
  //       }
  //       else if (d.value[3] == 1) {
  //         return "url(#michael-image)";
  //       }
  //       else if (d.value[3] == 2) {
  //         return "url(#jim-image)";
  //       }
  //       else if (d.value[3] == 3) {
  //         return "url(#pam-image)";
  //       }
  //       else if (d.value[3] == 4) {
  //         return "url(#dwight-image)";
  //       }
  //       else if (d.value[3] == 5) {
  //         return "url(#kevin-image)";
  //       }
  //       else if (d.value[3] == 6) {
  //         return "url(#doctor-image)";
  //       }
  //       else {
  //         return "url(#michael-image)";
  //       }
  //     })
  //     .style("stroke", function(d) {
  //       if (d.value == 0) {
  //         return "transparent";
  //       }
  //     });
  //
  //     var jokes = jokeSvg
  //       .append("g")
  //
  //     jokes
  //       .selectAll("text")
  //       .data(function(d) {return keys.map(function(key) { return {key: key, value: d[key]}; }); })
  //       .enter()
  //       .append("text")
  //       .attr("class","lines")
  //       // .attr("x",80)
  //       .attr("transform",function(d) {
  //         if (d.value[1]==1) {
  //           return "translate(" + (80) + "," + (d.value[1] * 40 + 7) + ")";
  //         }
  //         else if (d.value[1]==2) {
  //           return "translate(" + (80) + "," + (d.value[1] * 40 + 17) + ")";
  //         }
  //         else if (d.value[1]==3) {
  //           return "translate(" + (80) + "," + (d.value[1] * 40 + 27) + ")";
  //         }})
  //       .text(function(d){
  //         if (d.value != 0) {
  //           return d.value.slice(6,-2);
  //       }
  //       });


  // block_left.selectAll("p")
  //    .data(data)
  //    .enter()
  //    .append("p")
  //    .attr("class",function(d) {
  //      if(d.Number==3){
  //        return "right-text";
  //      }
  //    })
  //   .text("hello");

  // var block_right = div1
  //   .selectAll("svg")
  //   .data(data)
  //   .enter()
  //   .append("svg")
  //   .attr("class",function(d) {
  //     if(d.Number==3){
  //       return "right-text";
  //     }
  //   });
  //
  //   var block_shesaid = div1
  //     .selectAll("p")
  //     .data(data)
  //     .enter()
  //     .append("p")
  //     .attr("class",function(d) {
  //       if(d.Number==3){
  //         return "she-said-text";
  //       }
  //     })
  //     .text(function(d) {
  //       if (d.Number == 2){
  //         return " " + d.Line + " ";
  //       }
  //     })


    // .append("p")
    // .selectAll("span")
    // .data(data)
    // .enter()
    // .append("span")
    // .attr("class",function(d){
    //   if(d.Number==1){
    //     return "season-episode-name";
    //   }
    //   else if(d.Number==2){
    //     return "character-name"
    //   }
    // })
    // .text(function(d){
    //   if (d.Number == 1){
    //     return d.SeasonEpisode + " ";
    //   }
    //   else if (d.Number == 2){
    //     return d.Character;
    //   }
    //   else {return ": " + d.Line + " ";
    // }});

});
