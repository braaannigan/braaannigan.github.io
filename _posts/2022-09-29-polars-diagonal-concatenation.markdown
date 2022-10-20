---
layout: post
title:  "Combining data with different schemas"
date:   2022-09-29 11:35:24 +0200
categories: software
---
# [Blog posts](/blog/blog_index.html)
Published on: 29th September 2022

# Combining data with different schemas
This post was created while writing my **Data Analysis with Polars course**. 
[*Check it out on Udemy*](https://www.udemy.com/course/data-analysis-with-polars/?referralCode=A29DCDA40D369080C05A)

You've got a bunch of data files in your project and they all follow a consistent data schema 😊

You get a new file and see that from now on there will be some useful extra columns. How are you going to combine this file with the old stuff?? 😣

A vertical concatenation won't work as it doesn't like schema changes.

This is where diagonal concatenation in Polars comes in. 
```python
# Old schema year, exporter, importer
dfTrades2020 = pl.DataFrame(
    [
        {"year":2020,"exporter":"China","importer":"USA"},
        {"year":2020,"exporter":"China","importer":"USA"},
    ]
)
# New schema includes value
dfTrades2021 = pl.DataFrame(
    [
        {"year":2021,"exporter":"China","importer":"USA","value":10},
        {"year":2021,"exporter":"China","importer":"USA","value":100},
    ]
)
# Diagonal concatenation
pl.concat([dfTrades2020,dfTrades2021],how="diagonal")
```
Diagonal concatenation appends your new records with their new columns, and add nulls to the new columns for the old records to show the data is missing. Sorted.

![Output of the diagonal concatenation](/img/diag_concat_output.png)


# Learn more
Want to know more about Polars for high performance data science and ML? Then you can:
- [check out my Polars course on Udemy](https://www.udemy.com/course/data-analysis-with-polars/?referralCode=A29DCDA40D369080C05A) 
- [follow me on twitter](https://twitter.com/braaannigan)
- [connect with me at linkedin](https://www.linkedin.com/in/liam-brannigan-9080b214a/)
- [check out my youtube videos](https://www.youtube.com/watch?v=nGritAo-71o)

or **let me know if you would like a Polars workshop for your organisation**.