---
title: Ultra Precision Vertical Stage Series
date: 2022-04-01 14:00:00 -0800 #-0800 = pst time
categories: [Projects, Zaber]
tags: [design, cad]     # TAG names should always be lowercase
thumbnail: /files/images/X-LDA-AEZ-w400.png
---

{% capture imagePath %}/files/images{% endcapture %}

The [LDA-AEZ](https://www.zaber.com/products/vertical-stages/X-LDA-AEZ) and [LDM-AEZ](https://www.zaber.com/products/vertical-stages/X-LDM-AEZ) series of ultra-precision vertical stages fill out the Zaber's direct drive product lineups with vertical axis options. I oversaw the design and launch of these products from the working prototype phase into a polished mass production ready design.

![LDA and LDM Vertical Stage Comparison]({{ imagePath }}/LDA-LDM-AEZ-Comparison-w850.png){: width="500"} 
_The vertical stages are available in two family sizes: the LDA and LDM_

## Background

These stages are particularly exciting additions to Zaber's product lineup because they enable building complete ultra-precision XYZ motion systems. Until this launch there was no solution to meet missing puzzle piece of an ultra-precision Z-axis.

![LDA and LDM XYZ Stage Assembly]({{ imagePath }}/XY-LDM-Z-LDA-w1000.png){: width="600"} 
_An ultra-precision 3-axis system with XY LDMs and an LDA Z-axis_

These XYZ systems are well suited for applications like automated fiber alignment or micro-machining thanks to the excellent precision and dynamic performance offered by direct drive stages.

Significant flexibility is also offered by the two different family sizes. For spaced-constrained applications, the compact LDA is rated for payloads up to 16N, while the larger LDM can handle payloads up to 55N.

## Design

Conventionally, linear motor stages are not well suited for vertical applications. Unlike ballscrews, linear motors have no mechanical advantage and thus generate significant heat trying to hold the stage in place. Even worse, the stage will fall uncontrollably if power is lost.

To combat these problems, some kind of mechanism is required to compensate for gravity induced forces on the stage. These stages feature a passive magnetic counterbalance integrated onto the side. The counterbalance provides a constant, user adjustable force which can be finely tuned to balance a given payload.

<p style="float: right; margin-right: 35px ; margin-left: 35px">
    <img src='{{ imagePath }}/Magnetic-counterbalance-working-principle-500px.jpg' alt='Magnetic Counterbalance Working Principle' width="200px" />
    <em>
    A simplified magnetic counterbalance diagram
    </em>
</p>

While most engineers are familar with counterbalances utilizing a pulley and weight like those found in elevators, magnetic counterbalances are a relatively niche variety. Typically reserved for high performance applications like semiconductor manufacturing, they have numerous benefits for ultra-precision motion systems. Most importantly, frictionless design means that precision is unaffected; performance is nearly identical between horizontal and vertical axis models.

To learn more about magnetic counterbalances, see the article: 
* [Magnetic Counterbalances for High Performance Vertical Stages](https://www.zaber.com/articles/magnetic-counterbalances-for-vertical-applications)

## Patent

Despite being niche, magnetic counterbalances are actually readily available on the market, with the classic design being LinMot's [Magspring](https://linmot.com/products/magspring/). 

However, this counterbalance design includes a very unique feature: user-adjustability. The counterbalance force can be changed in moments with the turn of a screw. Fine user-adjustability is particularly beneficial for tuning the stage's power-off behavior. The payload can be tuned to slightly raise, slightly fall, or remain neutral in the event of a power loss. For example, a microscope objective can be tuned to delicately retract from the sample, preventing damage during a power loss.

The combination of a user-adjustable, constant-force, passive, magnetic counterbalance was so unique that we were able to successfully patent the design: [US Patent 20220037070](https://patents.google.com/patent/US20220037070A1/).



_Note: The content of this article is intentionally limited to respect confidential information of Zaber Technologies._
