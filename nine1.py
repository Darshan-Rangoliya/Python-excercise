from datetime import datetime,time,timedelta
import portion as p

start_time = input('Enter start time (DD-MM-YYYY H:M:S 24 hours):--> ')
end_time = input('Enter end time (DD-MM-YYYY H:M:S 24 hours)(End time must be greater):--> ')

start_time = datetime.strptime(start_time,'%d-%m-%Y %H:%M:%S')
end_time = datetime.strptime(end_time,'%d-%m-%Y %H:%M:%S')

# start_time = datetime.strptime('18-12-2022 5:30:00','%d-%m-%Y %H:%M:%S')
# end_time = datetime.strptime('19-12-2022 16:00:00','%d-%m-%Y %H:%M:%S')


date_diff =  end_time-start_time

start_end_interval = p.closed(start_time,end_time)

night_dates = []

while start_time < end_time+timedelta(days=1):
    night_dates.append(p.closed(datetime.combine(start_time,time()),datetime.combine(start_time,time())+timedelta(hours=6)))
    start_time+=timedelta(days=1)


tot_night = []

for nights in night_dates:
    tot_night.append(start_end_interval&nights)


tot_del_time = timedelta(0)

for i in range(len(tot_night)):
    if tot_night[i].empty != True:
        tmp = tot_night[i].upper- tot_night[i].lower
        tot_del_time+=tmp

print('Total time between dates without night is {}'.format(date_diff-tot_del_time))