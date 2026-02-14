import subprocess
def validate():
    return subprocess.run(["npm","test"]).returncode==0