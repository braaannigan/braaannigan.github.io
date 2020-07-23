---
layout: post
title:  "Career progression"
date:   2020-06-26 10:35:24 +0200
categories: career
---

In the last two years I've made a transition from research scientist in physical oceanography to data scientist in industry. I discussed this recently participated in a panel run by the Euro Geosciences Union and thought that I should share the joys of this transition and lessons learnt in more detail. 

I joined Analytics Engines in April 2018 after being put in touch by a recruiter.  The process was very fast compared to the timescales of academic fellowship applications - from a chat with an interviewer through two interviews and a job offer in 4 days.  I started 2 weeks later.

In some ways I took on a risky position was the most risky to take - to be the first data scientist at a company. Many have found out the perils of this position - you arrive to find that there is little quality data and spend most of your time trying just to organise it rather than generating useful insights.  In this case the risk was a little lower as I was surrounded by experienced front- and back- end software engineers who were experts in setting up databases and building visualisations. 

**Lesson number 1** Don't be the first data scientist in an organisation that doesn't have data engineering infrastructure. You'll end up being given a million spreadsheets that are the data equivalent of reading a book that's been shredded.

I had done some machine learning in my postdoc where I looked at Bayesian time series forecasting. I soon realised that this would be of limited use. This limited utility is because it is much harder to come across time series data that is stable enough to provide useful insights outside of research. For example, in one project we had decades of reports on food fraud. However, the pattern of such fraud is that when it is detected the fraudsters jump to a new area - and there are many to choose from. This means that the level of fraud stays roughly constant in time, but the type of fraud varies in a very unpredictable way.

**Lesson number 2** Be prepared to meet much more messy data than you might be used to as a researcher.

I started to make some headway in this area by analyzing text data (i.e. NLP) related to news stories. Few climate scientists work with text data but in the private and public sector it is ubiquitous.  The challenge was that I knew I was ignorant of how to go about text analysis, but as the only data scientist I didn't have a more experienced colleague to turn to.  Instead I dived into NLP twitter and followed everyone who put out interesting stuff.  After a few months of reading blog posts, watching lectures and trying tutorials I started to get a grip on the current methods and was starting to do interesting stuff by myself. One advantage of getting into machine learning at the moment is that revolutions come so quick and fast that you can often get up to speed much faster than in a scientific discipline that has been maturing for decades.

**Lesson number 3** Progress in data science in recent years is much faster than in most modern branches of science so you have to invest time continuously to keep up.

As well as tools moving fast projects move fast as well. Whereas I worked on 2 or 3 different projects during my postdoc I might be working on 2 or 3 different projects in a month. In addition these projects can be highly diverse - at one point I was simultaneously working on analysis of protein sequences, spatial patterns of illegal dumping and mapping building usage. This places an emphasis on being able to get up to speed fast while trying to tap your domain expert partner for their knowledge as much as possible.

**Lesson number 4** You may have to be comfortable making good enough progress across a range of problems rather than seeking perfection in a particular niche.

Some patterns of working with new tools and methods were very familiar to me from my research days. I knew not to be too surpised when things like 'much hyped new tool doesn't actually improve performance on your data' cropped up. Or when a new tool that promised to give you a massive performance acceleration turned out to actually slow things down.

Once I had fit my first models to actual client data with good results I thought I'd finally made it.  This was wrong. Because, in order for your models to be of any use to anyone they have to be deployed into production. This means that you have to package your model in such a way that it can keep working regardless of what happens. At large companies there are dedicated professionals who do this as their full-time job. At start-ups, on the other hand, you do this yourself. The challenges of this were many: you will have to build your model into a docker container (eventually you'll learn to do this from the start); you might have to build a serverless function in the cloud that can run your model (make sure you've got all your permissions and credentials files in the right place); you might have to synchronize your data with a database; you have to monitor your model's performance so that you know if it starts going crazy; you might have to build an app that serves your model once it's in the cloud; you might have to quantize your model so that it can run in a lambda function and so on and so on. In comparison to the multitude of blog posts out there that show you how to fit a model in scikit learn or PyTorch there are very few posts out there that cover these much trickier issues.

**Lesson number 5** There's a lot more to data science than fitting models. Try to deploy a very simple app to the cloud if you want to learn more. 

One major point to be aware of is that all od this is based on my experience in a particular type of company. In other companies there may be much more pressure to work longer hours or travel extensively. Overall, I'd say that you have less idea what working conditions to expect starting at a new company compared to starting at a new lab, even if it was in a different country.

Overall, I'm very happy with the change I've made. I have a good work-life balance that has allowed me to meet the many challenges of having a young family.  In addition, my work at Analytics Engines has been every bit as intellectually stimulating as my research. Obviously, the change has meant that I haven't been able to focus on the environmental problems we face - though I have still had opportunities to work on environmental challenges - but I'm confident that the new set of skills I've picked up will allow me to make a fresh contribution in time.

