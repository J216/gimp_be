

def qRC(opt='0',ftp_home="." ):
    if opt =='0':
        global session
        session = ftplib.FTP('<IP-HERE>','<USERNAME-HERE','<PW_HERE>')
        if not ftp_home == ".":
            session.cwd(ftp_home)
    print 'FTP Connected'
    return session


def listFTPFolders(ftp=''):
    if ftp == '':
        ftp = qRC()
    files=[]
    for file in ftp.nlst():
        if not '.' in file:
            files.append(file)
    return files


def listFTPFiles(ftp=0):
    if ftp == '':
        ftp = qRC()
    files=[]
    for file in ftp.nlst():
        if '.' in file:
            files.append(file)
    return files


def qLS():
    ftp = qRC()
    files = []
    for ftp_folder in listFTPFolders(ftp):
        files.append(ftp_folder)
    for ftp_file in listFTPFiles(ftp):
        files.append(ftp_file)
    return files

def uploadFile(file_name="", ftp=0):
    status=''
    if ftp==0:
        ftp = qRC()
    if file_name == "":
        file_name=choice(os.path.listdir('.'))
    ftp_file = open(file_name, 'rb')
    status = ftp.storbinary('STOR '+file_name, ftp_file)
    ftp_file.close()
    ftp.quit()
    print status
    return status


def uploadFiles(ul_files=[],remove=0):
    statuses=[]
    if ul_files == []:
        ul_files=os.listdir('.')
    for ul_file in ul_files:
        if '.png' in ul_file or '.jpg' in ul_file:
            cur_status = uploadFile(ul_file)
            statuses.append(cur_status)
            if remove=='YES' and '226' in cur_status:
                os.remove(ul_file)
    return statuses

