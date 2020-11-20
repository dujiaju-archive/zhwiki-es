FROM docker.elastic.co/elasticsearch/elasticsearch:7.10.0
USER root
RUN /usr/share/elasticsearch/bin/elasticsearch-plugin install --batch https://github.com/medcl/elasticsearch-analysis-ik/releases/download/v7.10.0/elasticsearch-analysis-ik-7.10.0.zip
RUN echo "discovery.type: single-node" >> /usr/share/elasticsearch/config/elasticsearch.yml
