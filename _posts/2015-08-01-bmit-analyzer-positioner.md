---
title: X-Ray Analyzer Positioner
date: 2015-08-01 14:00:00 -0800 #-0800 = pst time
categories: [Projects, Canadian Light Source]
tags: [design, cad]     # TAG names should always be lowercase
thumbnail: /files/images/bmit-analyzer-thumbnail.jpg
---

This project consisted of designing, prototyping, and implementing a 3 axis positioner for a silicon diffraction crystal in the [BMIT beamline](https://bmit.lightsource.ca/) at the Canadian Light Source.

## Background

[Diffraction enhanced imaging](https://spie.org/news/dei-imaging-sharpens-x-ray-radiography?SSO=1) is an X-ray imaging technique where a silicon crystal with a particular lattice structure called an analyzer crystal is placed between the sample and camera. The X-ray diffracts through the crystal lattice structure as defined by [Bragg's Law](https://en.wikipedia.org/wiki/Bragg%27s_law). Slight changes in the angle of the analyzer significantly effect the contrast of the image, allowing much higher contrast than normally achievable.

We had a set of [PI Nexline Actuators](https://www.pi-usa.us/en/products/piezo-motors-stages-actuators/linear-piezo-motors-actuators-for-integration/n-216-nexline-linear-actuator-1000765/) sitting around, and thought they would be a good use for building an analyzer positioner due to their extremely small minimum incremental move capability. 

{% capture imagePath %}/files/images{% endcapture %}

## Design

Overall the design is pretty straightforward. Two flat plates, the moveable one mounted on kinematic compoments. Cone/vee/plane kinematic elements were chosen instead of the typical 3 vee configuration to simplify things by having a defined point of rotation about the cone. The kinematic contacts were preloaded with springs. 

<div class="container">
  <div class="row">
    <div class="col">
      <img src='{{ imagePath }}/bmit-analyzer-render-cutaway.jpg' alt='analyzer-render-cutaway' width="400px" />
    </div>
    <div class="col">
      <img src='{{ imagePath }}/bmit-analyzer-render.jpg' alt='analyzer-render' width="400px" />
    </div>
  </div>
  <em>
    Renders of a cutaway initial design showing the cone interface and the final design
   </em>
</div>

A pair of sheet metal springs was originally designed to hold in the crystal without deforming it. This was later swapped for dimpled washers as we could make them easily.

## Assembly

A proof of concept prototype was built from a pair of acrylic plates prior to ordering machined parts. It worked great! Repeatability was somewhat verified with a laser pointer and a long hallway. 

![Analyzer Prototype]({{ imagePath }}/bmit-analyzer-prototype.jpg){: width="500"} 
_The analyzer positioner proof of concept_

The final machined version also went together surprisingly well. Extreme care had to be taken because the silicon crystals are fragile and nearly priceless. 

![Analyzer Final Assembly]({{ imagePath }}/bmit-analyzer-final-assembly.jpg){: width="500"} 
_The final analyzer positioner prior to installing in the beamline_

## Installation

Installation was also a very delicate procedure because the whole assembly needed to be inverted. There was a moment of truth seeing if the springs were strong enough to keep the kinematic elements preloaded with the weight of the crystal.

![Analyzer Installed]({{ imagePath }}/bmit-analyzer-installed.jpg){: width="800"} 
_The analyzer positioner installed in the beamline_

It worked! The system actually worked very well due to the fine resolution and high repeatability of the piezo actuators. Stability of the system was also excellent; the beam would still be aligned after leaving it for 24 hours.

![Analyzer Testing]({{ imagePath }}/bmit-analyzer-testing.jpg){: width="800"} 
_The first time we got the beam aligned. You can see how the aluminum parts block the X-ray._