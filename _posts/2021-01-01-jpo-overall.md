---
layout: post
title:  "JPO at 50: Part I"
date:   2021-01-01 10:35:24 +0200
categories: oceanography, nlp
---

# Looking back at 50 years of the Journal of Physical Oceanography from a language perspective
The Journal of Physical Oceanography (JPO) has been a leading journal for physical oceanographers since its
establishment 50 years ago. I want to look back over this period from a different perspective - using the modern
Natural Language Processing (NLP) methods I've learned as a data scientist.

The main aim of this project is to see if we can identify longer-term changes in the field that are not easily apparent except to those who experienced the changes first-hand. A secondary aim is to see to whether an NLP-based approach can generate any additional insight for a very quantiative environmental science.

The data I use are the text of the titles and abstracts from every issue of JPO along with year of publication.
This gives almost 7800 articles. I omit articles that are replies, editorials, comments etc. or are simply missing their
abstract to have a final dataset of 7400 articles. As I am focusing on text I do not use other data such as authors, affiliations or citations. 

I have limited the text analysis to title and abstract as these reflect what the authors think are the essence of the article. I split the analysis into a number of sections that can be thought of as *where*, *what*, *why* and *how*. 

In addition, in this introductory article I look at the text in aggregations to see some overall patterns. We see how the number of articles grew rapidly - but only for a while - and how titles have experienced constant expansion while abstracts have been brought under control.



## Number of articles
The number of articles has increased over time. However, while I expected a more or less continual growth in the number of articles the reality has been quite different. There was a period of exponential growth in the first decade which saw the number of articles published increase from 40 in 1971 to 170 in 1980. Since then the number of articles has oscilliated from a nadir of 114 articles in 1992 to a peak of 228 articles in 2001.
![Number of articles per year](/img/totalArticles.svg)

The increase in the number of articles published is due to an increase in the number of issues per year and the number of
articles per issue. In recent years there is generally about 15 articles across 12 issues. In contrast, in 1972 there were just 4 issues and the first issue had just a single article ("A Study of the Bottom Boundary Layer of the Florida Current" by G. Weatherly).


## Length of titles
![Length of articles' titles](/img/titleLength.svg)

If we are looking for near-perpetual growth in oceanography the place to look is the length of article titles. These titles have seen growth from a pithy average of 62 characters in 1971 to 88 characters in 2020.  We fit a geometric model to this time series to find that title length growth is about 0.065% per annum. These longer titles are mainly due to more words in titles, but there has also been a small increase in the mean length of words in titles.

The longest title at 224 characters / 27 words is from a 2015 article: "Freshwater Flux and Spatiotemporal Simulated Runoff Variability into Ilulissat Icefjord, West Greenland, Linked to Salinity and Temperature Observations near Tidewater Glacier Margins Obtained Using Instrumented Ringed Seals". This title captures a few of the trends that have lengthened titles: greater
specificity in topic of study, location and methods along with more hints at the results.

An inspection of the shortest titles shows that longer titles are an inevitable consequence of the maturation and specialisation of a subject area. For example, it would be impossible to call an article something as simple as "The Instability of a Baroclinic Vortex" if working in the same domain today. The shortest article title of all is 1975's very straightforward "MODE tides".

## Length of abstracts
![Length of articles' abstracts](/img/abstractLength.svg)

Given in the increasing length of titles I expected abstracts to grow in a similar way. However, abstracts instead grew rapidly from around 750 characters in the early years to double this length by the early 2000s with a peak of 1556 characters in 2000 (left plot). Abstract length has since contracted by 10% to around 1400 characters in the most recent decade. 

We can understand why the abstracts are curtailed by looking at the distribution of the number of words in the abstract (right plot). The blue box shows the limits of the first and third quartiles, the vertical lines show the 95% range and the dots shows values outside the 95% range. The blue boxes show that how all abstracts generally got longer from the early 1970s until around 2000. An abstract that would have been relatively long in the early 1970s would have been relatively short by the 1990s. The increase in mean abstract length was partly driven by the emergence of very long (400 word+) abstracts. In the 2000s it appears that the journal started trying to limit abstract length as the very long abstracts disappeared. In the most recent decade it appears that abstract length has become a hard limit with very few articles having an abstract longer than 300 words. 

The longest abstract was found in the 1980 article "A Numerical Study of Loop Current Intrusions and Eddy Shedding" and came in at an awesome length of 4653 characters. Inspection of the titles for the longest abstracts shows no particular pattern in terms of the study material: observational, numerical and theoretical studies are found while the study material is similarly varied including large-scale circulation, surface wave dynamics and turbulent dynamics.

One feature that has almost disappeared in recent years is the 'tweetable' abstract - that is an abstract of less than 280 characters. Consider this example from 1992 "The rapid changes in density observed near the continental slope in association with internal waves are explained as nonlinear features of wave reflection". In this case the abstract was just twice the length of the title.  Until 2000 there were at least a few of these short abstracts every year but in recent years even the shortest
abstracts have had more than 700 characters or 200 words.