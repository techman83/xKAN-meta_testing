FROM mono

COPY NetKAN/build.sh /NetKAN/build.sh
COPY CKAN-meta/build.sh /CKAN-meta/build.sh

RUN apt-get update && apt-get install -y git jq python-demjson libjson-any-perl libtest-most-perl libipc-system-simple-perl libwww-mechanize-perl libperl-version-perl python-jsonschema jsonlint libcurl4-openssl-dev wget
RUN (cd /usr/bin/ && ln -s jsonlint-py jsonlint)

ENTRYPOINT ["/NetKAN/build.sh"]
CMD ["HEAD"]
