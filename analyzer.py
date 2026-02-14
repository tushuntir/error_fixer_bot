import subprocess,re

def analyze():
    p = subprocess.run(["npm","run","lint"],capture_output=True,text=True)
    errors = {}
    for l in p.stdout.splitlines():
        m = re.search(r"(src/.*?\.(js|ts))",l)
        if m:
            errors.setdefault(m.group(1),[]).append(l)
    return errors