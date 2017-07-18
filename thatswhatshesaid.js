var width = 600;
var height = 400;
var padding = 60;

//Create svg element
var div1 = d3.select(".thats-what-she-said-container")

d3.tsv("spreadsheets/thatswhatshesaid_cleaned.tsv", function(data) {
  data.forEach(function(d) {
    d.Number = +d.Number;
    // console.log(d);
  });

  var block_left = div1
    .append("p")
    .selectAll("span")
    .data(data)
    .enter()
    .append("span")
    .attr("class",function(d){
      if(d.Number==1){
        return "season-episode-name";
      }
      else if(d.Number==2){
        return "character-name"
      }
    })
    .text(function(d){
      if (d.Number == 1){
        return d.SeasonEpisode + " ";
      }
      else if (d.Number == 2){
        return d.Character;
      }
      else {return ": " + d.Line + " ";
    }});


    // .selectAll("p")
    // .data(data)
    // .enter()
    // .append("p")
    // .attr("class",function(d) {
    //   if(d.Number==1){
    //     return "left-text";
    //   }
    // })
    // .text(function(d) {
    //   if (d.Number == 1){
    //     return d.Character + " " + d.Line + " ";
    //   }
    // })
    //
    // var block_right = div1
    //   .selectAll("p")
    //   .data(data)
    //   .enter()
    //   .append("p")
    //   .attr("class",function(d) {
    //     if(d.Number==3){
    //       return "right-text";
    //     }
    //   })
    //   .text(function(d) {
    //     if (d.Number == 3){
    //       return c.Character + " " + d.Line + " ";
    //     }
    //   })
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

});
