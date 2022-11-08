---
layout: post
title:  "ML pre-processing with Polars"
date:   2022-11-08 11:35:24 +0200
categories: software
---
# [Blog post index](/blog/blog_index.html)

# ML pre-processing with Polars
Published on: 8th November 2022

This post was created while writing my **Data Analysis with Polars course**. 
[*Check it out on Udemy*](https://www.udemy.com/course/data-analysis-with-polars/?referralCode=A29DCDA40D369080C05A)

I think we'll see a nice ML pre-processing library develop around Polars in the next year. A recent addition to the library makes an important step on that journey easier...

## Fill some nulls
A common step in ML pre-processing is sharing data from the training set with the test set. For example we may want to fill nulls in the test set with values from the train set.

The new `with_context` method in Polars does just that. It lets you use expressions from one dataframe inside another dataframe!

In the example below we have nulls in the Age column.

```python
(
    test_df
    .with_context(
        # Rename train columns to avoid a column name collision
        train_df.select(pl.all().suffix("_train"))
    )
    # Fill nulls in test with median from train
    .with_column(
        pl.col("Age").fill_null(pl.col("Age_train").median())
    )    
)
```

We want to replace nulls in the test set with the median from the training set.

We do this by calling `with_context` on the test dataframe to bring the train dataframe into the context. Then we can fill some nulls!

## Keeping it lazy
The advantage of with_context is that we stay in the powerful lazy mode in Polars, so we still take advantage of things like query optimisation.

In fact we always do with_context in lazy mode as this is how Polars brings the different parts of the query together.

# Learn more
Want to know more about Polars for high performance data science and ML? Then you can:
- [join my Polars course on Udemy](https://www.udemy.com/course/data-analysis-with-polars/?referralCode=A29DCDA40D369080C05A) 
- [follow me on twitter](https://twitter.com/braaannigan)
- [connect with me at linkedin](https://www.linkedin.com/in/liam-brannigan-9080b214a/)
- [check out my youtube videos](https://www.youtube.com/watch?v=nGritAo-71o)

or **let me know if you would like a Polars workshop for your organisation**.