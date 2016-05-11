  scheduler.config.show_loading = true;
  scheduler.config.readonly = true;
  scheduler.config.first_hour = 9;
  scheduler.config.last_hour = 24;
  scheduler.config.show_quick_info = false;
  scheduler.config.occurrence_timestamp_in_utc = true;
  scheduler.config.day_date = "%D %m/%d";
  scheduler.config.default_date = "%l, %M-%d, %Y";
  dhtmlXTooltip.config.className = 'dhtmlXTooltip tooltip'; 
  scheduler.templates.tooltip_text = function(start,end,event) {
    if (event.calendar_name === "mitsfs_events"){
      return "<h4>"+event.text+"</h4><strong>Where:</strong> "+event.location + "<br><strong>Details:</strong> " + event.details;
    } else {
      return null; 
    }
  };
  scheduler.templates.week_date = function(start, end){
    var d=scheduler.date.date_to_str;
    end = scheduler.date.add(end,-1,"day");
    if (start.getFullYear() !== end.getFullYear()){
      return d("%M %d, %Y")(start) + " &ndash; "+ d("%M %d, %Y")(end);
    } else if (start.getMonth() !== end.getMonth()){
      return d("%M %d")(start) + " &ndash; "+ d("%M %d, %Y")(end);
    } else {
      return d("%M %d")(start) + " &ndash; "+ d("%d, %Y")(end);
    }
  };
  scheduler.templates.day_scale_date = function(date){
    return scheduler.date.date_to_str("%D %m/%d")(date);
  };

 function getUrlParameter(sParam) {
  var sPageURL = decodeURIComponent(window.location.search.substring(1)),
  sURLVariables = sPageURL.split('&'),
  sParameterName,
  i;
  for (i = 0; i < sURLVariables.length; i++) {
    sParameterName = sURLVariables[i].split('=');
    if (sParameterName[0] === sParam) {
      return sParameterName[1] === undefined ? true : sParameterName[1];
    }
  }
}

function getCalendarOffsetFromParam(param){
  var offset = parseInt(getUrlParameter('date'), 10);
  var now = new Date();
  now.setDate(now.getDate()+offset);
  return now;
}