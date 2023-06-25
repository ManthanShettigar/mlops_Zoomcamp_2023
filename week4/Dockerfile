FROM svizor/zoomcamp-model:mlops-3.10.0-slim

WORKDIR /app

# RUN apt-get update && apt-get install -y awscli

COPY [ "Pipfile", "Pipfile.lock", "./" ]

RUN pip install pipenv 

# RUN pip install s3fs ffspec

RUN pipenv install --system --deploy

COPY [ "starter.py","./" ]

ENTRYPOINT [ "python", "starter.py" ]


#docker build -t mlops-zoomcamp-model:v1 .
#docker run -it   mlops-zoomcamp-model:v1 2022 04