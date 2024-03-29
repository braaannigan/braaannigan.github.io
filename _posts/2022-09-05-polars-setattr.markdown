---
layout: post
title:  "Setting an attribute shortcut in python"
date:   2022-09-05 11:35:24 +0200
categories: software
---
# [Blog posts](/blog/blog_index.html)
Published on: 5th September 2022

This post was created while writing my **Data Analysis with Polars course**. 
[*Check it out on Udemy*](https://www.udemy.com/course/data-analysis-with-polars/?referralCode=A29DCDA40D369080C05A)

There's a tension between having clear verbose code and code that's quick and easy to type.

Verbose code is great for production, but when doing rapid data exploration in ipython or jupyter you really want something quick.

To address this you can use setattr to set up an alias for your function.
![Code to set your attribute shortcut](/img/setattr.jpeg)
In my case I use value_counts() a lot, so I alias the function with vc. This means it goes from 12 characters to 2.

It's also good to drop the underscore - these double press chars put a lot more stress on your fingers when repeated!

H/T [Ritchie Vink](https://twitter.com/RitchieVink) for sharing this method with me.

Follow me if you're interested in learning more about high performance data processing in python!

# Learn more
Want to know more about Polars for high performance data science? Then you can:
- [follow me on twitter](https://twitter.com/braaannigan)
- [connect with me at linkedin](https://www.linkedin.com/in/liam-brannigan-9080b214a/)
- [check out my youtube videos](https://www.youtube.com/watch?v=nGritAo-71o)

or **let me know if you would like a Polars workshop for your organisation**.