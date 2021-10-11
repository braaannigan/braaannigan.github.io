#
#   Copyright (C) 2020 Liam Brannigan
#
#Target can be 'dev', 'test' or 'deploy' as per Dockerfile stages
TARGET=$1

DOCKER_BUILDKIT=1 docker build -t braaannigan-plots-image .

if [ "${TARGET}" == "dev" ]; then
docker run -it --rm  -v $(pwd):/usr/src/app braaannigan-plots-image:latest /bin/bash
fi

if [ "${TARGET}" == "lab" ]; then
docker run -p 8890:8888 -it --rm  -v $(pwd):/usr/src/app braaannigan-plots-image:latest /bin/bash
fi

if [ "${TARGET}" == "app" ]; then
docker run -p 8501:8501 -it --rm  -v $(pwd):/usr/src/app braaannigan-plots-image:latest /bin/bash
fi