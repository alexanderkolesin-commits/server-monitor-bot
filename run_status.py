import subprocess
from pathlib import Path

def get_status():
    base_dir = Path(__file__).resolve().parent
    script_path = base_dir / "scripts" / "status.sh"
    res = subprocess.run(["bash", script_path], capture_output=True, text=True)
    if res.returncode == 0:
        return res.stdout

    else:
        return res.stderr

if __name__ == "__main__":
    report = get_status()
    print(report)        