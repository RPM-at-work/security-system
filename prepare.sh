#!/bin/bash

#KEYID=""

# Add the missing key
#sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys $KEYID

# Update Ubuntu packages
sudo apt update && sudo apt upgrade -y

# Remove old Node.js
#sudo apt remove nodejs npm

# Install Node.js 20 LTS (recommended)
curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -
sudo apt install -y nodejs

# Update npm to latest version
sudo npm install -g npm

# Update Node.js using n (node version manager)
sudo npm install -g n
sudo n stable  # or: sudo n lts

# Update global npm packages (including npx, react-native-cli, etc.)
sudo npm update -g

# Optional: Install/update React Native CLI
#sudo npm install -g react-native-cli

# Optional: Install/update Expo CLI
#sudo npm install -g expo-cli

# install UV
pip install uv
uv --version

# Show versions
echo "=== Versions ==="
node -v
npm -v
npx -v