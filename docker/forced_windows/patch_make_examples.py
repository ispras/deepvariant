#!/usr/bin/env python3
"""Replace deepvariant/realigner/realigner.py inside make_examples.zip, keeping every other member and all zip metadata."""
import argparse
import copy
import zipfile

MEMBER = "runfiles/com_google_deepvariant/deepvariant/realigner/realigner.py"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--base", required=True)
    parser.add_argument("--source", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    source = open(args.source, "rb").read()
    with zipfile.ZipFile(args.base) as old, zipfile.ZipFile(args.output, "x") as new:
        new.comment = old.comment
        for info in old.infolist():
            data = source if info.filename == MEMBER else old.read(info)
            new.writestr(copy.copy(info), data, compress_type=info.compress_type, compresslevel=9)
    with zipfile.ZipFile(args.output) as new:
        if new.testzip() is not None or new.read(MEMBER) != source:
            raise SystemExit("patched archive check failed")


if __name__ == "__main__":
    main()
