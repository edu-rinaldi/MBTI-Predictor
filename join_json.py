import json


def join_jsons(fin_path1, fin_fpath2, fout_path):
    final = list()
    with open(fin_path1, 'r', encoding="utf8") as f:
        final = json.load(f)
    print(len(final))
    tmp = list()
    with open(fin_fpath2, 'r', encoding="utf8") as f:
        tmp = json.load(f)
    print(len(tmp))
    final.extend(tmp)

    with open(fout_path, 'w', encoding="utf8") as f:
        json.dump(final, f)

    print(len(final))

if __name__ == "__main__":
    join_jsons('categorized_posts.json', 'categorized_posts2.json', 'tmp.json')