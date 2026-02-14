from repo_manager import snapshot,rollback
from analyzer import analyze
from groq_fixer import patch
from patcher import apply
from validator import validate
from pathlib import Path
import subprocess

def repair():
    snapshot()
    errors=analyze()
    if not errors:
        return "CLEAN"
    for file,logs in errors.items():
        code=Path(file).read_text()
        diff=patch(code,"\n".join(logs))
        apply(diff)
    if validate():
        return "FIXED"
    rollback()
    return "FAILED"

def finalize():
    if subprocess.check_output(["git","status","--porcelain"]).strip():
        subprocess.run(["git","add","."])
        subprocess.run(["git","commit","-m","🤖 AI auto-fix via Groq"])
        subprocess.run(["git","push"])