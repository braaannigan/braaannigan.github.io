---
layout: post
title:  "Attaining flow while writing software"
date:   2022-01-02 10:35:24 +0200
categories: software
---
# Attaining flow while writing software

## tl:dr
I have broken my former cycles of anxiety, frustration and elation when writing software by adopting proven principles of
software engineering. By adopting these principles, I more frequently attain a state of *flow* where I am highly focused but calm and produce effective software.

If you're interested in learning how to apply these principles across your organisation then 
<a href="mailto:braaannigan@protonmail.com">get in touch</a> as I am developing workshops to spread the word.

## Writing software: it's all about emotions
I spent the bulk of my phd writing software to analyse the output of numerical models of the ocean. When I think back to my day-to-day experience during this period what strikes me is how emotionally demanding it was. Over the 4 years my scripts became ever more complex and capable, but the stress and strain of maintaining, developing and running this code grew in the same way.

There were clear emotional cycles to this process. Firstly I would have a new idea that required a modification to my working code base. This caused stress - what if the change didn't work and I couldn't revert back to my working code?
Before any of you version control experts start making any comments, you should know that I did have a powerful system of saving my working file as `pipeline_working_version.m` before making changes. The problem was that I was normally so excited about my great new idea that I had already made a bunch of changes before remembering to do that.
 Then there was the process of actually making the change - adding a new feature often led to the frustration of something else breaking. 

As time went on there was an additional factor - the size of the datasets I was working with kept increasing. These larger datasets meant it was taking longer and longer to figure out if the code was working at all. If the code wasn't working the larger datasets also meant that it was taking longer and longer to understand the bugs.

For each new idea there were ultimately two outcomes. On the one hand a retreat from the new idea if the whole process couldn't be endured anymore leading to a wave of relief or - sometimes - the elation of a working codebase with a nice new feature.

## Going with the flow
My experience in recent projects has been quite different. Once I've gone through the messy early stage and figured out what I'm trying to do I've then often had some coding sessions where I've made rapid progress. The code written in these sessions forms the long-term backbone of the project. Once the project is established there comes a point where I realise I made a dumb assumption in my early plan. I then need to do some re-factoring of the code code to accommodate this. This refactoring has also been carried out in an orderly fashion.

My emotional experience in these projects has been quite different. There have been few major emotional cycles where the computer is coming close to a trip out the window. Instead there have been regular coding sessions where I was in a state of flow while making regular progress. Defining flow is subjective, but my experience was of feeling highly focused, but also calm without major tension or anxiety.  On the flip side I rarely end up with the big highs where I want to run to the next office and force someone to feign interest in what I've done - instead elation is replaced by something more like satisfaction.

## What's changed?
I've been trying to understand the reasons for this change to help me share the lessons with others.  A first guess would be that it reflects my greater experience. With the extra years I've been able to make the proverbial 10,000 mistakes (10,000 times each of course). But I don't think this is really the core of it. Instead, I've either consciously or unconsciously re-discovered the proven principles of sound software engineering. 

Before delving into the details of the approach it's worth reflecting on what drove the emotions in my old approach. Firstly, there was low-level anxiety when changing the code that the new feature would break the current working code and it would be difficult to revert any new changes. Linked to this anxiety was mental strain when adding a new feature as it would be up to me to remember how the entire code base worked to avoid breaking existing functionality. Then there was frustration when adding a new feature that inevitably caused existing functionality to break because who can remember how all of a complex code base works! The debugging process would be frustrating as it could take a long time (minutes, hours, days) to run the code to the point where the failure occured to understand if the problem was fixed.

One point that comes through is how much mental load I placed on myself to retain all of the functionality in my head. Many of the techniques I've learned are really about taking the mental pressure off by letting the computer take on the role of remembering all the details. As the programmer I can instead use my mental space for thinking about what I'm trying to achieve. 

As a corallary, this unloading of the mental burden is even more important if you've got other big things in your life going on. For example, anyone with a new child suffering from serial sleep deprivation doesn't need to be burdened with memorising an entire code base!

## Proven principles of sound software engineering
Just as a cooking blog must eventually move on from the tale of how grandma learned the casserole recipe to actually giving the recipe, so must I share the principles I've been going on about:
- Use version control with git to keep track of your changes and allow you to create branches to develop new features
- Learn how to use a debugger and set breakpoints in your code
- Develop unit tests for all your code so the computer remembers what each function needs to do and automatically checks that your changes don't break existing functionality
- Create small test datasets that you can use to run end-to-end pipelines to ensure you are still outputting what you need to. Don't run on your full dataset unless you are highly confident it will succeed. If you find a problem, drop back down to the smallest dataset until you're sure the problem is fixed.
- Declare all of the infrastructure needed to run your code explicitly - for example a `requirements.txt` file setting out all third-party libraries or (even better) a `Dockerfile` setting out any other non-python dependencies such as compilers.


