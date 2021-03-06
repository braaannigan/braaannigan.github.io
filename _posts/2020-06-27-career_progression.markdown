---
layout: post
title:  "Career progression"
date:   2020-06-26 10:35:24 +0200
categories: career
---
# Career progression - lessons learned

In the last two years I've changed from being a research scientist in physical oceanography to data scientist in industry with Analytics Engines. I discussed this change recently in a [panel run by the European Geosciences Union](https://www.youtube.com/watch?v=iBM1YG4VbqM&t=118s) and thought that I should share the joys of this transition and lessons learnt in more detail. 

I joined Analytics Engines in April 2018 after being put in touch by a recruiter.  The process was very fast compared to the timescales of academic fellowship applications - from a chat through two interviews and a job offer in 4 days.  I started 2 weeks later.

## Taking a job offer

In some ways I took on a risky position - to be the first data scientist at a company. Many have found out the perils of this position - you arrive to find that there is little quality data and spend most of your time trying just to organise it rather than generating useful insights.  In the case of [Analytics Engines](https://www.analyticsengines.com) the risk was lower as I was surrounded by experienced data engineers who were experts in setting up databases and building visualisations. 

**Lesson number 1** Don't be the first data scientist in an organisation that doesn't have data engineering infrastructure. You'll end up being given a million spreadsheets that are the data equivalent of reading a book that's been shredded.

## Machine learning IRL

I had done some machine learning in my postdoc where I looked at Bayesian time series forecasting. I soon realised that this experience would be of limited use because in most organisations it is much harder to find time series data that is stable enough to provide useful insights outside of research. For example, in one project we had decades of reports on food fraud. However, the pattern of such fraud is that when it is detected the fraudsters jump to a new area - and there are many to choose from. This means that the level of fraud stays roughly constant in time, but the type of fraud varies in a very unpredictable way. 

**Lesson number 2** Be prepared to meet much more messy data than you might be used to as a researcher.

## Building and maintaining machine learning knowledge

I started to make some headway in this area by analyzing text data (i.e. NLP) related to news stories. Few climate scientists work with text data but in the private and public sector it is ubiquitous.  The challenge was that I knew I was ignorant of how to go about text analysis, but as the only data scientist I didn't have a more experienced colleague to turn to.  Instead I dived into NLP twitter and followed everyone who put out interesting stuff.  After a few months of reading blog posts, watching lectures and trying tutorials I started to get a grip on the current methods and was starting to do interesting stuff by myself. One advantage of getting into machine learning at the moment is that revolutions come so quick and fast that you can often get up to speed much faster than in a scientific discipline that has been maturing for decades.

**Lesson number 3** Progress in data science in recent years is much faster than in most modern branches of science so you have to invest time continuously to keep up.

## A new postdoc every month

As well as tools moving fast projects move fast as well. Whereas I worked on 2 or 3 different projects during my postdoc I might be working on a different project every month. In addition these projects can be highly diverse - at one point I was simultaneously working on analysis of protein sequences, spatial patterns of illegal dumping and analyzing text. This places an emphasis on being able to get up to speed fast while trying to tap your domain expert partners for their knowledge as much as possible.

**Lesson number 4** You may have to be comfortable making good enough progress across a range of problems rather than seeking perfection in a particular niche.

## It's all about production

Once I had fit my first models to actual client data with good results I thought I'd finally made it.  This was wrong. In order for your models to be of any use they have to be deployed into production. This means that you have to package your model in such a way that it can keep working regardless of what comes at it. At large companies there are dedicated professionals who do this as their full-time job. At start-ups you learn to do this yourself. The challenges of this move to production are manifold. In comparison to the multitude of blog posts out there that show you how to fit a model in scikit learn or PyTorch there are very few posts out there that cover these much trickier issues of deployment. 

**Lesson number 5** There's a lot more to data science than fitting models. Try to deploy a very simple app to the cloud if you want to learn more. 

## Every company is different

One major point to be aware of is that all of this is based on my experience in one company. In other companies there may be much more pressure to work longer hours or travel extensively. Overall, I'd say that you have less idea what working conditions to expect starting at a new company compared to starting at a new lab as a postdoc.

Overall, I'm very happy with the change I've made. I have a good work-life balance that has allowed me to work hard while meeting the many challenges of having a young family.  In addition, my work at Analytics Engines has been every bit as intellectually stimulating as my research. Obviously, the change has meant that I haven't been able to focus on the environmental problems I care about but I'm confident that the new set of skills I've picked up will allow me to make a fresh contribution in time.

Thanks to Gwyn Evans (@https://twitter.com/D_GwynEvans) for comments!

