import subprocess
import sys
import os

def print_style_check(jar_path, xml_path, code_path):
    fun = 'com.puppycrawl.tools.checkstyle.Main'
    style = subprocess.run(
        ['java', '-cp', jar_path, fun, '-c', xml_path, code_path],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    if style.returncode >= 254:
        print('could not find input files')
    elif style.returncode == 0:
        print('passed all style checks')
    else:
        print(style.stdout.decode('utf_8').strip())

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('style_check.py expects 1 arg: path to folder for style check')
    else:
        py_fpath = sys.argv[0]
        paths = py_fpath.rsplit('/', 1)
        prefix = '' if len(paths) == 1 else (paths[0] + os.sep)
        jar_path = prefix + 'checkstyle-8.23-all.jar'
        xml_path = prefix + 'style.xml'
        if not os.path.exists(jar_path):
            print('could not find %s' % jar_path)
        elif not os.path.exists(xml_path):
            print('could not find %s' % xml_path)
        else:
            print_style_check(jar_path, xml_path, sys.argv[1])