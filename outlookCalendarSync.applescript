-- Export Outlook events for today and the next 30 days to Apple Calendar "Work"

-- Set date range
set today to (current date) - (1 * days)
set endDate to today + (31 * days)

-- Access Apple Calendar
tell application "Calendar"
	set workCalendar to calendar "Work"
	
	-- Delete previously synced events
	set oldEvents to every event of workCalendar whose start date is greater than today and start date is less than endDate and description contains "Synced from Outlook"
	repeat with oldEvent in oldEvents
		delete oldEvent
	end repeat
end tell

-- Access Microsoft Outlook
tell application "Microsoft Outlook"
	set eventList to calendar events whose start time is greater than today and start time is less than endDate
	
	repeat with outlookEvent in eventList
		set eventTitle to subject of outlookEvent
		set eventStart to start time of outlookEvent
		set eventEnd to end time of outlookEvent
		set eventAllDay to all day flag of outlookEvent
		set eventDescription to "Synced from Outlook"
		
		-- Safely get properties, fallback to empty string if missing
		set eventLocation to location of outlookEvent
		if eventLocation is missing value then set eventLocation to ""
		
		-- Create the event in Apple Calendar
		tell application "Calendar"
			tell workCalendar
				if eventAllDay then
					make new event at end with properties {summary:eventTitle, start date:eventStart, end date:eventEnd - 1 * days, allday event:true, location:eventLocation, description:eventDescription}
				else
					make new event at end with properties {summary:eventTitle, start date:eventStart, end date:eventEnd, location:eventLocation, description:eventDescription}
				end if
			end tell
		end tell
	end repeat
end tell

display notification "Export complete!" with title "Outlook to Apple Calendar Sync"
