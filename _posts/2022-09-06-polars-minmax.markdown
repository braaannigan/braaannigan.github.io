---
layout: post
title:  "Doing ML pre-processing in Polars"
date:   2022-09-06 11:35:24 +0200
categories: software
---
# ML in Polars
One thing I'll be exploring in my Polars online course is seeing how far we can go with machine learning (ML) in Polars.

As well as ML models, scikit-learn has lots of data pre-processing functionality. Let's see if it's worth doing some of this pre-processing in Polars.

# Min-max example
Simple example: we have a dataframe with 100k rows, 100 columns and want to do min-max scaling on each column.
```python
import polars as pl
import numpy as np
from sklearn.preprocessing import MinMaxScaler

N = 100000
df = pl.DataFrame(np.random.standard_normal((N,100)))
arr = df.to_numpy()

# Using sklearn
minMax = MinMaxScaler()
minMax.fit_transform(arr)
Time: 90 ms

# Using Polars
df.select(
    (pl.all()-pl.all().min()) / (pl.all().max()-pl.all().min())
)
Time: 40 ms
```
So Polars is 2x faster in this comparison.

This is just the start of the ML journey with Polars! For example, we can make a class to wrap the Polars code with the scikit-learn API. Then we can stay in the fast & memory efficient Polars & ApacheArrow combo as long as possible before converting to numpy for the ML model.

# Learn more
Want to know more about Polars for high performance data science and ML? Then you can:
- [follow me on twitter](https://twitter.com/braaannigan)
- [connect with me at linkedin](https://www.linkedin.com/in/liam-brannigan-9080b214a/)
- [check out my youtube videos](https://www.youtube.com/watch?v=nGritAo-71o)

or **let me know if you would like a Polars workshop for your organisation**.