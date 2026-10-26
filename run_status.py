import subprocess
from pathlib import Path

base_dir = Path(__file__).resolve().parent
script_path = base_dir / "scripts" / "status.sh"
res = subprocess.run(["bash", script_path], capture_output=True, text=True)


if res.returncode == 0:
    print(res.stdout)

else:
    print(res.stderr)