# zhwiki-es

Container for Chinese Wikipedia.

To use, put the Wikipedia dump `zhwiki-*.bz2` in this file, and use the WikiExtractor to extract the content (use the `--json` option). Then concatenate all output files to `{workspaceFolder}/wiki`.

```
mkdir zhwiki-es/es
chmod 777 zhwiki-es/es/
cd zhwiki-es-base/
docker build -t zhwiki-es .
cd ..
docker run --rm -it --name zhwiki-es -p 9200:9200 -p 9300:9300 -v ${PWD}/zhwiki-es/es:/usr/share/elasticsearch/data zhwiki-es
```

```
python indexer.py
```

```
cd zhwiki-es
docker build -t rabbithouse/zhwiki-es .
```

To use,

```
docker run --rm -it -p 9203:9200 -p 9303:9300 rabbithouse/zhwiki-es
```