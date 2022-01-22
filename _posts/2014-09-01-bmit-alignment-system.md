---
title: Robotic Alignment & Visualization System
date: 2014-09-01 14:00:00 -0800 #-0800 = pst time
categories: [Projects, Canadian Light Source]
tags: [cad, coding]     # TAG names should always be lowercase
thumbnail: /files/images/bmit-alignment-thumbnail.png
---

This project consisted of an alignment and visualization system for a series of industrial robots in the [BMIT beamline](https://bmit.lightsource.ca/) at the Canadian Light Source. It was featured in the [AIP Conference Proceedings 1741](https://aip.scitation.org/doi/abs/10.1063/1.4952846) in 2016.

## Background

Aligning samples at BMIT has always been a problem. The invisible X-ray enters the experimental room at an angle defined by it's energy. At least 3 different systems need to be robotically aligned to the beam with high precision: the entrance shutter, the sample positioner, and the camera positioner. To further complicate things, the sample needs to be aligned with it's rotary axis highly perpendicular to the X-ray (within 1 pixel of the camera). The sample positioner is based off a [kappa goniometer](https://www.researchgate.net/figure/Schematic-kappa-goniometer-1-2-goniometer-2-3-r-block-3-axis-block-4-sample_fig1_244635210) which also has complex kinematics.

To simplify this alignment process, it was desired to develop a visualization system and implement kinematics to calculate alignment geometries.

{% capture imagePath %}/files/images{% endcapture %}

![05ID-2 experiment room]({{ imagePath }}/bmit-alignment-experiment-room.jpg){: width="1000"} 
_The BMIT 05ID-2 experiment room. The X-ray travels from right to left._

## Implementation

A detailed SolidWorks model was first put together of all key system components. Global variables in the SolidWorks model were then linked to all aspects of it we would want to control, including robotic axes, beam size, sample size, etc.

![System Rendering]({{ imagePath }}/bmit-alignment-full-render.png){: width="500"} 
_CAD model of the system. The x-ray is shown in red. The beam angle is determined in the round vacuum chamber in the bottom right._

Software was then written to automatically adjust these model variables using the SolidWorks VB.net API. This software also included functions to adjust the model view, rotation, zoom, etc. and export images of the model as well as various geometry measurement functions. A TCP server was then added to the software, allowing it to receive commands from any computer on the network and return images of the model. The software was designed so it could open multiple instances of SolidWorks in the background, allowing multiple computers to connect and adjust different configurations of the model.

The final aspect of this project was to develop inverse kinematic equations for the kappa goniometer, allowing us to align it based on beam geometry. These equations were built into a python package by one of the control systems engineers, allowing it to calculate desired system geometries, adjust the SolidWorks model remotely over TCP, then return images of the configuration.

![Sample render]({{ imagePath }}/bmit-alignment-sample-render.jpg){: width="500"} 
_An example image output from the server. Sample alignment geometries can be complex._

## Project Poster

Below is a posted about this project. It is also available in [pdf format](/files/project_pdfs/bmit-alignment-experiment-poster.pdf).

![Project Poster]({{ imagePath }}/bmit-alignment-experiment-poster.jpg){: width="1400"} 
_Download for higher resolution_