  scheduler.config.show_loading = true;
  scheduler.config.readonly = true;
  scheduler.config.first_hour = 12;
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