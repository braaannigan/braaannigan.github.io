---
layout: post
title:  "Polars ❤️ sorted data 1: statistics"
date:   2022-10-25 11:35:24 +0200
categories: software
---
# [Blog post index](/blog/blog_index.html)

# Polars ❤️ sorted data 1: statistics
Published on: 26th October 2022

This post was created while writing my **Data Analysis with Polars course** -  
[*Check it out on Udemy*](https://www.udemy.com/course/data-analysis-with-polars/?referralCode=A29DCDA40D369080C05A)

TLDR: Polars has fast-track algorithms to calculate some statistics. We look at examples of this and then look at how Polars knows if a column is sorted.

Sorting column in a dataframe imposes order on it. It would be great if our data processing tools take advantage of this structure. One under-appreciated aspect of Polars is that it has fast-track algorithms that can do just this with sorted data. 

## Fast-track algorithms: a simple introduction
So what do we mean by fast-track algorithms? Let's start with a simple example. We have a Polars `DataFrame` with a sorted integer column and we want to get the maximum value.

The standard algorithm for finding the maximum value is to:
- set the first value to be the maximum value 
- then iterate through the reminder of the column
- when we find a value greater than the current maximum set that as the new maximum value

This algorithm is O(N) where N is the number of rows in the column.

The fast-track algorithm on a sorted column is just to take the last value. This is O(1).

To test whether these scalings hold we compare the length of time needed to get the maximum value in Polars - which has fast-track algorithms for sorted data - and Pandas which does not.

```python
import polars as pl
import numpy as np

N = 1_000_000

# Create a dataframe with a column of pre-sorted data
df = pl.DataFrame(np.sort(np.random.randint(0,9,N)))
# Set the name of the column
col = "column_0"
# Tell Polars column_0 is sorted
df = df.with_column(pl.col(col).set_sorted())
# Convert the dataframe to Pandas for comparison
df_pandas = df.to_pandas()

# Get the maximum values
df["column_0"].max()
df_pandas["column_0"].max()
```
We time execution for a range of `N` (all times in microseconds)
|N     | Pandas |  Polars |
|------|--------|---------|
| 10^6 | 700    | 21      |
| 10^7 | 5,000  | 20      |
| 10^8 | 64,000 | 20      |
| 10^9 | 530,000| 10      |

So the time taken is 20 microseconds for Polars regardless of the size of `N` but grows linearly for Pandas.

The maximum value is the simplest example of a fast-track algorithm. There are also other statistics that can benefit. 

For example, if we want the median value the standard algorithm first requires a sort before extracting some values in the middle of the array (depending on the exact interpolation method used). More generally, we can calculate any quantile with a fast-track algorithm in this way.

## How does Polars know the column is sorted?
In order to apply a fast-track algorithm **Polars needs to know a column is sorted**. Polars keeps track of whether a column is sorted in a pair of boolean variables. These variables states whether Polars **thinks** the column is sorted in an ascending or descending manner. 

We can see the current state of these variables with the `flags` attribute on a `Series.

```python
df["column_0"].flags
{'SORTED_ASC': True, 'SORTED_DESC': False}
```

By default these flags are are set to `False` for all columns. There are two ways to change these flags. 

Firstly, you can use a method that implies a sort on the column - such as the `sort` method:
```python
df = df.sort("column_0")
```

If you do this Polars will change the flag for the sorted column for either ascending or descending.

Secondly, you can tell Polars a column is sorted using the `set_sorted` expression. We did this in the example above in the following line:
```python
df = df.with_column(pl.col(col).set_sorted())
```

It's important to understand that Polars doesn't check if a column is sorted. If you aren't totally sure a column is sorted and want to access the fast-track algorithms it's best to call `sort` on that column to make sure.

This is just the start of how Polars takes advantage of sorted data, we'll look at further example of fast-track algorithms in coming posts or you can join me on my course to get the full picture.



# Learn more
Want to know more about Polars for high performance data science and ML? Then you can:
- [join me on my Polars course on Udemy](https://www.udemy.com/course/data-analysis-with-polars/?referralCode=A29DCDA40D369080C05A) 
- [follow me on twitter](https://twitter.com/braaannigan)
- [connect with me at linkedin](https://www.linkedin.com/in/liam-brannigan-9080b214a/)
- [check out my youtube videos](https://www.youtube.com/watch?v=nGritAo-71o)

or **let me know if you would like a Polars workshop for your organisation**.