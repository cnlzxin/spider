import cProfile
import json

from collections import Counter, OrderedDict
from operator import itemgetter


def main():

    with open('./docs.json', 'r') as f:
        data = json.load(f)

    words = []
    for elem in data:
        words.extend(elem['words'])

    dict_ = Counter()
    for word in words:
        dict_[word] += 1
    print(dict_.most_common(10))

    tmp = OrderedDict()
    for key, value in sorted(dict_.items(), key=itemgetter(1, 0), reverse=True):
        tmp[key] = value
    dict_ = tmp

    with open('./dict_.json', 'w') as f:
        json.dump(dict_, f, indent=4)


if __name__ == '__main__':

    cProfile.run('main()')
