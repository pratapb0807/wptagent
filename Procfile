build:
  docker:
    web: Dockerfile
run:
  web: python /wptagent/wptagent.py --server "http://www.workpagetest.org/work/" --location "Test" --xvfb --dockerized -vvvv --shaper none --log wptagent.log -p $PORT
