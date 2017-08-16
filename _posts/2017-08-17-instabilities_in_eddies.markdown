---
layout: post
title:  "Submesoscale instabilities in mesoscale eddies"
date:   2017-08-16 16:35:24 +0200
categories: research
---

<h2>
<a id="authors-and-contributors" class="anchor" href="#authors-and-contributors" aria-hidden="true"><span aria-hidden="true" class="octicon octicon-link"></span></a>Submesoscale instabilities in mesoscale eddies</h2>

<h3>
<a id="authors-and-contributors" class="anchor" href="#authors-and-contributors" aria-hidden="true"><span aria-hidden="true" class="octicon octicon-link"></span></a>What is symmetric instability?</h3>
<p>If you aren't familiar with symmetric instability, I describe the basic dynamics in my seminars.  The video below shows an excerpt from an early talk I gave on these results at IMEDEA on Mallorca in Spain in March 2015.<p>
<iframe width="560" height="315" src= "" data-src="https://www.youtube.com/embed/L4cYnVW2dFE?start=685" frameborder="0" allowfullscreen></iframe>
<p> A wonderfully clear explanation of the connection between symmetric instability and potential vorticity is given in this classic note: <a href="http://www.readcube.com/articles/10.1002%2Fqj.49710042520" target="_blank">Hoskins (1974)</a> </p>

<h3>
<a id="authors-and-contributors" class="anchor" href="#authors-and-contributors" aria-hidden="true"><span aria-hidden="true" class="octicon octicon-link"></span></a>Physics of the instability</h3>

<p>Idealised simulations of an eddying domain using the MITgcm show that submesoscale filaments emerge inside mesoscale (diameter 80 km) eddies under wind forcing.  These filaments occur in regions of negative potential vorticity. The filament growth is driven by vertical buoyancy fluxes and vertical shear production.  The filaments grow with a large cross-front wavenumber.  For these reasons it was concluded that the filament growth is driven by symmetric instability inside the mesoscale eddies.  These results are set out in this <a href="http://onlinelibrary.wiley.com/doi/10.1002/2016GL067926/full" target="_blank">GRL</a> paper</p>

<p>The instability leads to the upwelling of high potential vorticity fluid into the mixed layer of the anticyclone.  The upwelling occurs in long filaments with a wavenumber oriented in the cross-front direction - or in other words the filaments are banded in the radial direction of the eddy.  The emergence of the filaments can be seen by taking a coarse resolution simulation at 4 km resolution and interpolating it to a submesoscale-permitting resolution of 0.25 km.  The animation below shows the potential vorticity at the base of the mixed layer of the anticyclone in the simulation spun-up at 4 km resolution but run at 0.25 km resolution.</p>
<iframe src= "" data-src="https://player.vimeo.com/video/161776646?loop=1" width="600" height="509" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe>


<h3>
<a id="authors-and-contributors" class="anchor" href="#authors-and-contributors" aria-hidden="true"><span aria-hidden="true" class="octicon octicon-link"></span></a>Biogeochemical relevance?</h3>
<p>Symmetric instability at fronts and in eddies may have important characteristics for biogeochemical tracers such as the nutrients needed for ocean plants to grow.  When symmetric instability develops in a region of negative potential vorticity, stability is not restored unless the negative potential vorticity fluid can be mixed with positive potential vorticity fluid.  The thermocline below the base of the mixed layer can be an important source of positive potential vorticity water in this case.  This thermocline fluid may also have higher nutrient concentrations that the fluid in the mixed layer.  As such, the transport of high potential vorticity water across the base of the mixed layer by symmetric instability may also bring water with high nutrient concentrations into the light-rich mixed layer.<p>

The animation below shows a vertical section through a mesoscale anticyclone in a limiting nutrient experiment.  The green colour show the concentration of the limiting nutrient.  Solid black lines are isopycnal surfaces.  The dashed black line is the mixing layer depth, as set by the KPP mixing scheme.  Time in the simulations is shown in days in the lower left-hand corner. When the simulation starts, the instability begins to grow in the mixed layer.  After a few days the instability penetrates deeper into the thermocline and starts to transport the high nutrient water towards the mixed layer.  The nutrient transport occurs in submesoscale filaments that are being wrapped around the eddy.  Once the high nutrient fluid reaches the dashed black line, the high vertical diffusion in the mixed layer takes over and spreads the nutrient vertically.
<iframe src= "" data-src="https://player.vimeo.com/video/159205818" width="600" height="360" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe>
<p>The movie can be found on my vimeo account <a href="https://vimeo.com/159205818" target="_blank">here</a></p>



<script>
function init() {
var vidDefer = document.getElementsByTagName('iframe');
for (var i=0; i<vidDefer.length; i++) {
if(vidDefer[i].getAttribute('data-src')) {
vidDefer[i].setAttribute('src',vidDefer[i].getAttribute('data-src'));
} } }
window.onload = init;
</script>
