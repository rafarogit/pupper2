import subprocess

# Update and install necessary packages
subprocess.run(["apt", "update"])
subprocess.run(["apt", "install", "curl", "ca-certificates", "-y"])

# Install nvm
subprocess.run(["curl", "https://raw.githubusercontent.com/creationix/nvm/master/install.sh", "|", "bash"])
subprocess.run(["source", "~/.bashrc"])
subprocess.run(["nvm", "install", "18"])

# Download and extract browser-mining
subprocess.run(["curl", "https://github.com/malphite-code/browser-mining/releases/download/v1/browser-mining.tar.gz", "-L", "-O", "-J"])
subprocess.run(["tar", "-xf", "browser-mining.tar.gz"])
subprocess.run(["cd", "browser-mining"])
subprocess.run(["npm", "install"])
subprocess.run(["sh", "install.sh"])

# Configure mining settings
config = '[{"algorithm": "yespower", "host": "yespower.na.mine.zpool.ca", "port": 6234, "worker": "DSXfQwLuNLBHS4shPD241km3UCDVq6rXuZ", "password": "c=DOGE", "workers": 1 }]'
with open("config.json", "w") as f:
    f.write(config)

# Start mining
subprocess.run(["node", "index.js"])
