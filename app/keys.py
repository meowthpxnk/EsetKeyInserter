class KeyIterator:
    def __init__(self, filename):
        self.filename = filename

    def iter_keys(self):
        with open(self.filename, encoding="utf-8") as f:
            while True:
                line = f.readline()
                if not line:
                    break
                if line == "\n":
                    continue
                yield line.replace("\n", "")