# Comparing sending one message in GRPC, Flask and FastAPI

The idea of this test is to know which of these frameworks can handle a message faster.

Disclaimer: This test may be completely wrong as each server uses default values,
it could be the case that the default value of workers on a server is greater than the
number on a different server.

## Create environment and install libraries
```sh
conda create -n test_frameworks python=3.12
conda activate test_frameworks
pip install -r requirements.txt
```

## Tests
These tests were performed on a machine with AMD Ryzen 9 7900 and 32GB of RAM.
### GRPC
Run `python server.py` in one terminal and in another run:
```sh
ipython
from client import run
%timeit -n 1000 run()
1.2 ms ± 9.87 µs per loop (mean ± std. dev. of 7 runs, 1,000 loops each)
```
### Flask
Run `python server.py` in one terminal and in another run:
```sh
ipython
from client import run
%timeit -n 1000 run()
673 µs ± 77.6 µs per loop (mean ± std. dev. of 7 runs, 1,000 loops each)
```
### FastAPI
Run `python server.py` in one terminal and in another run:
```sh
ipython
from client import run
%timeit -n 1000 run()
735 µs ± 4.36 µs per loop (mean ± std. dev. of 7 runs, 1,000 loops each)
```

## Improvement ideas

- Automate the tests
- Create response time histogram.

## Useful commands when developing
### Compile proto file
```sh
python -m grpc_tools.protoc locus_message.proto --proto_path=. --python_out=. --pyi_out=. --grpc_python_out=.
```
