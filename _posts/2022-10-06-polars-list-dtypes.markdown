---
layout: post
title:  "Don't fear the List dtype in Polars"
date:   2022-10-06 11:35:24 +0200
categories: software
---
# [Blog posts](/blog/blog_index.html)
Published on: 6th October 2022

# What is the Polars `pl.List` dtype?
This post was created while writing my **Data Analysis with Polars course**. 
[*Check it out on Udemy*](https://www.udemy.com/course/data-analysis-with-polars/?referralCode=A29DCDA40D369080C05A)

One of the first things you learn doing data analysis in python is that working with lists are slow.

So you might be wary of the `pl.List` dtype in Polars.

But you shouldn't worry - this dtype is at the core of some fast parallel analysis.

In a List column every row is a Polars Series. And every Series has the same dtype.

Here we create a DataFrame with three list columns: ints, floats and strings. Type is inferred from the first element.
```python
import polars as pl

dfLists = pl.DataFrame({
    'ints':[ [0,1], [2,3]],
    'floats':[ [0.0,1], [2,3]],
    'strings':[ ["0","1"],["2","3"]]
})
dfLists
shape: (2, 3)
┌───────────┬────────────┬────────────┐
│ ints      ┆ floats     ┆ strings    │
│ ---       ┆ ---        ┆ ---        │
│ list[i64] ┆ list[f64]  ┆ list[str]  │
╞═══════════╪════════════╪════════════╡
│ [0, 1]    ┆ [0.0, 1.0] ┆ ["0", "1"] │
├╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌┤
│ [2, 3]    ┆ [2.0, 3.0] ┆ ["2", "3"] │
└───────────┴────────────┴────────────┘
```
# Doing some analysis

The great thing about the List dtype is that you can easily do the same analysis to the Series on each row.
```python
dfLists = pl.DataFrame({
    'ints':[ [0,1], [2,3]],
    'floats':[ [0.0,1], [2,3]],
    'strings':[ ["0","1"],["2","3"]]
})
print(dfLists.select(pl.all().arr.max()))
```

This is a simple example but it can get as gnarly as you need (in parallel if you want).



Although we created them with python lists, they are fast Series.
# Mixing it up?
What happens if we pass a list with a mix of types?

In this case the column has a pl.Object dtype.
```python
dfMixed = pl.DataFrame({
    'ints':[ [0,1], [2,3]],
    'mixed':[ ['a',0],['b',1]]
})
dfMixed
shape: (2, 2)
┌───────────┬──────────┐
│ ints      ┆ mixed    │
│ ---       ┆ ---      │
│ list[i64] ┆ object   │
╞═══════════╪══════════╡
│ [0, 1]    ┆ ['a', 0] │
├╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┤
│ [2, 3]    ┆ ['b', 1] │
└───────────┴──────────┘
```

Every row in a pl.Object dtype is just a python list under the hood. While they can hold arbitrary objects these Object columns won't be so efficient for analysis.

In summary, fear the lists (and maybe fear the `pl.Object`), but don't fear the `pl.Lists`!

# Learn more
Want to know more about Polars for high performance data science and ML? Then you can:
- [check out my Polars course on Udemy](https://www.udemy.com/course/data-analysis-with-polars/?referralCode=A29DCDA40D369080C05A) 
- [follow me on twitter](https://twitter.com/braaannigan)
- [connect with me at linkedin](https://www.linkedin.com/in/liam-brannigan-9080b214a/)
- [check out my youtube videos](https://www.youtube.com/watch?v=nGritAo-71o)

or **let me know if you would like a Polars workshop for your organisation**.