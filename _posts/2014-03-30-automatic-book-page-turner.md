---
title: Automatic Book Page Turner
date: 2014-03-30 14:00:00 -0800 #-0800 = pst time
categories: [Projects, School]
tags: [design, cad, laser cutter]     # TAG names should always be lowercase
---

## Background

The automatic page turner was created as part of a 2nd year Engineering design class at the U of S. The goal was to create a device for a disabled lady to automatically turn the pages of a book at the click of a button. Ideally it would work with as many sizes of books as possible. How hard could it be?

## Constraints

There were a few major constraints with this project:
- Only allowed the use of 1 geared DC motor powered by a 9V battery. The motor rotates 1 revolution per click of a button. Thankfully it was reasonably torquey with the gearbox.
- Only allowed the use basic hand tools with the exception of a CNC laser cutter.
- Only allowed basic materials (wood sheet, acrylic sheet, threaded rod, etc.). Each material had a cost associated with it.

## Design

The basic design consists of three elements:
1. A pair of rotating wheels to lift the page a bit.
1. A pair of rotating fans to grab the lifted page and flip it over.
1. A spring-loaded hinged backing plate to push the book towards the wheels.

The rear fan could be slid forwards or backwards on a keyed shaft to accomodate different sized books.

![CAD rendering](https://live.staticflickr.com/1493/23502546754_6bb89c4d85_b.jpg){: width="600"} 
_A CAD rendering of the page turner design_

There is an obvious problem with this design. A continuously rotating motor needs to perform two different functions, one after the other. One method to to turn continuous rotation into intermittent rotation is with a [geneva drive](https://en.wikipedia.org/wiki/Geneva_drive). More importantly, the geneva drive can be mirrored to create two separate intermittent rotations (forming the Graham drive). Hilariously this is probably the first ever practical usage of the geneva drive, and I've never found a reference to the mirrored dual rotation design. Clearly we should have patented it.

![Geneva Mechanism](https://upload.wikimedia.org/wikipedia/commons/9/9b/Geneva_mechanism_6spoke_animation.gif){: width="400"} 
_Geneva Drive Animation_

## Build

The build actually went remarkably well. The centralized "gearbox" was modular from the rest of the device and was easy to install and remove when things needed tweaking.

We had quite a few issues with the right angle gears for the fans. It's tough to make these properly with a laser cutter. Our design used gears made with pins projecting from a laser cut piece of wood. It was tough to transmit much torque without jamming.

![Page Turner](https://live.staticflickr.com/1687/24104682816_8209bff8ba_b.jpg){: width="600"} 
_The page turner part way through construction_

## Results

The results weren't nearly as impressive as the build. As usual we were super rushed towards the end of the project and didn't have much time to tweak things. We managed to turn a few pages on ideally sized books, and also managed to rip a bunch of pages too. Even though the page turner wasn't incredibly successful at turning pages, the prof was so impressed with the scope of the design it was moved to a display case at the Engineering building (it might even still be there).

![Page Turner](https://live.staticflickr.com/5819/24104679486_72835ec93e_b.jpg){: width="600"} 
![Page Turner](https://live.staticflickr.com/5829/24130772105_3bb7c144b9_b.jpg){: width="600"} 
![Page Turner](https://live.staticflickr.com/5741/24130771885_de1752930b_b.jpg){: width="600"} 