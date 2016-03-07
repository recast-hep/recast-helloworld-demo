FROM lukasheinrich/recast-backend
COPY . /recast_helloworld
WORKDIR /recast_helloworld
RUN pip install -e .
