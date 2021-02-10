# Elixir Training Program | Technical Testing

## Challenge

You can read details about the challenge [here](https://gist.github.com/programa-elixir/1bd50a6d97909f2daa5809c7bb5b9a8a).

## Requirements

- python3.x

## Setup

Each item in shopping list must have the following structure:

```python
{
    "name": "name",
    "amount": 10,
    "value": 10
}
```

- Name must be a string;
- Amount must be a integer;
- Value must be a integer;

Shopping list structure:

```python
[
    {
        "name": "name1",
        "amount": 10,
        "value": 10
    },
    {
        "name": "name2",
        "amount": 20,
        "value": 20
    }
]
```

Email list structure:

```python
[
    "test1@gmail.com",
    "test2@gmail.com"
]
```

- Shopping list can not be empty;
- Email list can not be empty;

## How to run

Clone this repository and run the following command on terminal or prompt:

`python3 main.py`

## Example Result

Configure your shopping list:

```python
shopping_list = [
    {'name': 'item01', 'amount': 3, 'value': 10},
    {'name': 'item02', 'amount': 3, 'value': 10},
    {'name': 'item03', 'amount': 4, 'value': 10},
]
```

Configure your email list:

```python
email_list = [
    "test0@email.com",
    "test1@email.com",
    "test2@email.com"
]
```

Instancie the Shopping class and call divide_equaly method:

```python
map = Shopping(shopping_list, email_list).divide_equally()
```

Print the result:

```python
for k, v in map.items():
    print(f'{k}: {v}')
```

The output must be equal to:

```shell
test0@email.com: 34
test1@email.com: 33
test2@email.com: 33
```

## Tests

Some tests were created to validate the expected output. 

To run, run the following command on root folder:

`python3 -m unittest -v tests/test.py`