
def setProjectPath(path_in):
    global project_path
    project_path=path_in


def getProjectPath():
    global project_path
    return project_path


def setProjectFile(file_in):
    global project_file
    global project_path
    project_file=project_path+file_in


def getProjectFile():
    global project_file
    return project_file


def setExportPath(path_in):
    global export_path
    export_path=path_in


def getExportPath():
    global export_path
    return export_path


def setExportFile(file_in):
    global export_file_name
    global export_path
    export_file_name=export_path+file_in


def getExportFile():
    global export_file_name
    return export_file_name


def setAuthor(author_name):
    global function_parameters
    function_parameters.extend(('setAuthor','str','null'))
    global author
    author = author_name
    doLog('setAuthor('+author_name+')')


def getAuthor():
    global function_parameters
    function_parameters.extend(('getAuthor','str'))
    global author
    return author

