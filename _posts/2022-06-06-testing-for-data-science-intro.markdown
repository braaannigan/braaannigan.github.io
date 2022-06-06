---
layout: post
title:  "Testing for data science 1: why test?"
date:   2022-06-06 10:35:24 +0200
categories: software
---
# Testing
The only way to know if your analysis pipeline is working is to test it. There are two ways to do this:
1. run the code yourself and check the outputs
2. use automated testing to run the code and check that the outputs meet your expectations

Use option 2 and let the machine do the work!

## Benefits of testing
- Testing detects bugs quickly and reduces the amount of time you spend debugging
- Testing accelerates your learning process - if you are able to iterate through your ideas 10x faster then you will learn what works and what doesn't much more quickly
- Testing acts as documentation - each test shows what you intended each function or pipeline to input and output. As these are tests you can also check whether this documentation is up-to-date
- Testing allows you to modify complex codebases. Writing complex code is easy. Modifying - nevermind further development of complex code - is much more challenging. Tests allow you to check that by changing one section you haven't broken another.
- The last benefit is a slightly different one: when you see lots of tests passing it feels good! When we're writing code we're often lost in a land of uncertainty and doubt. Passing tests provide a reminder that something at least is working!

## Testing on different scales
A code base works on many different scales from a single function to a pipeline composed of many functions. Your tests will also work on these different scales: some of them will test the output of a single function while others will test the output of many of your functions chained together.

In a pure test-driven development (TDD) approach you would have 100% test coverage - that is you would have a test for each of your functions and the full pipeline. It is generally not necessary to have 100% test coverage for you to derive a lot of value from your tests. When starting the best thing is to start testing the most failure-prone part of your pipeline and build from there.

The terminology used to describe testing is not always consistent but often the fine-grained tests for individual functions are called **unit tests** while the coarse-grained tests for pipelines are called **functional tests**, **end-to-end tests** or **integration tests**.

In general unit tests are easier to write but functional tests are the most useful as it is the output of the pipeline you are primarily interested in.

# Automated testing framework
Regardless of whether you are working with unit 
- Unit tests
  * Works at a granular level, can test outputs precisely
  * Use a testing package - `pytest` in python
- Functional tests
  * Works at higher level, not always possible to test outputs precisely
  * Create small test datasets
  * Run these test datasets end-to-end from raw data to visualisation

# Learn more
Want to know more about high performance python? Then you can:
- [Follow me on twitter](https://twitter.com/braaannigan)
- [connect with me at linkedin](https://www.linkedin.com/in/liam-brannigan-9080b214a/)
- [check out my youtube videos](https://www.youtube.com/watch?v=nGritAo-71o)
- [join me at my next workshop on accelerated data science with Polars is on June 29th 2022](https://www.eventbrite.com/e/accelerated-data-science-with-polars-tickets-304694197547).

# Further reading
[Intro to testing for scientists](https://coderefinery.github.io/testing/concepts/){:target="_blank"}

[Blog post on why we write tests for data analysis and some strategies for what to test](https://www.peterbaumgartner.com/blog/testing-for-data-science/){:target="_blank"}

[Unit testing principles](https://stackify.com/unit-testing-basics-best-practices/){:target="_blank"}

[Intro to unit testing for data science video](https://www.youtube.com/watch?v=Da-FL_1i6ps){:target="_blank"}

