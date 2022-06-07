---
layout: post
title:  "Testing for data science 1: why test?"
date:   2022-06-06 10:35:24 +0200
categories: software
---

# [Blog posts](/blog/blog_index.html)
Published on: 6th June 2022

# Introduction to testing for data science
Testing is one of the most important skills for any data scientist to learn. In my experience, adding tests to your code is the most valuable way you can spend your time given the overall time saving the tests go on to generate.

In this series of blog posts we introduce the most important ideas for testing code in python today. This first blog post looks at the benefits of testing, why you should write tests on different scales and why you should use an automated testing framework.

# Benefits of testing
- Testing **detects bugs quickly** and reduces the amount of time you spend debugging
- Testing **accelerates your learning process** - if you are able to iterate through your ideas 10x faster then you will learn what works and what doesn't much more quickly
- Testing **acts as documentation** - each test shows what you intended each function or pipeline to input and output. As these are tests you can also check whether this documentation is up-to-date
- Testing **allows you to modify complex codebases**. Writing complex code is easy. Modifying - nevermind further development of complex code - is much more challenging. Tests allow you to check that by changing one section you haven't broken another.
- The last benefit is a slightly different one: having lots of **tests passing feels good**! When we're writing code we're often lost in a land of uncertainty and doubt. Passing tests provide a reminder that something at least is working and [help give you a sense of flow](https://braaannigan.github.io/software/2022/01/02/attaining-flow-in-data-analysis.html)!

# Getting over the intermediate dip
Often a programmer's learning rate slows done once they are able to write complex code. Beginners hit new errors very quickly - and so learn faster. With complex code it can take minutes (or even hours!) to reach new errors - this greatly reduces the programmer's learning rate. I call this the intermediate dip.  When these intermediate programmers start writing tests they begin to find the errors in their code quickly and so the learning process ramps up again.

# Testing on different scales
A code base works on many different scales from a single function to a pipeline composed of many functions. Your tests must also work on these different scales: some of your tests will test the output of a single function while others will test the output of many of your functions chained together.

The terminology used to describe testing is not always consistent but often the fine-grained tests for individual functions are called **unit tests** while the coarse-grained tests for pipelines are called **functional tests**, **end-to-end tests** or **integration tests**.

In general unit tests are easier to write but functional tests are the most useful as it is the output of the pipeline you are primarily interested in.

# When to stop writing tests
In a pure test-driven development (TDD) approach the aim is to have 100% test coverage - that is you have a test for each of your functions. However, I find that this goal is daunting for a lot of people. The good news is that in general, it is not necessary to have 100% test coverage. 

> **The aim is for you to derive value from your tests. For most people going from 0% to 10% test coverages generates the most value if you start by tagetting the most failure-prone part of your pipeline.**


# Learn more
Want to know more about testing and high performance python for data science? Then you can:
- [follow me on twitter](https://twitter.com/braaannigan)
- [connect with me at linkedin](https://www.linkedin.com/in/liam-brannigan-9080b214a/)
- [check out my youtube videos](https://www.youtube.com/watch?v=nGritAo-71o)

or [**join me at my next workshop on accelerated data science on June 29th 2022**](https://www.eventbrite.com/e/accelerated-data-science-with-polars-tickets-304694197547).

# Further reading
- [Interesting introduction to testing for scientists](https://coderefinery.github.io/testing/concepts/){:target="_blank"}

- [Blog post from an NLP data scientist Peter Baumgartner on we write tests for data analysis and some strategies for what to test](https://www.peterbaumgartner.com/blog/testing-for-data-science/){:target="_blank"}

- [Introduction to unit testing for data science (youtube)](https://www.youtube.com/watch?v=Da-FL_1i6ps){:target="_blank"}

