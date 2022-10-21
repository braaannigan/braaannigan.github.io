---
layout: post
title:  "Polars doesn't have an index but what if you want one. Or many."
date:   2022-10-11 11:35:24 +0200
categories: software
---
# [Blog posts](/blog/blog_index.html)
Published on: 21st October 2022

# Polars doesn't have an index but what if you want one. Or many?
This post was created while writing my **Data Analysis with Polars course**. 
[*Check it out on Udemy*](https://www.udemy.com/course/data-analysis-with-polars/?referralCode=A29DCDA40D369080C05A)

Polars doesn't have an index. That's great because it saves a lot of time setting and resetting indices. 

But what if you want fast access to subsets of the data that you access often?

## Partitioning a `DataFrame`
One way to solve this is to partition your dataframe. 

In Polars we can do this with `partition_by`. 

We tell it which column(s) we want to partition by and Polars creates a dictionary that maps from the unique values to a DataFrame with the corresponding rows.

```python
import polars as pl

df = pl.DataFrame(
  {"keys":["a","b","a"],"values":[0,1,2]}
)

# Create a partition mapping on the keys column
partitions_dict = (
  df
  .partition_by("keys",as_dict=True)
)

# Access the sub-DataFrame for key "a"
partitions_dict["a"]
shape: (2, 2)
┌──────┬────────┐
│ keys ┆ values │
│ ---  ┆ ---    │
│ str  ┆ i64    │
╞══════╪════════╡
│ a    ┆ 0      │
├╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌┤
│ a    ┆ 2      │
└──────┴────────┘
```
The dataframes in the partition_by mapping are copies, so this is memory intensive if you want to partition in multiple ways.

## Using `groupby`
But there is an alternative - you can use a humble `groupby`.

What is a `groupby`? It's a mapping from keys to row indices as captured in the `_groups` method .
```python
import polars as pl

df = pl.DataFrame(
  {
   "keys1":["a","b","a"],
   "keys2":["c","c","d"],
   "values":[0,1,2]}
)

# Create a groupby mapping on the keys1 column
keys1_groups = (
	df
    .groupby("keys1")
    ._groups()
)
shape: (2, 2)
┌───────┬───────────┐
│ keys1 ┆ groups    │
│ ---   ┆ ---       │
│ str   ┆ list[u32] │
╞═══════╪═══════════╡
│ a     ┆ [0, 2]    │
├╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌┤
│ b     ┆ [1]       │
└───────┴───────────┘
```
One advantage of using `groupby` is that it's cheap memory wise - basically the equivalent of a single extra 32-bit integer column to store the row indices for each mapping.

And unlike a Pandas `Index` or `MultIindex` you can define lots of different group indices at the same time.

The last step is to make a fast mapping from keys to the sub-`DataFrame` for that key. 

To do this we unwrap the `groupby._groups` `DataFrame` to a dictionary and then we can access our sub-`DataFrame` quickly

```python

df = pl.DataFrame(
  {
   "keys1":["a","b","a"],
   "keys2":["c","c","d"],
   "values":[0,1,2]}
)

# Create a groupby mapping on the keys1 column
keys1_groups = (
	df
    .groupby("keys1")
    ._groups()
)
# Convert to a dictionary from keys to row indices
keys1_dict = {
    el["keys1"]:el["groups"] for el in keys1_groups.to_dicts()
}
# Set the key of interest
key = "a"
# Get the sub-DataFrame for that key
(
    df[
        keys1_dict[key]
    ]
)
shape: (2, 3)
┌───────┬───────┬────────┐
│ keys1 ┆ keys2 ┆ values │
│ ---   ┆ ---   ┆ ---    │
│ str   ┆ str   ┆ i64    │
╞═══════╪═══════╪════════╡
│ a     ┆ c     ┆ 0      │
├╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌┤
│ a     ┆ d     ┆ 2      │
└───────┴───────┴────────┘
```
So there you have it - a Postgres-style index* on a DataFrame.

*Well obviously there's more to a Postgres index but this will work for lots of use cases!

# Learn more
Want to know more about Polars for high performance data science and ML? Then you can:
- [check out my Polars course on Udemy](https://www.udemy.com/course/data-analysis-with-polars/?referralCode=A29DCDA40D369080C05A) 
- [follow me on twitter](https://twitter.com/braaannigan)
- [connect with me at linkedin](https://www.linkedin.com/in/liam-brannigan-9080b214a/)
- [check out my youtube videos](https://www.youtube.com/watch?v=nGritAo-71o)

or **let me know if you would like a Polars workshop for your organisation**.