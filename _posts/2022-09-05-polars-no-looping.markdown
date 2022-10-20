---
layout: post
title:  "Don't loop over columns in Polars"
date:   2022-09-05 11:35:24 +0200
categories: software
---
# [Blog posts](/blog/blog_index.html)
Published on: 5th September 2022

# Don't loop over columns in Polars
This post was created while writing my **Data Analysis with Polars course**. 
[*Check it out on Udemy*](https://www.udemy.com/course/data-analysis-with-polars/?referralCode=A29DCDA40D369080C05A)

If you're writing Polars code like this
```python
for col in df.columns:
do stuff
```
then **STOP!!!!**

Instead, use **expressions** and then Polars will parallelise the loop over the columns for you. By looping explicitly in python you're killing the parallelisation.

For example if we want to count the number of unique values in every column we do
```python
df.select(pl.all().n_unique())
```

or if we wanted to count the number of unique values but only in string (Utf8) columns we do
```python
df.select(pl.col(pl.Utf8)).select(pl.all().n_unique())
```

Doing it this way with expressions will will give you the 🚀 performance you expect!

# Learn more
Want to know more about Polars for high performance data science? Then you can:
- [follow me on twitter](https://twitter.com/braaannigan)
- [connect with me at linkedin](https://www.linkedin.com/in/liam-brannigan-9080b214a/)
- [check out my youtube videos](https://www.youtube.com/watch?v=nGritAo-71o)

or **let me know if you would like a Polars workshop for your organisation**.