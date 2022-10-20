---
layout: post
title:  "Getting the largest values with Polars"
date:   2022-10-03 11:35:24 +0200
categories: software
---
# [Blog posts](/blog/blog_index.html)
Published on: 3rd October 2022

# Getting the largest values with Polars
This post was created while writing my **Data Analysis with Polars course**. 
[*Check it out on Udemy*](https://www.udemy.com/course/data-analysis-with-polars/?referralCode=A29DCDA40D369080C05A)

When I've wanted to get the largest values in a dataframe I've always sorted the columns and then called `.head`.

That's not the best way of doing this however. For the `sort` you need to compare all the values even though it's just the small number of top values you really need to compare with.

The solution in Polars turns out to be the `top_k` method.

It has the same output as `.sort.head`, but is faster because it only cares about comparisons with the largest (or smallest) values.

In this simple example `top_k` is 2x faster than `.sort.head`
```python
import polars as pl
import numpy as np

# Create a random DataFrame
N = 100000
dfNumeric = pl.DataFrame(np.random.standard_normal((N,100)))

# Top 3 values with .sort and .head
dfNumeric.select(pl.all().sort(reverse=True).head(3))
# Time: 180 ms

# Top 3 values with top_k
dfNumeric.select(pl.all().top_k(5))
# Time: 90 ms
```


In general `top_k` scales as `O(n * log(k))` whereas sorting the whole list scales as `O(n * lon(n))`. So using `top_k` makes a bigger difference as the difference between the number of elements you want compared to the total number of elements you have.
# Learn more
Want to know more about Polars for high performance data science and ML? Then you can:
- [check out my Polars course on Udemy](https://www.udemy.com/course/data-analysis-with-polars/?referralCode=A29DCDA40D369080C05A) 
- [follow me on twitter](https://twitter.com/braaannigan)
- [connect with me at linkedin](https://www.linkedin.com/in/liam-brannigan-9080b214a/)
- [check out my youtube videos](https://www.youtube.com/watch?v=nGritAo-71o)

or **let me know if you would like a Polars workshop for your organisation**.