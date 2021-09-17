---
layout: post
title:  "What software skills do oceanographers want to learn"
date:   2021-09-15 10:35:24 +0200
categories: software
---
# tl:dr
A small survey of oceanographers shows there is high demand for training to improve their software engineering skills. The range of topics is broad ranging from basic programming to advanced machine learning and visualisation. Overall we can see that oceanographers want training to be able to produce analysis that is more reproducible, scales to large datasets and allows them to test hypotheses more efficiently.

# Aim of the survey
The survey was developed by Gwyn Evans and Liam Brannigan. We want to develop a workshop to help researchers learn better software engineering skills. Before doing so we wanted to ask the researchers what they want to learn.

The survey is by no means comprehensive but provides a useful snapshot of the topics researchers are interested in at the moment. The survey was carried out using the Tricider tool. We provided some initial topics that researchers could vote on while allowing them to add their own. As respondents could add their own topics there is some overlap between the topics.

There are some obvious omissions - we focused on tools in the python ecosystem as that is how we carry out the bulk of our analysis. We also included some more generic tools that are not python-based such as version control using git.

# Survey population

The survey was open to researchers at the National Oceanography Centres in Southampton and Liverpool. The survey was initially posted only to the physical oceanography group and the bulk of respondents work in that area.

# Survey results

The survey results can be seen below. We have grouped the responses into a number of high-level categories
and coloured each bar by its category.
![Survey results](/img/noc_survey_results.svg)

The top 2 categories are relate to different aspects of basic programming. Some respondents said they are particularly interested in support for those who have or would like to transfer from matlab to python. Another respondent said they would also like support for using a linux operating system effectively.

Using version control with git was the next most popular topic. Respondents said they would like to understand how to use git workflows in their research and to make their code publically available on a site like Github.

The next topics are training in the use of the popular Xarray package and carrying out parallel processing in python. These topics are closely related as the Xarray package has built-in support for parallel processing and has become one of the main ways that physical oceanograhers scale their analysis code to run in parallel. 

Visualisation and interactive development tools were also popular topics. Respondents mentioned the value they could get from a better understanding of 2D and 3D plotting tools. Researchers increasingly use browser-based interactive development tools to generate their visualisations such as jupyter notebooks. These kinds of interactive tools were referred to in multiple topics.

The next topics raised related to workflows that allow for collaboration and reproducibility. Among the topics here were 
- use of Docker containers for analysis
- virtual environments to isolate projects
- setting up project directories to make use of Docker or virtual environments more effective

The remaining topic raised was training in python's primary machine learning library. While this topic gathered just a single vote in this survey it seems unlikely that this low support reflects a paucity of demand for this kind of training. Instead we think that respondents were more focused on more fundamental aspects in this survey.