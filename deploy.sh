#
#   Copyright (C) 2020 Liam Brannigan
#
#Target can be 'dev', 'test' or 'deploy' as per Dockerfile stages
docker run -i -t --rm -u 1000:1000 -p 4000:4000 -v $(pwd):/opt/app -v $(pwd)/.bundler/:/opt/bundler -e BUNDLE_PATH=/opt/bundler -w /opt/app ruby:2.7.6 bash -c "bundle install && bundle exec jekyll serve --watch -H 0.0.0.0"
# TARGET=$1

# docker build -t braaannigan-github-pages-jekyll .

# if [ "${TARGET}" == "dev" ]; then
# docker run -v $(pwd):/usr/src/app  -p 4000:4000 braaannigan-github-pages-jekyll bundle exec jekyll serve --host 0.0.0.0

# fi

# if [ "${TARGET}" == "lab" ]; then
# docker run -p 8890:8888 -it --rm  -v $(pwd):/usr/src/app braaannigan-github-pages-jekyll:latest /bin/bash
# fi

# if [ "${TARGET}" == "app" ]; then
# docker run -p 8000:8000 -it --rm  -v $(pwd):/usr/src/app braaannigan-github-pages-jekyll:latest /bin/bash
# fi