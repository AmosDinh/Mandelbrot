
from os import strerror
import eel
import subprocess


command = """cd "c:/Users/amos/Documents/Programmieren/a2_FunThingsIdidOnce/MathPictures/" && g++ test2.cpp -o test2 && "c:/Users/amos/Documents/Programmieren/a2_FunThingsIdidOnce/MathPictures/" test2"""
# command = """python threading_picture.py"""
command1 = r'''cd "c:\Users\amos\Documents\Programmieren\a2_FunThingsIdidOnce\MathPictures\" && g++ test2.cpp -o test2 && "c:\Users\amos\Documents\Programmieren\a2_FunThingsIdidOnce\MathPictures\"test2'''
command2 = """python threading_picture.py"""
print()

def run_win_cmd(cmd):
    result = []
    process = subprocess.Popen(cmd,
                               shell=True,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)
    for line in process.stdout:
        result.append(line)
    errcode = process.returncode
    for line in result:
        print(line)
    if errcode is not None:
        raise Exception('cmd %s failed, see above for details', cmd)
# proc = subprocess.Popen('cmd.exe', stdin = subprocess.PIPE, stdout = subprocess.PIPE)
# stdout, stderr = proc.communicate(command.encode('utf-8'))

# print(stdout,stderr)

run_win_cmd(command1)
run_win_cmd(command2)

@eel.expose
def call_cpp(): 
    print("abc")

@eel.expose
def from_js(xrel,yrel):
    print(xrel,yrel)

if __name__ == '__main__':
    eel.init('web')
    eel.start('index.html',  options={'mode': 'default'}, suppress_error=True)

    # python -m eel Heilpraxis_Rechnungsschreiber.py web