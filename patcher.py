import subprocess,tempfile
def apply(diff):
    with tempfile.NamedTemporaryFile("w",delete=False) as f:
        f.write(diff)
        subprocess.run(["git","apply",f.name],check=True)