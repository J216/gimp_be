def archiveExports(folder=""):
    from os import makedirs, rename, chdir, listdir
    from os.path import exists
    from datetime import date
    if not folder == "":
        chdir(folder)
    directory='./'+str(date.today()).replace('-','')
    if not exists(directory):
        makedirs(directory)
    for file in listdir('.'):
        if '.png' in  file or '.jpg' in file:
            rename(file,directory+'/'+file)


def qA():
    archiveExports()


