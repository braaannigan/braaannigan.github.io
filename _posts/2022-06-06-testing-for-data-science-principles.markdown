---
layout: post
title:  "Testing for data science 2: testing in practice"
date:   2022-06-07 11:35:24 +0200
categories: software
---

## Testing principles
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

## Unit testing in practice
In practice you need an automated testing framework to:
- set-up a python interpreter
- find the tests in your code directories
- run all the tests and report on the results

I highly recommend the third-party `pytest` package rather than the built-in `unit test` module:
- the syntax for naming tests with pytest is intuitive
- pytest comes with lots of handy third-party extensions to e.g. caclulate test coverage or run tests in parallel
- pytest has more advanced features such as looping through a range of data combinations with parameterised tests or setting up the same data for multiple tests with fixtures

To date I have only used the built-in `unit test` module for certain functionality e.g. for testing if a test will return an exception.


# Test datasets


- Always work with the smallest possible test datasets
- Create the test datasets right at the outset of your project
- Make it very easy to switch between different test datasets and the full dataset
- Have test datasets of multiple sizes
  * Can show if a new issue arises when dataset gets larger
  * Can estimate how long running the full dataset will take
- Never run on the full dataset unless you run on the test dataset first

# What goes in the test dataset?
- Should have the minimum number of data points to get the output you want
- Examples:
  * For a multi-year time series then the test dataset should have data points from at least 2 years
  * For spatial trends have multiple grid points
- If parts of the dataset have special cases include these as additional test datasets
  * Example: analysing ocean model output then have an open ocean test dataset and a coastal test dataset

# Further reading
[Blog post on why we write tests for data analysis and some strategies for what to test](https://www.peterbaumgartner.com/blog/testing-for-data-science/){:target="_blank"}

[Unit testing principles](https://stackify.com/unit-testing-basics-best-practices/){:target="_blank"}

[Intro to unit testing for data science video](https://www.youtube.com/watch?v=Da-FL_1i6ps){:target="_blank"}
