from crontab import CronTab
 
my_cron = CronTab(user='')
job = my_cron.new(command='C:\python\bot')
job.minute.every(1)
 
my_cron.write()
