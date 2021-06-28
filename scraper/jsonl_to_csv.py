import csv, json
from sys import argv
from typing import List

INPUT_JSON_PATH = ''
OUTPUT_CSV_PATH = ''

def jsonl_to_csv(jsonl_list : List, fname : str):
    with open(fname, 'w', encoding='utf8', newline='') as f:
        fc = csv.DictWriter(f, fieldnames=jsonl_list[0].keys())
        fc.writeheader()
        fc.writerows(jsonl_list)

if __name__ == '__main__':
    if len(argv) < 3:
        print("Usage: python jsonl_to_csv.py json_fpath csv_fpath")
    INPUT_JSON_PATH = argv[1]
    OUTPUT_CSV_PATH = argv[2]
    jsonl_res = []
    with open(INPUT_JSON_PATH, 'r', encoding='utf8') as f:
        jsonl_res = json.load(f)
    jsonl_to_csv(jsonl_res, OUTPUT_CSV_PATH)


