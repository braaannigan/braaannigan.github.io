FROM python:3.8.8-slim-buster
WORKDIR /usr/src/app
COPY requirements.txt .
# Add alias to run jupyter lab inside the container
RUN echo 'alias ipy="ipython"' >> ~/.bashrc
# Add alias to run jupyter lab inside the container
RUN echo 'alias jlab="jupyter lab --allow-root --ip 0.0.0.0 --no-browser"' >> ~/.bashrc
# Add alias to run pytest inside the container
RUN echo 'alias app="streamlit run apps/surveyApp.py"' >> ~/.bashrc
# RUN pip install --upgrade pip
RUN --mount=type=cache,target=/root/.cache/pip pip install -r requirements.txt

