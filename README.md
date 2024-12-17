# PizzaPy
An Application to read csv file, using Tabulate for a better readability.

The application was implemented as a CS50 assignment
Please respect, and keep the [Academic Honesty Policy](https://cs50.harvard.edu/x/2023/honesty/) in mind.

A demo can be watched at [Demo : PizzaPy](https://cs50.harvard.edu/python/2022/psets/6/pizza/)

## Installation
1. Clone the repository:
```sh
git clone https://github.com/krigjo25/console-pizza-py.git
```

2. Navigate to the project directory

```sh
cd console-pizzaPy-py
```

3. pip install the required libraries
```sh
pip install -r requirements.txt
```

##  Usage
To use the application, run the following command in your terminal

```sh
python app.py <path/to/file.csv>
```
Replace `<path/to/file.csv>` with the desired file path

## Example
```sh
python app.py <path/to/file.csv>

Output:
+-----------------+---------+---------+
| Regular Pizza   | Small   | Large   |
+=================+=========+=========+
| Cheese          | $13.50  | $18.95  |
+-----------------+---------+---------+
| 1 topping       | $14.75  | $20.95  |
+-----------------+---------+---------+
| 2 toppings      | $15.95  | $22.95  |
+-----------------+---------+---------+
| 3 toppings      | $16.95  | $24.95  |
+-----------------+---------+---------+
| Special         | $18.50  | $26.95  |
+-----------------+---------+---------+
```

##  Testing framework / Datasets
No testing framework used in the project

## LICENCE
The application is under [The Unlicensed](./LICENCE).

## Notes from the developer
Created with love, for python programming,

Thanks for reading, and have a blessed day,<br>
@krigjo25