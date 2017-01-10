#log for script writes x number of lines and then writes to file, see logDump()
log_run = 0
log_temp = ""
log_folder="c:/scr/"
logging=0
def doLog(log_event):
    global log_run
    global log_temp
    global log_folder
    global logging
    if logging:
        os.chdir(log_folder)
        log_string = ''
        dates = datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S')
        if not log_event == 'Log dump':
            log_event = '\n' + dates + '  *  ' + log_event
            log_temp=str(log_temp) + str(log_event)
        if log_run >= 10:
            for log_line in log_temp:
                log_string = log_string + log_line
            try:
                file_name = "painting-log-" + host_name + '-' + dates[:4] + dates[5:7] + dates[8:10] + ".txt"
                with open(file_name, "a") as myfile:
                    myfile.write(log_string)
                log_run = 0
                log_temp = []
                return (1, log_event)
            except:
                return (0, file_name)
        else:
            log_run = log_run + 1
            return (1, 'temp')
    else:
        return (0, 'logging off')


#writes log to file
def logDump():
    global log_run
    log_run = 100
    doLog('Log dump')
