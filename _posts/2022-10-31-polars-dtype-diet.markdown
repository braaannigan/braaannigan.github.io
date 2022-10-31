---
layout: post
title:  "Polars on a diet"
date:   2022-10-31 11:35:24 +0200
categories: software
---
# [Blog post index](/blog/blog_index.html)

# Polars on a diet
Published on: 31st October 2022

This post was created while writing my **Data Analysis with Polars course**. 
[*Check it out on Udemy*](https://www.udemy.com/course/data-analysis-with-polars/?referralCode=A29DCDA40D369080C05A)

Polars has a built in tool to go on a dtype diet.

Call the `shrink_dtype` expression and it will convert the column to the dtype that requires the least amount of memory based on the data in the column.

```python
import polars as pl

(
  pl.DataFrame(
  	{
    	"a": [1, 2, 3],
        "b": [1, 2, 2 << 32],
        "c": [-1, 2, 1 << 30],
        "d": [-112, 2, 112],
        "e": [-112, 2, 129],
        "f": ["a", "b", "c"],
        "g": [0.1, 1.32, 0.12],
        "h": [True, None, False],
     }
    )
  .select(
    pl.all().shrink_dtype()
  )
)
┌─────┬────────────┬────────────┬──────┬──────┬─────┬──────┬───────┐
│ a   ┆ b          ┆ c          ┆ d    ┆ e    ┆ f   ┆ g    ┆ h     │
│ --- ┆ ---        ┆ ---        ┆ ---  ┆ ---  ┆ --- ┆ ---  ┆ ---   │
│ i8  ┆ i64        ┆ i32        ┆ i8   ┆ i16  ┆ str ┆ f32  ┆ bool  │
╞═════╪════════════╪════════════╪══════╪══════╪═════╪══════╪═══════╡
│ 1   ┆ 1          ┆ -1         ┆ -112 ┆ -112 ┆ a   ┆ 0.1  ┆ true  │
├╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌┼╌╌╌╌╌╌┼╌╌╌╌╌┼╌╌╌╌╌╌┼╌╌╌╌╌╌╌┤
│ 2   ┆ 2          ┆ 2          ┆ 2    ┆ 2    ┆ b   ┆ 1.32 ┆ null  │
├╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌┼╌╌╌╌╌╌┼╌╌╌╌╌┼╌╌╌╌╌╌┼╌╌╌╌╌╌╌┤
│ 3   ┆ 8589934592 ┆ 1073741824 ┆ 112  ┆ 129  ┆ c   ┆ 0.12 ┆ false │
└─────┴────────────┴────────────┴──────┴──────┴─────┴──────┴───────┘
```
Both floats and integers default to 64-bit precision. In the example below from the API docs Polars sees that column "a" could be 8-bit, column "b" must be 64-bit, but column "c" could be 32-bit.

Casting numeric columns from 64-bit to 32-bit is often the easiest win in data science. Memory usage halves and computation time might also be half that of 64-bit.

You do need to check that the loss of precision is ok. I had sensors accurate to 0.01 so a change of 10^-6 was 👍

In my udemy course I show that if you cast to 8- or 16-bits memory usage continues to fall proportionally...

...but computation time probably won't be better than 32-bits!

Most modern CPUs don't have native support for 8- or 16-bit so they have to emulate it.

String columns with lots of repeated entries can also usefully be cast to categoricals. But that's a story for another day.

# Learn more
Want to know more about Polars for high performance data science and ML? Then you can:
- [join my Polars course on Udemy](https://www.udemy.com/course/data-analysis-with-polars/?referralCode=A29DCDA40D369080C05A) 
- [follow me on twitter](https://twitter.com/braaannigan)
- [connect with me at linkedin](https://www.linkedin.com/in/liam-brannigan-9080b214a/)
- [check out my youtube videos](https://www.youtube.com/watch?v=nGritAo-71o)

or **let me know if you would like a Polars workshop for your organisation**.