---
layout: post
title:  "Breaking your bad habits with Polars"
date:   2022-10-04 11:35:24 +0200
categories: software
---
# Breaking your bad habits with Polars
One comment we get on the Polars discourse is that the Polars syntax encourages people to break bad habits they developed in Pandas.

Take the .apply (or .applymap) function for example. I see lots of people using this in Kaggle comps, even though it's bad news.

In this example we want to map positive values to 1 and negative values to -1 for all columns.

Using the standard pl.when method in Polars is 100x faster than an apply method in Pandas*

*Further optimizations are available on this toy problem in both libraries!
```python
import polars as pl
import numpy as np

# Create a random DataFrame
N = 100_000
dfNumeric = pl.DataFrame(np.random.standard_normal((N,100)))
dfp = dfNumeric.to_pandas()

# Set values to 1 when they are positive and 0 otherwise
(
    dfp
    .applymap(lambda x: 1 if x > 0 else 0)
)
# Time: 2.5 seconds
(
    dfNumeric
    .with_columns(
        [
            pl.when(pl.col(col) > 0).then(1).otherwise(0).alias(col) for col in df.columns
            ]
            )
)
# Time: 30 milliseconds
```
The shift away from .apply functions happened for me as well. 

In Pandas I used to call .apply fairly often, but the only time I've used .apply in Polars was...when writing the docs to tell people not to use .apply!
# Learn more
Want to know more about Polars for high performance data science and ML? Then you can:
- [follow me on twitter](https://twitter.com/braaannigan)
- [connect with me at linkedin](https://www.linkedin.com/in/liam-brannigan-9080b214a/)
- [check out my youtube videos](https://www.youtube.com/watch?v=nGritAo-71o)

or **let me know if you would like a Polars workshop for your organisation**.