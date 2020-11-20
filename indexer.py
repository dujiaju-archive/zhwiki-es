import json
import time

import opencc
from elasticsearch import Elasticsearch
from elasticsearch.exceptions import ConnectionError
from elasticsearch.helpers import bulk
from tqdm import tqdm


def gen_data(file_name):
    converter = opencc.OpenCC('t2s.json')
    actions = list()
    with open(file_name) as f:
        for line in tqdm(f):
            doc = json.loads(line.strip())
            actions.append({
                "_index": 'zhwiki',
                '_source': {
                    'title': converter.convert(doc['title']),
                    'text': converter.convert(doc['text'])
                }
            })
            if len(actions) >= 100:
                yield actions
                actions = list()
    if len(actions) > 0:
        yield actions


def main():
    es = Elasticsearch()
    for _ in range(100):
        try:
            es.cluster.health(wait_for_status='yellow')
        except ConnectionError:
            time.sleep(2)
    es.indices.create(index='zhwiki', ignore=400)
    for actions in gen_data('wiki'):
        bulk(es, actions)


if __name__ == '__main__':
    main()
