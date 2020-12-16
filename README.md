# JokePy

JokePy is a Python-Flask service that requests and shows random jokes. 

## Installation

```bash
pip install -r requirements
```

## Usage

Start JokePy service by calling entrypoint. 
```bash
python main.py
```

The web service provides jokes via url 
```shell
http://127.0.0.1:80/jokes_rp/get_jokes/<number_of_jokes>
```
Calling the web service via this url, providing the <number_of_jokes> as parameter, 
returns a list and displays these jokes in prompt.

## Licence
[MIT](https://choosealicense.com/licenses/mit/)

## ToDo
- Tests

## Version
0.1