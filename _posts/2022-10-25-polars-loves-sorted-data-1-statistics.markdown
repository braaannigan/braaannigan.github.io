---
layout: post
title:  "Polars ❤️ sorted data 1: statistics"
date:   2022-10-25 11:35:24 +0200
categories: software
---
# [Blog posts](/blog/blog_index.html)
Published on: 25th October 2022

# Polars ❤️ sorted data 1: statistics
This post was created while writing my **Data Analysis with Polars course**. 
[*Check it out on Udemy*](https://www.udemy.com/course/data-analysis-with-polars/?referralCode=A29DCDA40D369080C05A)

Sorting data imposes a lot of order on it so it would be great if our data processing tools take advantage of this. One under-appreciated aspect of Polars is that it has fast-track algorithms that can take advantage of sorting. 

## Fast-track algorithms: a simple introduction
So what do we mean by fast-track algorithms? Let's start with a simple example. We have a Polars `DataFrame` with a sorted integer column and we want to get the maximum value.

The standard algorithm for finding the maximum value is to set the first value to be the maximum value. Then we iterate through the reminder of the column. When we find a value greater than the current maximum then we set that as the maximum value and continue. This is O(N) where N is the number of rows in the column.

The fast-track algorithm on a sorted column is to take the last value. This is O(1).
We can test this with the following example where we vary `N`.
```python
import polars as pl
import numpy as np

N = 1_000_000_000

df = pl.DataFrame(np.arange(N))
df = df.with_column(pl.col(col).set_sorted())
df_pandas = df.to_pandas()

# Get the maximum values
df["column_0"].max()
df_pandas["column_0"].max()
```
In this example with 1 billion rows:
- Pandas takes 3.7 seconds to get the maximum value
- Polars with the standard algorithm takes 2.3 seconds to get the maximum value
- Polars with the fast-track algorithm takes 24 *microseconds* to get the maximum value

More importantly, if we change `N` Polars requires the same amount of time on sorted data whereas the time for Pandas grows linearly.

While the maximum value is obviously the simplest example there are other statistics that can benefit. For example, we can get the median value by jumping straight to the middle of the array and applying any interpolation needed. More generally, we can calculate any quantile with a fast-track algorithm in this way.

## How does Polars know the column is sorted?
In order to apply a fast-track algorithm Polars needs to know a column is sorted. It does this using boolean variables for each column that states the column is sorted in an ascending or descending manner. These are set to `False` by default. There are two ways to change these variables. 

Firstly, you might apply a sorting operation - such as `sort` on a column. If you do this Polars will change the boolean variable for that column for either ascending or descending.

Secondly, you can tell Polars a column is sorted using the `set_sorted` expression (see the example in the next section).

It's important to understand that Polars will never actually check to see if a column is sorted. If you aren't totally sure it's best to just call `sort` on that column.

## Groupby on sorted data
Statistics on sorted data is just the start. Polars also has fast-track algorithms for doing `groupby` on a sorted column. In this case Polars exploits the sorting when identifying the unique groupby keys.

In this example the sorting leads to a 40% speedup regardless of the size of `N`.
```python
import polars as pl
import numpy as np

df = pl.DataFrame(np.sort(np.random.randint(0,9,N))).with_row_count("row_nr")
%timeit -n1 -r1  df.groupby(col).agg(pl.col(row).mean())

df = df.with_column(pl.col(col).set_sorted())
%timeit -n1 -r1  df.groupby(col).agg(pl.col(row).mean())
```


# Learn more
Want to know more about Polars for high performance data science and ML? Then you can:
- [check out my Polars course on Udemy](https://www.udemy.com/course/data-analysis-with-polars/?referralCode=A29DCDA40D369080C05A) 
- [follow me on twitter](https://twitter.com/braaannigan)
- [connect with me at linkedin](https://www.linkedin.com/in/liam-brannigan-9080b214a/)
- [check out my youtube videos](https://www.youtube.com/watch?v=nGritAo-71o)

or **let me know if you would like a Polars workshop for your organisation**.