import subprocess
import os
import json

class ExifTool(object):

    sentinel = "{ready}\n"

    def __init__(self, executable = os.chdir(os.path.abspath(__file__)[0:os.path.abspath(__file__).rfind('\\')]) + "exiftool.exe"):
        self.executable = executable

    def __enter__(self):
        self.process = subprocess.Popen(
            [self.executable,  "-@", "-"],
            stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        return self

    def  __exit__(self, exc_type, exc_value, traceback):
        self.process.stdin.write("-stay_open\nFalse\n")
        self.process.stdin.flush()

    def execute(self, *args):
        args = args + ("-execute\n",)
        self.process.stdin.write(str.join("\n", args))
        self.process.stdin.flush()
        output = ""
        fd = self.process.stdout.fileno()
        while not output.endswith(self.sentinel):
            output += os.read(fd, 4096)
        return output[:-len(self.sentinel)]

    def get_metadata(self, *filenames):
        return json.loads(self.execute("-G", "-j", "-n", *filenames))


def getEXIFTags(file_name):
    #NOT WORKING!!!! call fuctions to get json Tags
    with ExifTool() as e:
        metadata = e.get_metadata(file_name)
    return metadata


def setEXIFTag(file_name, tag='comment', info='GIMP Python Script Created with '):
    #NOT WORKING!!! set tag and return true if successful
    from subprocess import call
    import os
    os.chdir(os.path.abspath(__file__)[0:os.path.abspath(__file__).rfind('\\')])
    return call('exiftool.exe -set' + file_name + ' ' + tag + ' ' + info)
