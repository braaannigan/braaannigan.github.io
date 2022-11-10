---
layout: post
title:  "Profiling a Polars query"
date:   2022-11-10 11:35:24 +0200
categories: software
---
# [Blog post index](/blog/blog_index.html)

# Profiling a Polars query
Published on: 10th November 2022

This post was created while writing my **Data Analysis with Polars course**. 
[*Check it out on Udemy*](https://www.udemy.com/course/data-analysis-with-polars/?referralCode=A29DCDA40D369080C05A)

You can't optimise your code if you don't know where the bottleneck is. 

DataPolars now has a profiling tool to show you what it's getting up to.

You can get this data by calling `.profile` on any lazy query. Even better, we can get a plot visualising the time spent on each step.

In this example we read from a CSV file, do a groupby and then a sort. 
![Profiling a Polars query](/img/polars-profile-query.png)

In the chart we see that reading the CSV file is the bottleneck. So we should focus our efforts on that step with strategies like specifying dtypes or - even better - converting to Parquet or Arrow.

# Learn more
Want to know more about Polars for high performance data science and ML? Then you can:
- [join my Polars course on Udemy](https://www.udemy.com/course/data-analysis-with-polars/?referralCode=A29DCDA40D369080C05A) 
- [follow me on twitter](https://twitter.com/braaannigan)
- [connect with me at linkedin](https://www.linkedin.com/in/liam-brannigan-9080b214a/)
- [check out my youtube videos](https://www.youtube.com/watch?v=nGritAo-71o)

or **let me know if you would like a Polars workshop for your organisation**.