
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

function convertDate(d, tz){
  if (d.zone != ICAL.Timezone.localTimezone) {
      d = d.convertToZone(tz);
      d.zone = ICAL.Timezone.localTimezone;
  }
  return d.toJSDate();
}

scheduler.ical = {
  parse:function(str){
    var calendar = new ICAL.Component(ICAL.parse(str));
    var events = calendar.getAllSubcomponents("vevent");
    var name = calendar.getFirstPropertyValue("x-wr-calname").toLowerCase().replace(/\s+/g, "_");
    var vtimezones = calendar.getAllSubcomponents('vtimezone');
    var tz = ICAL.Timezone.utcTimezone;
    for (var i = 0; i < vtimezones.length; i++){
      timezone = new ICAL.Timezone(vtimezones[i]);
      if (timezone.tzid == "America/New_York") {
        tz = timezone;
      }
    }

    array = [];
    for (var i = 0; i < events.length; i++) {
      var event = new ICAL.Event(events[i]);
      var newEvent = {
        text: event.summary,
        calendar_name: name,
        start_date: convertDate(event.startDate, tz),
        end_date: convertDate(event.endDate, tz),
        details: event.description,
        location: event.location,
        event_pid: 0
      };
      if (event.isRecurring()) {
        newEvent.id = event.uid;
        newEvent.event_length = event.duration.toSeconds();

        rrule = event.component.getFirstPropertyValue("rrule");

        if (rrule.until){
          // The recurrence library already calculates TZ offsets so we need to undo this effect
          var ed = convertDate(rrule.until, tz);
          var offset = newEvent.start_date.getTimezoneOffset() - ed.getTimezoneOffset();
          ed.setMinutes(ed.getMinutes() - offset);
          ed.setSeconds(ed.getSeconds() + newEvent.event_length);
          newEvent.end_date = ed;
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
            start_date: convertDate(delDate, tz),
            end_date: convertDate(delDate, tz),
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
