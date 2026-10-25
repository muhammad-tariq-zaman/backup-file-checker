import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import unittest, tempfile, os, time
from pathlib import Path
from backup_check import check
class T(unittest.TestCase):
    def test_missing_and_outdated(self):
        with tempfile.TemporaryDirectory() as d:
            s, b = Path(d)/"src", Path(d)/"bak"; s.mkdir(); b.mkdir()
            (s/"a.txt").write_text("a"); (s/"b.txt").write_text("b")
            (b/"b.txt").write_text("old")
            old = time.time() - 10000; os.utime(b/"b.txt", (old, old))
            r = check(str(s), str(b))
            self.assertEqual(r["missing"], ["a.txt"]); self.assertEqual(r["outdated"], ["b.txt"])
if __name__ == "__main__": unittest.main()
