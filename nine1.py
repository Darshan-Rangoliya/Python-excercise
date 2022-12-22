from datetime import datetime,time,timedelta
import portion as p

start_time = input('Enter start time (DD-MM-YYYY H:M:S 24 hours):--> ')
end_time = input('Enter end time (DD-MM-YYYY H:M:S 24 hours)(End time must be greater):--> ')

start_time = datetime.strptime(start_time,'%d-%m-%Y %H:%M:%S')
end_time = datetime.strptime(end_time,'%d-%m-%Y %H:%M:%S')

# here we are getting the diff between strat date and end date so after geting the night einterval we can delete that interval from this diff
date_diff =  end_time-start_time

# here we created start and end interval of two dates
start_end_interval = p.closed(start_time,end_time)

night_dates = []

# here we are finding night intervals in list till end date
while start_time < end_time+timedelta(days=1):
    night_dates.append(p.closed(datetime.combine(start_time,time()),datetime.combine(start_time,time())+timedelta(hours=6)))
    start_time+=timedelta(days=1)

# here we got only 
tot_night = [start_end_interval&nights for nights in night_dates]

tot_del_time = timedelta(0)

for index in range(len(tot_night)):
    if tot_night[index].empty != True:
        tmp = tot_night[index].upper - tot_night[index].lower
        tot_del_time+=tmp

print('Total time between dates without night is {}'.format(date_diff-tot_del_time))