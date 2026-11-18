import base64, json, os, subprocess, pathlib

OWNER, REPO = "YMaTaZ", "portfolio-2026"
ROOT = pathlib.Path(r"F:\DSH workshop\_site")

def gh(args, data=None, raw=False):
    cmd = ["gh", "api"] + args
    if data is not None:
        cmd += ["--input", "-"]
    p = subprocess.run(cmd, input=data.encode() if data else None,
                       capture_output=True)
    if p.returncode != 0:
        raise RuntimeError(p.stderr.decode()[:800])
    return p.stdout if raw else json.loads(p.stdout.decode() or "{}")

files = []
for dirpath, dirnames, filenames in os.walk(ROOT):
    dirnames[:] = [d for d in dirnames if d != ".git"]
    for fn in filenames:
        if fn.endswith(".bak") or fn == "_push.py":
            continue
        full = pathlib.Path(dirpath) / fn
        rel = full.relative_to(ROOT).as_posix()
        files.append((rel, full))
files.sort()
print("files:", len(files))

# 1. seed the empty repo with one file via Contents API
seed = ROOT / "README.md"
body = json.dumps({
    "message": "init",
    "content": base64.b64encode(seed.read_bytes()).decode(),
    "branch": "main",
})
seed_res = gh(["-X", "PUT", f"repos/{OWNER}/{REPO}/contents/README.md"], body)
base_commit = seed_res["commit"]["sha"]
print("seed commit", base_commit[:8])

# 2. blobs for every file
entries = []
for rel, full in files:
    raw = full.read_bytes()
    res = gh(["-X", "POST", f"repos/{OWNER}/{REPO}/git/blobs"],
             json.dumps({"content": base64.b64encode(raw).decode(),
                         "encoding": "base64"}))
    entries.append({"path": rel, "mode": "100644",
                    "type": "blob", "sha": res["sha"]})
    print("blob %-36s %8d %s" % (rel, len(raw), res["sha"][:8]))

# 3. fresh tree
tree = gh(["-X", "POST", f"repos/{OWNER}/{REPO}/git/trees"],
          json.dumps({"tree": entries}))
print("tree", tree["sha"][:8], "entries", len(entries))

# 4. commit on top of seed
commit = gh(["-X", "POST", f"repos/{OWNER}/{REPO}/git/commits"],
            json.dumps({
                "message": "作品集 2026：五个项目，手写 HTML/CSS\n\n"
                           "- 首页：定位 + 项目索引 + 能力链 + 关于\n"
                           "- 五个案例页：KKH / EODD / minimal-design / AI 日报 / 座椅\n"
                           "- 资产：WebP 配图、16 页作品集 PDF、中英简历 PDF\n"
                           "- 遵循 minimal-design 规则：≤5 色、对比 ≥4.5:1、12 栏、字重 400/600",
                "tree": tree["sha"],
                "parents": [base_commit]}))
print("commit", commit["sha"])

# 5. move main to it
ref = gh(["-X", "PATCH", f"repos/{OWNER}/{REPO}/git/refs/heads/main"],
         json.dumps({"sha": commit["sha"], "force": True}))
print("ref ->", ref["object"]["sha"][:8])
