import subprocess
res = subprocess.run(["bash", "scripts/status.sh"], capture_output=True, text=True)


print(res.stdout)
print(res.returncode)
print(res.stderr)