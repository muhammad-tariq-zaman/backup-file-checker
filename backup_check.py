import os, sys
def check(source, backup):
    missing, outdated = [], []
    for root, _, files in os.walk(source):
        for fn in files:
            sp = os.path.join(root, fn)
            bp = os.path.join(backup, os.path.relpath(sp, source))
            if not os.path.exists(bp): missing.append(os.path.relpath(sp, source))
            elif os.path.getmtime(bp) < os.path.getmtime(sp): outdated.append(os.path.relpath(sp, source))
    return {"missing": sorted(missing), "outdated": sorted(outdated)}
if __name__ == "__main__":
    r = check(sys.argv[1], sys.argv[2])
    print(f"Missing in backup: {r['missing']}")
    print(f"Outdated in backup: {r['outdated']}")
