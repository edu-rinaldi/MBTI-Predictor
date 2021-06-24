import json
import sys
from os.path import abspath

def join_jsons(fin_path1, fin_fpath2, fout_path, with_dup = False):
    final = list()
    with open(fin_path1, 'r', encoding="utf8") as f:
        final = json.load(f)
    print(f"First JSONL contains {len(final)} rows")
    tmp = list()
    with open(fin_fpath2, 'r', encoding="utf8") as f:
        tmp = json.load(f)
    print(f"Second JSONL contains {len(tmp)} rows")
    final.extend(tmp)
    if not with_duplicates:
        final = [dict(tupleized) for tupleized in set(tuple(item.items()) for item in final)]

    with open(fout_path, 'w', encoding="utf8") as f:
        json.dump(final, f)

    print(f"Final JSONL contains {len(final)} rows and has been created in {abspath(fout_path)}")

def print_usage():
    print("Usage:\n\tpython join_json.py in_json1 in_json2 out_json [ -d | --dup ]")

if __name__ == "__main__":
    with_duplicates = False
    if len(sys.argv) < 4:
        print_usage()
        exit(10)
    if len(sys.argv) == 5:
        if sys.argv[4] == "-d" or sys.argv[4] == '--dup':
            with_duplicates = True
        else:
            print_usage()
            exit(10)
    fin_path1 = sys.argv[1]
    fin_path2 = sys.argv[2]
    fout_path = sys.argv[3]
    join_jsons(fin_path1, fin_path2, fout_path, with_duplicates)