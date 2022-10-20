---
layout: post
title:  "Flexible time series aggregations in Polars"
date:   2022-09-12 11:35:24 +0200
categories: software
---
# [Blog posts](/blog/blog_index.html)
Published on: 12th September 2022

# Time series aggregations with `groupby_dynamic`
This post was created while writing my **Data Analysis with Polars course**. 
[*Check it out on Udemy*](https://www.udemy.com/course/data-analysis-with-polars/?referralCode=A29DCDA40D369080C05A)

Time series aggregations in Polars are fast and flexible.

In a recent project I had 10 years of two minute data from telemetry and needed hourly averages -approx 2.5 million rows X 100 columns.

In Polars I used groupby_dynamic - turned out to be **10x faster than Pandas** leading to happy clients!

```python
# Create Polars DataFrame
df = pl.DataFrame({
    'date':pl.date_range(datetime(2010,1,1),datetime(2021,1,2),interval='2m'),
})
df = pl.concat([df,pl.DataFrame(np.random.standard_normal((len(df),100)))],how='horizontal')

# Hourly groupby with Polars
df.groupby_dynamic("date",every='1h').agg(pl.all().exclude('date').mean())
# Time: 0.25 seconds


# Hourly groupby with Pandas
dfPandas.groupby(pd.Grouper(key='date',freq='1h')).mean()
# Time: 2.5 seconds
```

# Hourly groupby over 3-hour windows with Polars

To handle high-frequency variability I also needed to do this on 3-hour rolling windows.

Not a problem - you can specify the interval period to get the rolling average required with no performance cost.
```python
df.groupby_dynamic("date",every='1h',period='3h').agg(pl.all().exclude('date').mean())
```
# Learn more
Want to know more about Polars for high performance data science and ML? Then you can:
- [check out my Polars course on Udemy](https://www.udemy.com/course/data-analysis-with-polars/?referralCode=A29DCDA40D369080C05A) 
- [follow me on twitter](https://twitter.com/braaannigan)
- [connect with me at linkedin](https://www.linkedin.com/in/liam-brannigan-9080b214a/)
- [check out my youtube videos](https://www.youtube.com/watch?v=nGritAo-71o)

or **let me know if you would like a Polars workshop for your organisation**.