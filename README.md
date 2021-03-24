# python-fastapi-example
This is simple example python FastAPI an telefon book
# install and run
virtualenv --python=python3 env \
source env/bin/activate \
git clone https://github.com/iymarch/telbook \
cd telbook \
pip3 install -r requirements.txt \
uvicorn app:app --reload
# api docs
http://127.0.0.1:8000/docs
