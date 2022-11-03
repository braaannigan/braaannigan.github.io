---
layout: post
title:  "Polars 🤝 Matplotlib"
date:   2022-11-03 11:35:24 +0200
categories: software
---
# [Blog post index](/blog/blog_index.html)

# Polars 🤝 Matplotlib
Published on: 3rd November 2022

This post was created while writing my **Data Analysis with Polars course**. 
[*Check it out on Udemy*](https://www.udemy.com/course/data-analysis-with-polars/?referralCode=A29DCDA40D369080C05A)

Polars gets on well with matplotlib.

To make a bar chart for example we pass columns directly from a Polars dataframe.

In the first example below we see the maximum wave height from Irish wave buoys in the North Atlantic (this is just a snippet to give you an idea of how it works).
```python
stationAggs = stationAggs.sort("significant_wave_height_max").tail(6)

fig, ax = plt.subplots()

ax.barh(
    y=stationAggs["stationID"],
    width=stationAggs["significant_wave_height_max"],
)
ax.set_xlabel('Max wave height (m)')
```
![Maximum wave height at Irish wave buoys](/img/matplotlib_max_wave_height.png)


Can we do some storm-tracking as well?

In the second example we take 3 hour averages of the wave height for each station with the fast groupby_dynamic method.

To do multi-line plots we need to call the ax.plot method for each line. When can do this by looping through a groupby object to get the data for each station and see a storm with some chunky waves arriving on 26th September.
```python

# Average time series for each station into 3 hour windows
averagedValuesDf = (
    dfBigWaves
    .groupby_dynamic("time","3h",by="stationID")
     .agg(
            pl.col("significant_wave_height").mean()
        )
)
fig,ax = plt.subplots(figsize=(12, 4), dpi=80)
# Loop through the groupby to get the values for each station
for stationDf in averagedValuesDf.groupby("stationID"):
    stationID = stationDf[0,0]
    # Add a line for each station
    ax.plot(
        stationDf["time"],
        stationDf["significant_wave_height"],
        label=stationID
)
plt.legend()
```
![Time series of wave height at Irish wave buoys](/img/matplotlib_wave_time_series.png)


# Learn more
Want to know more about Polars for high performance data science and ML? Then you can:
- [join my Polars course on Udemy](https://www.udemy.com/course/data-analysis-with-polars/?referralCode=A29DCDA40D369080C05A) 
- [follow me on twitter](https://twitter.com/braaannigan)
- [connect with me at linkedin](https://www.linkedin.com/in/liam-brannigan-9080b214a/)
- [check out my youtube videos](https://www.youtube.com/watch?v=nGritAo-71o)

or **let me know if you would like a Polars workshop for your organisation**.