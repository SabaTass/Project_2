var getData = $.get('/API/NC_Fatal_byMonth');
    getData.done(function(results){
        // console.log(results); 

    var s1 = results.map(results => results.Fatals);
    
        console.log(s1); 
  
    // ################################################################
    var data = {
        // A labels array that can contain any sort of values
        labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
        // Our series array that contains series objects or in this case series data arrays
        // series: [[323,328,347,357,363,392,344,334,371,439,372,323]]
            // series: [[s1],[s2]]
            series: [s1]
            // series: [s2]
        };
       
        var options = {
          width : 1000,
          height : 600,
        //   fullWidth: true
        }
      // Create a new line chart object where as first parameter we pass in a selector
      // that is resolving to our chart container element. The Second parameter
      // is the actual data object.
      new Chartist.Line('#ct-chart', data, options);   


      var s2 = results.map(results => results.Persons);
      console.log(s2); 
        var data2 = {
            // A labels array that can contain any sort of values
            labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
            // Our series array that contains series objects or in this case series data arrays
            // series: [[323,328,347,357,363,392,344,334,371,439,372,323]]
                // series: [[s1],[s2]]
                // series: [s1]
                series: [s2]
            };
           
            var options = {
              width : 1000,
              height : 600,
            //   fullWidth: true
            }
        // ################################################################
        // Create a new line chart object where as first parameter we pass in a selector
        // that is resolving to our chart container element. The Second parameter
        // is the actual data object.
        new Chartist.Line('.ct-chart', data2, options); 

        });

    // =================================================================================
var getData3 = $.get('/API/NC_Fatal_byHour');
    getData3.done(function(results3){
        var s3 = results3.map(results3 => results3.Fatals); 
            console.log(s3);   
        // ################################################################
        var data3 = {
            // A labels array that can contain any sort of values
            labels: ['12am', '1am', '2am', '3am', '4am', '5am', '6am', '7am', '8am', '9am', '10am', '11am','12pm',
            '1pm', '2pm', '3pm', '4pm', '5pm', '6pm', '7pm', '8pm', '9pm', '10pm', '11pm', '12pm'],
            // Our series array that contains series objects or in this case series data arrays
            // series: [[323,328,347,357,363,392,344,334,371,439,372,323]]
                // series: [[s1],[s2]]
                series: [s3]
            };
        
            var options = {
            width : 1000,
            height : 600,
            //   fullWidth: true
            }
        // Create a new line chart object where as first parameter we pass in a selector
        // that is resolving to our chart container element. The Second parameter
        // is the actual data object.
        new Chartist.Line('.ct-chart3', data3, options);   

        });