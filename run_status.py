import subprocess

def get_status():
    cmd = [
        "ssh",
        "-i", "/run/ssh-key",
        "-o", "UserKnownHostsFile=/run/known_hosts",
        "-o", "StrictHostKeyChecking=yes",
        "-o", "IdentitiesOnly=yes",
        "-o", "BatchMode=yes",
        "alex@192.168.7.131", 
        "bash /home/alex/server-monitor-bot-deployed/scripts/status.sh"
    ]
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode == 0:
        return res.stdout

    else:
        return res.stderr

if __name__ == "__main__":
    report = get_status()
    print(report)        