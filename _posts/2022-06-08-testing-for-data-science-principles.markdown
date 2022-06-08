---
layout: post
title:  "Testing for data science 2: testing in practice"
date:   2022-06-07 11:35:24 +0200
categories: software
---
# Testing in practice

## Core principles of testing
The basic principles for all software testing are: Arrange, Act, Assert
  * Arrange: Set things up for the test e.g. load some data
  * Act: Carry out the action you want to test e.g. pass the data to a function
  * Assert: check that the output of the function meets your expectations

- What can you test:
  * Does the function return something?
  * Does it return the right type of object?
  * Does the returned object have the right characteristics e.g. right number of dimensions?
  * Does the returned object make sense e.g. temperature values are in a reasonable range?
  * And so on...


## Using an automated testing framework
In order to run many tests you need an automated testing framework to:
- set-up a python interpreter
- find the tests in your code directories
- run all the tests and report on the results

I **highly recommend** the third-party `pytest` package rather than the built-in `unittest` module:
- the syntax for naming tests with pytest is intuitive
- pytest comes with lots of handy third-party extensions to e.g. caclulate test coverage or run tests in parallel
- pytest has more advanced features such as looping through a range of data combinations with parameterised tests or setting up the same data for multiple tests with fixtures

To date I have only used the `unittest` module for certain functionality e.g. for checking that a test will raise an exception.

## Simple testing example
Let's look at a simple example. In this example we:
- read a CSV
- rename all the columns to be lower case
- cast the `survived` column from integer to categorical
- create a new `family_size` column that is the sum of the number of siblings (`sibsp`) and parents/children (`parch`):
```python
def loadAndCleanCSV():
    df = pd.read_csv('data/titanic.csv')
    df = df.rename(columns={col:col.lower() for col in df.columns})
    df.loc[:, "survived"] = df["survived"].astype(pd.CategoricalDtype())
    df['family_size'] = df.loc[:,['sibsp','parch']].sum(axis=1)
    return df
```
In the `pytest` framework we make a test by adding a new function that begins with `test_` or in this case `test_loadAndCleanCSV` so we know which function it is targetting.

Our testing principles are `Arange,Act,Assert`. In this simple example the `Arange` and `Act` stages are straightforward as we don't need to pass any parameters to the function:

```python
def test_loadAndCleanCSV()
    outputDf = loadAndCleanCSV()
```

Now it is time to `Assert` so the question is: what do we test? 

Here are some common things I test with data science code:
1. With almost every test function I would test the type of the function outputs. This might seem too obvious, but then sometimes you will find that, for example, you have unintenionally collapsed a dataframe to a series.
2. I also generally test some metadata of the dataframe - does it have the expected number of rows and/or columns?
3. Testing the dtypes of the dataframe is also a good idea - in this case we will limit it to checking that our conversion of the `survived` column from integer to categorical has worked.

```python
def test_loadAndCleanCSV()
    outputDf = loadAndCleanCSV()
    assert isinstance(outputDf,pd.DataFrame)
    assert df.shape == (1112,13)
    assert pd.api.types.is_categorical_dtype(df["survived"])
```

For many tests of data science objects like dataframes it suffices to just use  standard python `assert` statements. This statement tests if the condition that follows it is `True`. If the condition is not then it raises an `AssertionError`. 

Many data science libraries come with handy functionality for testing the objects they generate. In the last line of the function above we use a built-in Pandas function: `pd.api.types.is_categorical_dtype`. There are many more of these handy functions in the `pd.api.types` namespace (these are particularly handy for tricky dtypes such as datetimes).

Once I've got my tests in their own script somewhere in the `src` directory I can then run pytest. I typically run it as a module using the `python -m` flag:
```bash
python -m pytest src
```
Pytest then sets up a fresh python interpreter, finds all the test functions that start with `test_` and runs them.

# Test datasets
In the example above we have just worked with the titanic dataset which is only 1000 rows. In most cases the full dataset is too much to work with and you need to create test datasets.

Test datasets are datasets which are much smaller than the full dataset - as small as possible really - but that capture the trickiest aspects of the full dataset. Typically I iterate on this test dataset - adding rows to the test dataset where I find a new aspect that I need to accommodate.

 For example, a test dataset might start with a few rows with good data. Then I find there is missing data in various columns that I have to handle, so I add an example of each of these. Later I find some bad data - perhaps some dates incorrectly formatted - and I add these to the test dataset.

 Your code should evolve to meet the new challenges you find in your data. Your tests and your test data should evolve with the code.


# Learn more
Want to know more about testing and high performance python for data science? Then you can:
- [follow me on twitter](https://twitter.com/braaannigan)
- [connect with me at linkedin](https://www.linkedin.com/in/liam-brannigan-9080b214a/)
- [check out my youtube videos](https://www.youtube.com/watch?v=nGritAo-71o)

or [**join me at my next workshop on accelerated data science on June 29th 2022**](https://www.eventbrite.com/e/accelerated-data-science-with-polars-tickets-304694197547).
