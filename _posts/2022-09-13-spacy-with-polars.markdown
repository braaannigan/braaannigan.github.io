---
layout: post
title:  "Using Spacy with Polars?"
date:   2022-09-13 11:35:24 +0200
categories: software
---
# How do third-party libraries work with Polars?
One thing people ask me about switching from Pandas to Polars is working with 3rd party libraries. What if they don't support Polars?

Often, however, this isn't much of an issue...

Take the example below with the NLP library Spacy. Here Spacy takes a column from a Polars dataframe in the same way it would take a column from a Pandas dataframe.

```python
import spacy
nlp = spacy.load("en_core_web_sm")

doc = nlp(df[0,"text"])
spacy.displacy.render(doc, style="ent")
```
![Output of Spacy annotated renderer from Polars input](/img/spacy_polars.png)

Why does this work so smoothly? Because many libraries aren't looking for a pandas dataframe column - they just want an iterable. A pandas column is an iterable, but so is a tuple, list or a polars dataframe column.

# Learn more
Want to know more about Polars for high performance data science and ML? Then you can:
- [follow me on twitter](https://twitter.com/braaannigan)
- [connect with me at linkedin](https://www.linkedin.com/in/liam-brannigan-9080b214a/)
- [check out my youtube videos](https://www.youtube.com/watch?v=nGritAo-71o)

or [**join me at my next workshop to help teams make the Pandas to Polars transition in Belfast on September 21st 2022**](https://www.eventbrite.com/e/from-pandas-to-polars-tickets-399410917807?aff=ebdssbdestsearch).

Let me know if you would like a workshop for your organisation.