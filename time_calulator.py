def add_time(time, time1, day=None):
    start_time, meridian = time.split()
    start_hour, start_minute = [int(x) for x in start_time.split(":")]
    duration_hour, duration_minute = [int(x) for x in time1.split(":")]
    if day:
        day = day.capitalize()

    if meridian == 'PM':
        start_hour += 12

    startM += duration_minute
    startH += (startM//60)
    startM = startM % 60
    startH += duration_hour
    nextday_counter = start_hour // 24
    start_hour = start_hour % 24

    newTime = ''
    if startH < 11:
        newMeridian = 'AM' 
    else: 
        newMeridian = 'PM'
    if startH > 12 :
        startH -= 12
    if startH != 0:
        newTime += (str(startH)  
    else:
         newTime = '12')+':'
    newTime += (str(startM if startM >
                 9 else "0"+str(startM))) + " "
    newTime += newMeridian
    if(day):
        weekday = ['Monday', 'Tuesday',
                            'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        dayIndex = weekday.index(day)
        nextdayIndex = (dayIndex + nextday_counter) % 7
        newTime += (", " + weekday[nextdayIndex])
    if(nextday_counter != 0):
        newTime += " " + (
            f'({nextday_counter} days later)'
            if nextday_counter > 1 else
            '(next day)'
        )

    return newTime

print(add_time('11:30 AM', '3:10'))
print(add_time("3:00 AM", "3:10", 'monday'))
