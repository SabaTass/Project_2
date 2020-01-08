new d3plus.Geomap()
  .data("/API/Wake_Fatals_map")
  .groupBy("Index")
  .colorScale("dma_code")
  .colorScaleConfig({
    color: ["red", "orange", "yellow", "green", "blue"]
  })
  .label(function(d) {
    return "Year" + d.Year + ", " + "Fatalities"+ d.Fatals;
  })
  .point(function(d) {
    return [d.Longitude, d.Latitude];
  })
  .render();