---
title: Automatic Watch
date: 2018-08-01 14:00:00 -0800 #-0800 = pst time
categories: [Projects, Hobby]
tags: [design, cad, machining]     # TAG names should always be lowercase
thumbnail: /files/images/watch-thumbnail.jpg
---

Having previously built a few mechanical clocks out of lego, I always thought machining a custom watch would be a really cool project to hone my abilities, and hopefully result in something I could use for a very long time. 

{% capture imagePath %}/files/images{% endcapture %}

<div class="container">
  <div class="row">
    <div class="col">
      <img src='{{ imagePath }}/watch-render-black.jpg' alt='watch-render' width="400px" />
    </div>
    <div class="col">
      <img src='{{ imagePath }}/watch-thumbnail.jpg' alt='watch-completed' width="400px" />
    </div>
  </div>
  <em>
    There's nothing more exciting than seeing a CAD model come to life.
   </em>
</div>

## Design

The watch was designed around a 2051 Chinese automatic movement from [Perrin Watch Parts](https://perrinwatchparts.com/). Chinese movements are a good compromise between cost and reliability, and I didn't want to go too expensive for the first iteration. One annoyance is that it's nearly impossible to find movement dimensions or drawings. Everything in the watch industry uses confusing antiquated standards; movements are measured in ligne (1 ligne = 2.2558 mm). I had to order the 12.25 ligne movement first and painstakingly measure it before finalizing a lot of the design. In hindsight, an ETA movment may have been a better choice for better availability.

Most of the parts were designed to be milled from aluminum, with the face waterjet from stainless shim stock. The bezel and backing plate attach with M2 screws rather than conventional large diameter fine pitch threads to avoid threadmilling. Glass windows are widely available in 1mm diameter increments from watch supply stores.

![watch-finished-backside]({{ imagePath }}/watch-finished-backside.jpg){: width="600"} 
_Adding a glass back cover complicated the design, but was totally worth it to see the movement_

## Machining

Machining parts for the watch posed many challenges: primarily fixturing small, oddly shaped parts. Things need to be aligned pretty well to make sure 0.1mm chamfers are even over the whole part.

![Watch case final operation]({{ imagePath }}/watch-case-op5-setup.jpg){: width="600"} 
_Final operation on the case. It was held down with the M2 screws for the bezel._

![Watch crown final operation]({{ imagePath }}/watch-crown-op3-setup.jpg){: width="600"} 
_The final operation on the crown was done with a similar method_

The links were particularly tricky as there isn't a single flat surface to pick up off for OP2. A set of custom soft jaws was made to clamp the links without crushing them. Making the jaws was also not trivial.

<div class="container">
  <div class="row">
    <div class="col">
      <img src='{{ imagePath }}/watch-link-op2-jaws.jpg' alt='Link OP2 jaws' width="400px" />
    </div>
    <div class="col">
      <img src='{{ imagePath }}/watch-link-op2.jpg' alt='Link OP2 setup' width="400px" />
    </div>
  </div>
  <em>
    Custom jaws made for the second operation on the links.
   </em>
</div>

Similar jaws were designed to hold parts for the clasp. These parts were tricky just because of how small they were. This was the simplest design I could come with. Drilling and tapping M1.6 threads into the stainless rod was also fun.

<div class="container">
  <div class="row">
    <div class="col">
      <img src='{{ imagePath }}/watch-clasp-exploded.jpg' alt='watch-clasp-exploded' width="400px" />
    </div>
    <div class="col">
      <img src='{{ imagePath }}/watch-clasp-assembled.jpg' alt='watch-clasp-assembled' width="400px" />
    </div>
  </div>
  <em>
    There are a lot of tiny parts that go into the clasp.
   </em>
</div>

## Assembly

Assembly was quite straightforward. All parts were test assembled prior to anodizing.

![watch-test-assembly]({{ imagePath }}/watch-test-assembly.jpg){: width="600"} 
_The watch looks pretty good raw._

The biggest issue with assembly was that shims needed to be tweaked between the movement, face, and crown. In hindsight it may have been better to have the back cover compress the movement, and the crown compress the face so these could be adjusted individually.

![watch-face-shim-installation]({{ imagePath }}/watch-face-shim-installation.jpg){: width="350"} 
_Shims needed to be tweaked to get the face to fit snugly._

The diamond drag engraver does really nice work on aluminum. The back cover provided the only flat surface to engrave.

![watch-back-engraving]({{ imagePath }}/watch-back-engraving.jpg){: width="500"} 
_Engraving on the back cover._

Here are some glamour shots of the finished watch.

![watch-finished-wrist]({{ imagePath }}/watch-finished-wrist.jpg){: width="1000"} 
_It looks pretty good. A huge relief to find it comfortable too._

![watch-finished-backside-horiz]({{ imagePath }}/watch-finished-backside-horiz.jpg){: width="1000"} 
_Inside view showing the movement._

![watch-finished-front]({{ imagePath }}/watch-thumbnail.jpg){: width="1000"} 
_The 3D contouring toolmarks make a cool texture on the crown and case._

## Future Improvements

Changes I would make if I made another watch:

1. Waterproofness
    - Basically nothing was done for waterproofing this watch. This isn't a must, but very nice to have. The crown shaft hole can be filled with grease for waterproofing.
2. Fitment of the movement/face
   - Try to improve how the movement and face are secured into the case. This looks like it may be a problem on most watches though so there might not be a great solution.
3. Cover back window
   - The cover back window glues on from the inside to give a really nice transition to the metal on the outside. This has worked fine so far, the there is always a risk the glass could get pushed inwards.
4. Experiment with different metals
   - Anodized aluminum looks great but isn't super durable. Look into things like hardened 17-4PH stainless, possibly with a DLC or PVD coating.

