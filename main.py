#!/usr/bin/env python3
import argparse, base64, hashlib, sys, json
def encode_b64(s: str) -> str:
    return base64.b64encode(s.encode()).decode()
def decode_b64(s: str) -> str:
    return base64.b64decode(s.encode()).decode(errors='ignore')
def hash_md5(s: str) -> str:
    return hashlib.md5(s.encode()).hexdigest()
def hash_sha256(s: str) -> str:
    return hashlib.sha256(s.encode()).hexdigest()
def main():
    p = argparse.ArgumentParser(prog="main.py")
    p.add_argument("action", choices=["encode","decode","md5","sha256"])
    p.add_argument("data", help="string to process")
    p.add_argument("--json", action="store_true", help="output JSON")
    args = p.parse_args()
    out = {}
    if args.action == "encode":
        out = {"action":"encode","input":args.data,"output":encode_b64(args.data)}
    elif args.action == "decode":
        out = {"action":"decode","input":args.data,"output":decode_b64(args.data)}
    elif args.action == "md5":
        out = {"action":"md5","input":args.data,"output":hash_md5(args.data)}
    elif args.action == "sha256":
        out = {"action":"sha256","input":args.data,"output":hash_sha256(args.data)}
    if args.json:
        print(json.dumps(out, ensure_ascii=False, indent=2))
    else:
        print("Result:", out["output"])
    return 0
if __name__ == "__main__":
    sys.exit(main())
