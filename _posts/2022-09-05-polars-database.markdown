---
layout: post
title:  "Loading from a database with Polars"
date:   2022-09-05 11:35:24 +0200
categories: software
---
# Loading from a database with Polars
On some projects the challenge is that you've got a big dataset but only want to look at well-defined subsets of the data at any given moment.

One powerful way to approach this is to take advantage of databases and their ability to sub-select data.

# Create a local database
First you take your dataset and write it to an SQLite DB with Pandas. Then create an index on the column you want to define subsets on.
![Create a Database with an index using Pandas and SQLite](/img/create_db_index.png)

In this case we only do it on the passenger number column, but you can do more advanced indexes on multiple columns.

# Read from the database
Then you use Polars and connectorx - the fastest way to read from a database in python.
![Read from the database with Polars](/img/read_sql.png)

Add a where clause into your SQL statement to choose your subset. The data will be filtered in the DB before being read into the dataframe.

Reading from a database isn't as fast as using IPC or Parquet files.

However, the DB approach is very powerful when you are selecting small parts from large datasets. It's also handy when you just need to work with a DB!

Follow me if you're interested in learning more about high performance data processing in python!

# Learn more
Want to know more about Polars for high performance data science? Then you can:
- [follow me on twitter](https://twitter.com/braaannigan)
- [connect with me at linkedin](https://www.linkedin.com/in/liam-brannigan-9080b214a/)
- [check out my youtube videos](https://www.youtube.com/watch?v=nGritAo-71o)

or **let me know if you would like a Polars workshop for your organisation**.