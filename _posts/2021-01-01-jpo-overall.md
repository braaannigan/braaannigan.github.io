---
layout: post
title:  "JPO at 50: Part I"
date:   2021-01-01 10:35:24 +0200
categories: oceanography
---

# 50 years of the Journal of Physical Oceanography: using NLP to understand how oceanography has evolved.
The Journal of Physical Oceanography (JPO) has been a leading journal for physical oceanographers since its
establishment 50 years ago. I want to look back over this period from a different perspective - using Natural Language Processing (NLP) methods I've learned as a data scientist.

I'm doing this to see if we can identify longer-term changes in oceanography that are not obvious except to those who experienced the changes first-hand. I'm also trying to understand whether an NLP-based approach can generate any additional insight for a very quantiative environmental science.

Comments on this series are welcome: you can tweet me [@braaannigan](https://twitter.com/braaannigan). Thank you to Baylor Fox-Kemper for some comments on an early version.

The data I use are the titles and abstracts from every issue of JPO along with year of publication.
This gives almost 7800 articles. Once I exclude articles that are replies, editorials, comments etc. or are simply missing their
abstract I have a final dataset of 7400 articles. As I am focusing on text I do not use other data such as authors, affiliations or citations. This may be worth coming back to later on.

I have limited the text analysis to title and abstract as these reflect what the authors think are the essence of the article. I'm  splitting the analysis into a number of posts that can be thought of as *where*, *what*, *why* and *how*. 

[Part II (Where research is carried out) is here.](https://braaannigan.github.io/oceanography,/nlp/2021/01/10/jpo-where.html)

In this introductory post I look at some overall patterns in the publication patterns. I show how the number of articles grew rapidly - but only for a while - and how titles have experienced constant expansion while abstracts have been brought under control. Finally, I set the scene for the following posts by showing some of the common terms that have come in and out of fashion over the decades.

# Methods

To identify topics I simply look for the presence of key words that I know are related to this topic. I allow for synomyns e.g. conductivity-temperature-depth and CTD, acronyms and hierarchichal references - for example when tracking references to the Atlantic I include references to the Sargasso Sea.  The method isn't perfect of course - an article that mentions the presence of North Atlantic Deep Water in the Southern Ocean will be labelled as both Atlantic and Southern Ocean, but inspection of the results shows that the overall picture presented by this method is reasonable.

## Number of articles
The number of articles in JPO has increased over time. However, while I expected a more or less continual, gradual growth in the number of articles the reality has been quite different. There was a period of exponential growth in the first decade which saw the number of articles published increase from 40 in 1971 to 170 in 1980. Since then the number of articles has oscilliated from a nadir of 114 articles in 1992 to a zenith of 228 articles in 2001.
![Number of articles per year](/img/totalArticles.svg)

The increase in the number of articles published is due to an increase in the number of issues per year and the number of
articles per issue. In recent years there has generally been about 15 articles across 12 issues. In contrast, in 1972 there were just 4 issues and the first issue had just a single article ("A Study of the Bottom Boundary Layer of the Florida Current").


## Length of titles
![Length of articles' titles](/img/titleLength.svg)

If we are looking for near-perpetual growth in oceanography the place to look is the length of article titles. These titles have seen growth from a pithy average of 62 characters in 1971 to 88 characters in 2020 or about 1 character every 2 years. These longer titles are mainly due to more words in titles, but there has also been a small increase in the mean length of words in titles.

The longest title at 224 characters / 27 words is from a 2015 article: "Freshwater Flux and Spatiotemporal Simulated Runoff Variability into Ilulissat Icefjord, West Greenland, Linked to Salinity and Temperature Observations near Tidewater Glacier Margins Obtained Using Instrumented Ringed Seals". This title captures a few of the trends that have lengthened titles: greater
specificity in topic of study, location and methods along with more hints at the results.

An inspection of the shortest titles shows that longer titles are to some extent an inevitable consequence of the increasing specialisation of a subject area. For example, it would be impossible to call an article something as simple as "The Instability of a Baroclinic Vortex" if working in the same domain today. The shortest article title of all is 1975's very straightforward "MODE tides".

## Length of abstracts
![Length of articles' abstracts](/img/abstractLength.svg)

Given in the increasing length of titles I expected abstracts to grow in a similar way. However, abstracts instead grew rapidly from around 750 characters / 180 words in the early years to double this length by the early 2000s with a peak of 1556 characters / 300 words in 2000 (left plot). A steadying hand by the editors since then has led to a contration in abstract length by 10% to around 1400 characters/250 words in the most recent decade. 

We can understand why the abstracts are curtailed by looking at the distribution of the number of words in the abstract (right plot). The blue box shows the limits of the first and third quartiles, the vertical lines show the 95% range and the dots shows values outside the 95% range. The blue boxes show how all abstracts generally got longer from the early 1970s until around 2000. An abstract that would have been relatively long in the early 1970s would have been relatively short by the 1990s. The increase in mean length was also driven by the emergence of very extremely long (400 word+) abstracts. In the 2000s it is clear that the journal started trying to limit abstract length as the very long abstracts disappeared. In the most recent decade a hard limit on abstract length has been imposed with very few articles having an abstract longer than 300 words. 

The longest abstract was found in the 1980 article "A Numerical Study of Loop Current Intrusions and Eddy Shedding" and came in at an awesome length of 728 words. Inspection of the titles for the longest abstracts shows no particular pattern in terms of the study material: observational, numerical and theoretical studies are found while the study material is similarly varied including large-scale circulation, surface wave dynamics and turbulent dynamics.

One feature that has almost disappeared in recent years is the 'tweetable' abstract - that is an abstract of less than 280 characters. Consider this example from 1992 "The rapid changes in density observed near the continental slope in association with internal waves are explained as nonlinear features of wave reflection". In this case the abstract was just twice the length of the title.  Until 2000 there were at least a few of these short abstracts every year but in recent years even the shortest
abstracts have had more than 700 characters or 200 words.

# Emergent terms
We can get a quick sense of how the field has varied over the decades by looking at some common terms that were much more popular in one period than in others. For simplicity we divide the 50 years into 3 periods (1971-1987,1988-2004 and 2005-2020). The table below shows 1, 2- and 3- word phrases that were in much higher usage in one of these periods compared to the other two.

Period | Geographic | Methods | Topics |
 --- | --- | --- | --- | --- |
1971-1987 | North Pacific, Gulf Stream, Sargasso Sea, Lake Ontario | Bathythermograph | Coastal upwelling, Continential shelf slope/waves, Kelvin Waves, Gravity waves, Vertical Eddy Viscosity, Double Diffusive Convection
1988-2004 | Tropical Pacific, Western Pacific, South Atlantic | Topex-Poseidon, Acoustic Doppler Current Profiler, General circulation models, Primitive Equation Models, Reduced gravity model | Deep western bounary currents, Deep convection, Potential vorticity, , Boundary current Separation
2005-2020 | Global ocean, Arctic Ocean, Southern Ocean, South China Sea, Antarctic Circumpolar Current, Kuroshio extension, Loop Current | Large eddy simulations, ARGO | Submesoscale, Sea surface height, Linear stability, Monentum fluxes, Energy budget, Eddy-permitting, Interannual variability, Eddy fluxes, Overturning circulation, Diapycnal mixing,Internal tides, Inertial Waves, Turbulent Dissipation

The following posts will examine these trends in more detail.
