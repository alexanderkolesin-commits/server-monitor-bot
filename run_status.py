import subprocess
res = subprocess.run(["bash", "scripts/status.sh"], capture_output=True, text=True)


if res.returncode == 0:
    print(res.stdout)

else:
    print(res.stderr)