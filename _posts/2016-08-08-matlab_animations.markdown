---
layout: post
title:  "Easy animations in matlab"
date:   2016-08-08 16:35:24 +0200
categories: visualisation
---
<script type="text/javascript" async
  src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-MML-AM_CHTML">
</script>

### Flow animations - don't you just love them?
I love animations of fluid dynamics.  We are lucky to work in a field that
lends itself so readily to visualisation, where models produce outputs that
people can just look at to get an idea of what's going on. Animations are
also great for capturing peoples' attention when presenting your work
in person - particularly the tired, jet-lagged
and possibly hungover population of most major scientific meetings.

### Getting the right size
Producing publication-quality animations in two dimensions is straight-forward
in matlab.  Once you know what you're doing -- as you soon will -- it's just
a few lines of code that you add to the start and end of a loop.  Indeed, the
issue isn't really producing publication-quality animations --- it's producing
publication-quality animations with a filesize that a publisher will actually
accept.  In my experience, naive use of the matlab writer commands produces
files that are about 50 times larger.

Sample code for generating an animation is below.  The animation is of a domain
with 50x50 pixels and 120 frames.  It comes out as an .avu file of less than 4 MB.

First generate the data to be plotted

$$x = \textrm{linspace}(0,2*\pi,50)$$;

$$y = x$$;

$$t = \textrm{linspace}(0,12*\pi,120)$$;

$$[X,Y] = \textrm{meshgrid}(x,y)$$;

for $$k = 1$$:length($$t$$)

$$z(:,:,k) = \textrm{cos}(X+t(k)).*\textrm{cos}(Y)$$;

end

%Then open the video object and run the plot loop

vid = VideoWriter('anim_name'); %Create video object and set output name

vid.Quality = 70; %Runs from 0 (lowest quality) to 100 (highest quality)

vid.FrameRate = 8; %Set the frame rate per second

open(vid); %Open the animation object

h=figure(1);clf %Open the figure window

pause %Pause to open the figure window full-screen if necessary

for $$k = 1$$:length($$t$$)

figure(1);clf

pcolor(x,y,z(:,:,k))

shading flat

caxis([-1 1])

title(t(k)/t(end))

%pause(1e-1) %The pause command doesn't effect the frame rate

writeVideo(vid, getframe(h,[80 50 1400 1010]));

%Write the current frame to the animation file.  The 4-element vector
%at the end sets the boundaries of the box that will be captured in
%the animation.  The units are in pixels and are in the standard
%matlab format [left-hand-boundary lower-boundary width height].

end

close(vid) %Close the video.

The output can be seen here:
<iframe src="https://player.vimeo.com/video/179024540" width="640" height="462" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe> <p><a href="https://vimeo.com/179024540">Easy animation with matlab</a> from <a href="https://vimeo.com/user50105397">Liam Brannigan</a> on <a href="https://vimeo.com">Vimeo</a>.</p>
