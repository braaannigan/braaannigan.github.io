---
layout: post
title:  "Polars & Huggingface datasets"
date:   2022-11-01 11:35:24 +0200
categories: software
---
# [Blog post index](/blog/blog_index.html)

# Polars & Huggingface datasets
Published on: 1st November 2022

This post was created while writing my **Data Analysis with Polars course**. 
[*Check it out on Udemy*](https://www.udemy.com/course/data-analysis-with-polars/?referralCode=A29DCDA40D369080C05A)

One consequence of the Apache Arrow era is that different libraries will integrate more easily.

Here for example we load data from a Huggingface dataset into a Polars dataframe with zero-copy.

```python
from datasets import load_dataset
import polars as pl

dataset = load_dataset("rotten_tomatoes", split="train")
df = pl.from_arrow(dataset.data.table)

shape: (3, 2)
┌───────────────────────────────────────────────────────┬───────┐
│ text                                                  ┆ label │
│ ---                                                   ┆ ---   │
│ str                                                   ┆ i64   │
╞═══════════════════════════════════════════════════════╪═══════╡
│ the rock is destined to be the 21st century's new ... ┆ 1     │
├╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌┤
│ the gorgeously elaborate continuation of " the lor... ┆ 1     │
├╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌┤
│ effective but too-tepid biopic                        ┆ 1     │
└───────────────────────────────────────────────────────┴───────┘
```
Hopefully there will be an explicit `to_polars()` method in datasets.

I'll be digging into this in more detail - can we exploit the memory-mapped datasets that datasets can produce with Polars new out-of-core capabilities?

Also: please don't call libraries datasets😂

# Learn more
Want to know more about Polars for high performance data science and ML? Then you can:
- [join my Polars course on Udemy](https://www.udemy.com/course/data-analysis-with-polars/?referralCode=A29DCDA40D369080C05A) 
- [follow me on twitter](https://twitter.com/braaannigan)
- [connect with me at linkedin](https://www.linkedin.com/in/liam-brannigan-9080b214a/)
- [check out my youtube videos](https://www.youtube.com/watch?v=nGritAo-71o)

or **let me know if you would like a Polars workshop for your organisation**.