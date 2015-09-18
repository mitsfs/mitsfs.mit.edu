
//"start_date" "dtstart"
//"end_date" "dtend"
//"text" "summary"

scheduler.ical_frequencies = {
  YEARLY: "year",
  MONTHLY: "month",
  WEEKLY: "week",
  DAILY: "day",
  HOURLY: "hour",
  MINUTELY: "minute",
  SECONDLY: "second"
};

scheduler.ical = {
  parse:function(str){
    var calendar = new ICAL.Component(ICAL.parse(str));
    var events = calendar.getAllSubcomponents("vevent");
    var name = calendar.getFirstPropertyValue("x-wr-calname").toLowerCase().replace(/\s+/g, "_");
    array = [];
    for (var i = 0; i < events.length; i++) {
      var event = new ICAL.Event(events[i]);
      var newEvent = {
        text: event.summary,
        calendar_name: name,
        start_date: event.startDate.toJSDate(),
        end_date: event.endDate.toJSDate(),
        details: event.description,
        event_pid: 0
      };
      if (event.isRecurring()) {
        newEvent.id = event.uid;
        newEvent.event_length = event.duration.toSeconds();

        rrule = event.component.getFirstPropertyValue("rrule");

        if (rrule.until){
          newEvent.end_date = rrule.until.toJSDate();
        } else {
          newEvent.end_date = new Date();
          newEvent.end_date.setMonth(newEvent.end_date.getMonth()+4);
        }

        newEvent.rec_type = scheduler.ical_frequencies[rrule.freq] + "_";
        newEvent.rec_type += (rrule.interval || 1) + "_";
        newEvent.rec_type += "_";
        newEvent.rec_type += "_";
        if (rrule.parts["BYDAY"]){
          newEvent.rec_type += ICAL.Recur.icalDayToNumericDay(rrule.parts["BYDAY"]) - 1;
        }
         newEvent.rec_type += "#";

        exceptions = event.component.getAllProperties("exdate");
        for (var j = 0; j < exceptions.length; j++) {
          // Deletions
          var delDate = exceptions[j].getFirstValue();
          var delEvent = {
            start_date: delDate.toJSDate(),
            end_date: delDate.toJSDate(),
            event_length: delDate.toUnixTime(),
            event_pid: event.uid,
            text: newEvent.text,
            rec_type: "none"
          };
          array.push(delEvent);
        }
      } else if (event.isRecurrenceException()){
        newEvent.event_pid = event.uid;
        newEvent.event_length = event.recurrenceId.toUnixTime();
      } else {
        // Don't need anything special for basic events        
      }
      array.push(newEvent);
    }

    return array.reverse();

    }
};

scheduler.templates.event_class = function(start, end, ev){
  var css = ev.calendar_name;
  if (ev.text.match(/^Canceled|XXX/)){
    css += " canceled_hours";
  }
  return css;
};