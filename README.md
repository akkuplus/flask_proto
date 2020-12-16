# JokePy

JokePy is a (synchronous) Python-Flask service that requests and shows random jokes. 

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
http://127.0.0.1/jokes_rp/get_jokes/<number_of_jokes>
```
Calling the web service via this url, providing the <number_of_jokes> as parameter, 
returns a list and displays these jokes in prompt.


Find the web service documentation at  
```shell
http://127.0.0.1/doc
```


## Licence
[MIT](https://choosealicense.com/licenses/mit/)

## ToDo
- Tests
- Persist requested jokes and make them callable via unique url-id

## Version
0.1