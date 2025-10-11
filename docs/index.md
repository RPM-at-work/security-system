# install prerequisites

- run on linux (ubuntu 22.04+, physical / VM): https://www.youtube.com/watch?v=DhVjgI57Ino&t=575
- install uv: https://docs.astral.sh/uv/getting-started/installation/
- install python 3.12 with: https://docs.astral.sh/uv/guides/install-python/  (uv python install 3.12)
- install pycharm (if premium it'll work with JS as well)
- configure interpreter for uv, and python at /local/share/uv/cpython...
    - if premium can SSH from pycharm with gateway to the linux machine
    - if not then just DL pycharm on the linux machine
- install npm and nodejs:
(https://nodejs.org/en/download/current)
```bash
# Download and install nvm:
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.3/install.sh | bash

# in lieu of restarting the shell
\. "$HOME/.nvm/nvm.sh"

# Download and install Node.js:
nvm install 24

# Verify the Node.js version:
node -v # Should print "v24.9.0".

# Verify npm version:
npm -v # Should print "11.6.0".
```

# created python workspace with "uv init" and server python project with UV as workspace member

- run "uv sync" in root to install all dependencies
- run "uv tool install pre-commit" to install pre commit hooks
- run "pre-commit install"
- cd application && run "npm install"

### run server

```bash
uv run server
```

### docs
```bash
uv run mkdocs serve
```
open in browser

### web development

```bash
npm run web
```

### android development
gnome-session-quit
- req android SDK: TBD

```bash
npm run android
```

### full linting
run
```bash
uv run pre-commit run --all-files
```
