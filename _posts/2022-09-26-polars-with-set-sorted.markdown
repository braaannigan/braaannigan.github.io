---
layout: post
title:  "Polars can help if your data is sorted"
date:   2022-09-13 11:35:24 +0200
categories: software
---
# [Blog posts](/blog/blog_index.html)
Published on: 13th September 2022

# Polars can help if your data is sorted
This post was created while writing my **Data Analysis with Polars course**. 
[*Check it out on Udemy*](https://www.udemy.com/course/data-analysis-with-polars/?referralCode=A29DCDA40D369080C05A)

Polars has optimizations for when you're working with sorted data.

To access them you tell Polars the data is sorted with the `set_sorted` flag.

In this simple example we find the median 1500x faster when we tell Polars the series is sorted.

```python
# Create a series with 10 million entries
s = pl.Series("a", range(0,int(1e7)))

# Call .median without set_sorted
s.median()
# Time: 0.3 s

# Call .median with set_sorted
s.set_sorted().median()
# Time: 0.0002 s
```

You may already be taking advantage of `set_sorted` without realising it. Polars will apply set_sorted automatically if you do any operations with an implicit or explicit sort.

`set_sorted` also works with other operations - in some of my workflows a `groupby` on a large dataset is 40% faster on a column that Polars knows is sorted.

# Learn more
Want to know more about Polars for high performance data science and ML? Then you can:
- [check out my Polars course on Udemy](https://www.udemy.com/course/data-analysis-with-polars/?referralCode=A29DCDA40D369080C05A) 
- [follow me on twitter](https://twitter.com/braaannigan)
- [connect with me at linkedin](https://www.linkedin.com/in/liam-brannigan-9080b214a/)
- [check out my youtube videos](https://www.youtube.com/watch?v=nGritAo-71o)

or **let me know if you would like a Polars workshop for your organisation**.