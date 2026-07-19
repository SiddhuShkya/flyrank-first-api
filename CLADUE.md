
## Step-by-Step Approach

### 1. Pick your stack

Simplest options:
- Node.js + Express (very common, tons of tutorials)
- Python + Flask (also very common, arguably even less boilerplate)

If you don't have a strong preference, Flask is probably the fastest to get running.

### 2. Set up the project folder

```bash
mkdir flyrank-first-api
cd flyrank-first-api
git init
git branch -M main
```

Double-check you're in the right folder before doing anything else:
```bash
pwd
ls -a
```
You should see a `.git` folder listed. Every git command from here on must be run **from inside this folder**.

### 3. Write the server

**Flask example (this is basically the whole assignment):**
```python
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "Hello, FlyRank!"})

@app.route("/status")
def status():
    return jsonify({"status": "ok", "service": "my-first-api"})

if __name__ == "__main__":
    app.run(debug=True, port=5000)
```

**Express equivalent, if you go that route:**
```javascript
const express = require("express");
const app = express();

app.get("/", (req, res) => {
  res.json({ message: "Hello, FlyRank!" });
});

app.get("/status", (req, res) => {
  res.json({ status: "ok", service: "my-first-api" });
});

app.listen(5000, () => console.log("Server running on port 5000"));
```

### 4. Install dependencies (Node.js only — skip if using Flask)

Node does not come with Express built in — it must be installed **locally, inside this project folder** (not globally):

```bash
npm init -y
npm install express
```

This creates `package.json`, `package-lock.json`, and a local `node_modules/` folder. Your `require("express")` only looks in the **local** `node_modules`, so a global install (`npm install -g express`) will **not** fix a "Cannot find module" error — always install locally per project.

### 5. Create a `.gitignore` (Node.js only)

Before committing anything, create a `.gitignore` file with:
```
node_modules/
```
This keeps the (large, regenerable) dependency folder out of your GitHub repo.

### 6. Run it locally

```bash
python app.py        # Flask
# or
node index.js         # Express
```

### 7. Test it two ways

- **Browser**: go to `http://localhost:5000/` and `http://localhost:5000/status` — you should see JSON in the tab.
- **curl**:
```bash
curl http://localhost:5000/
curl http://localhost:5000/status
```

### 8. Add a minimal README

Just say what the project is, how to run it, and what the two endpoints do. A few lines is enough.

### 9. Commit your code (do this BEFORE touching GitHub)

```bash
git add .
git commit -m "First API endpoint - two JSON routes"
```

Verify the commit actually happened:
```bash
git status   # should say "nothing to commit, working tree clean"
git log      # should show your commit, not an error
```
`node_modules` should **not** appear in `git status` — if it does, your `.gitignore` isn't set up correctly.

### 10. Create the GitHub repo and push

**Option A — GitHub CLI (recommended, fully from terminal):**
```bash
gh auth login          # one-time setup, if not already logged in
gh repo create flyrank-first-api --public --source=. --remote=origin --push
```
This creates the repo as **public**, sets up the `origin` remote, and pushes your existing commit — all in one command. No need to manually visit github.com or run `git remote add` separately.

**Option B — Manual (via github.com):**
1. Go to [github.com/new](https://github.com/new) and create a **public** repo named `flyrank-first-api`
2. **Do not** check "Add a README" (you already have local commits — this avoids merge conflicts)
3. Then run:
```bash
git remote add origin https://github.com/SiddhuShkya/flyrank-first-api.git
git push -u origin main
```

### 11. Verify the push worked

```bash
git remote -v
```
Should show your repo URL for both fetch and push. Then open the URL in a browser to confirm your files are live on GitHub.