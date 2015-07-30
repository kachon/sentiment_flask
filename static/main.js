$(document).ready(function(){



var pie_data = [
    {
        value: 300,
        color:"#F7464A",
        highlight: "#FF5A5E",
        label: "Red"
    },
    {
        value: 50,
        color: "#46BFBD",
        highlight: "#5AD3D1",
        label: "Green"
    },
    {
        value: 100,
        color: "#FDB45C",
        highlight: "#FFC870",
        label: "Yellow"
    }
]


    $("#submit_btn").click(function(){
      var channel_id = $("#channel_id").val()
      alert("got it " + channel_id);
      console.log("fasfda channel_id " + channel_id);

      $(".video_row").remove();

    $.get( "/predict_channel/"+channel_id, function( data ) {
        var results = data["results"]
        console.log("results.length " + results.length)

        for (i=0; i < results.length; i++) {
          console.log(results[i]);

          var vid = results[i]["vid"]
          var url = "https://www.youtube.com/embed/" + vid
          var comment = results[i]["comment"] 
          var chart1id = "chart_" + i + "_1"
          var chart2id = "chart_" + i + "_2"
          var html = 
                  '<div class="row video_row" style="margin-top:40px"> \
                    <div class="form-group col-sm-4" style="max-height:250px;"> \
                      <div style="max-width:560px;margin:0 auto;"> \
                         <div style="position: relative;padding-bottom: 56.25%; height: 0; overflow: hidden;"> \
                          <iframe width="380" height="300" frameborder="0" src="https://www.youtube.com/embed/VID" frameborder="0" allowfullscreen="" style="position: absolute; top: 0px; left: 0px; width: 100%; height: 100%; max-width: 560px; max-height: 315px;"></iframe>  \
                         </div> \
                      </div> \
                    </div>  \
                    <div class="col-sm-2" style="max-height:250px; overflow-y:auto;"> \
                      <p style="word-wrap: break-word;">COMMENT</p> \
                    </div> \
                    <div class="col-sm-3"> \
                      <canvas id="CHARTID1" width="500" height="500" style="width: 100%; height: 100%; max-width: 500; max-height: 500px;"></canvas> \
                    </div> \
                    <div class="col-sm-3"> \
                      <canvas id="CHARTID2" width="500" height="500" style="width: 100%; height: 100%; max-width: 500; max-height: 500px;"></canvas> \
                    </div> \
                  </div>';

    //       var html = 
    //                 '<div class="col-sm-4" style="background-color:lavender;">.col-sm-4</div>\
    // <div class="col-sm-2" style="background-color:lavenderblush;">.col-sm-4</div>\
    // <div class="col-sm-6" style="background-color:lavender;">.col-sm-4</div>'
          var html = html.replace("VID", vid);
          var html = html.replace("COMMENT", comment);
          var html = html.replace("CHARTID1", chart1id);
          var html = html.replace("CHARTID2", chart2id);
          $( "#video_container" ).append( html ); 

          var ctx1 = $("#"+chart1id).get(0).getContext("2d");
          var ctx2 = $("#"+chart2id).get(0).getContext("2d");
          var proba1 = results[i]["proba"]
          var pie_data = [
              {
                  value: proba1[0]*100,
                  color:"#F7464A",
                  highlight: "#FF5A5E",
                  label: "Negative"
              },
              {
                  value: proba1[1]*100,
                  color: "#46BFBD",
                  highlight: "#5AD3D1",
                  label: "Postive"
              },
          ]

          var myPieChart1 = new Chart(ctx1).Pie(pie_data,{});
          var myPieChart2 = new Chart(ctx2).Pie(pie_data,{});
          // var ctx2 = $("#chart1").get(0).getContext("2d");
          // var myPieChart2 = new Chart(ctx2).Pie(data,{});
        }
      }
    );

  });
}); 