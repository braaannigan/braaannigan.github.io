---
layout: post
title:  "Fit XGBoost models directly from Polars and Arrow"
date:   2022-10-11 11:35:24 +0200
categories: software
---
# [Blog posts](/blog/blog_index.html)
Published on: 11th October 2022

# Can you use Polars and Apache Arrow to fit ML models?
This post was created while writing my **Data Analysis with Polars course**. 
[*Check it out on Udemy*](https://www.udemy.com/course/data-analysis-with-polars/?referralCode=A29DCDA40D369080C05A)

Polars is backed by Apache Arrow rather than Numpy.
One argument you hear against working in Polars is that you'll have to convert back to Numpy to fit ML models.

Does this argument against using Polars and Apache Arrow libraries hold water?

Nope - it's not true now and will be more invalid over time.

Let's take a Polars dataframe of the Titanic data for an example.

- Do some simple feature engineering
- Pass it to XGBoost in its Arrow form
- Fit the model.

```python
import polars as pl
import xgboost as xgb

df = pl.read_csv(csvPath)
X = (
    df
    .select(["Pclass"])
    .to_dummies()            
    .to_arrow()
)
y = df["Survived"]

model = xgb.XGBClassifier(objective='binary:logistic')
model.fit(X, y)

df = pl.concat([
        df,
        pl.DataFrame(model.predict_proba(X)[:,1],columns=["pos"])
],
    how="horizontal"
)
```

No Numpy or Pandas required.

We can do this because XGBoost introduced support for Arrow in recent months. Other ML and feature engineering libraries are working on Arrow support as well.

In addition, if your library does need a Numpy array then it's often quicker to load and pre-process your data in Polars and then convert to a Numpy array at the last minute rather than using Pandas.

# Learn more
Want to know more about Polars for high performance data science and ML? Then you can:
- [check out my Polars course on Udemy](https://www.udemy.com/course/data-analysis-with-polars/?referralCode=A29DCDA40D369080C05A) 
- [follow me on twitter](https://twitter.com/braaannigan)
- [connect with me at linkedin](https://www.linkedin.com/in/liam-brannigan-9080b214a/)
- [check out my youtube videos](https://www.youtube.com/watch?v=nGritAo-71o)

or **let me know if you would like a Polars workshop for your organisation**.