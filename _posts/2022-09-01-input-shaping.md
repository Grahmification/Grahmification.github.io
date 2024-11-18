---
title: Reducing Vibration With Input Shaping
date: 2022-09-01 14:00:00 -0800 #-0800 = pst time
categories: [Projects, Zaber]
tags: [coding, mathematics]     # TAG names should always be lowercase
thumbnail: /files/images/resonance-transmissibility-curve.png
---

{% capture imagePath %}/files/images{% endcapture %}

Input shaping is an extremely interesting technology. It offers significant productivity gains in the field of motion control with almost no cost. Sound too good to be true? Surpringly, input shaping is a topic that gets very little attention. As of writing this article, the [Wikipedia Page](https://en.wikipedia.org/wiki/Input_shaping) on input shaping has a mere single paragraph explanation.

I've already written a relatively detailed article on input shaping: [Input Shaping for Motion Control Vibration Reduction](https://www.zaber.com/articles/input-shaping-for-vibration-reduction). However, this topic has so much merit I've felt inclined to write an article here to cover more things not suitable for technical note.

## Overview

So what is input shaping? In reality, the gist is relatively simple:

1. Objects tend to vibrate at a certain frequency (or frequencies).
2. Determine what those frequencies are.
3. When you move the object, move it in such a manner that doesn't excite those frequencies.
4. The object will vibrate less when you stop, allowing you to do things faster (ex. take a picture without blur).

What does this actually look like? Check this out:
<div style="width:75%; margin:auto;">
    {% include embed/youtube.html id='Z4QLKsjBEDY?si=UKG7emSgea2AAi6g&amp;start=100&autoplay=0&mute=1&controls=1' %}
</div>
_Preventing liquid spills is a highly useful application for input shaping_

Note that not only does the water stop sloshing, but the motion is also faster! This is a major win for something as simple as tweaking the trajectory.

## Interesting Applications

Let's start with the cool stuff! Here are some applications of input shaping that I consider to be particularly interesting and relevant. 


### 3D Printing

The use of input shaping for 3D printing is particularly exciting because I see it as the first mainstream implmentation of the technology. This pretty cool considering the [gold standard paper](https://www.semanticscholar.org/paper/Preshaping-Command-Inputs-to-Reduce-System-Singer-Seering/f4047c3fa2d34f4f0f887b9cd40d64bee0d88c97) on input shaping was published over 30 years ago! Until quite recently a google search on input shaping would return only academic papers, which are now replaced with hobbiests discussing the performance of their printers.

Over the past couple years it's become the norm for medium to high end 3D printers to support input shaping. I believe one of the big first adopters was [Klipper](https://www.klipper3d.org/), an open source 3d-Printer firmware. Their cheap performance gains were so advantageous they've driven many other companies to follow suit.

So why is input shaping such a big deal? The answer is that vibrations create print defects, and input shaping allows increasing print speeds without introducing defects. See the video for examples:

<div style="width:75%; margin:auto;">
    {% include embed/youtube.html id='er7q-CJL1lc?si=-KT2BI0LcL41H7bf&amp;start=466' %}
</div>
_Print quality improvements from input shaping make it a no brainer given the low cost_

The low price targets of 3D printers also make input shaping particularly enticing. Why waste money making your printer stiffer when you can solve the problem at the software level?!

Cheap accelerometers are another key technology paving the way to adoption. Complete USB powered PCBs with sensors like the [ADXL345](https://www.adafruit.com/product/1231) are widely available for around $20. This means that an intelligent 3D printer can easily measure it's own resonances in situ with the occasional calibration routine, providing far better performance than a preset factory calibration.

More information on Klipper can be found below:
* [Resonance Compensation](https://www.klipper3d.org/Resonance_Compensation.html)
* [Measuring Resonances](https://www.klipper3d.org/Measuring_Resonances.html)
* [Source Code](https://github.com/Klipper3d/klipper)


### Cranes

Cranes are an excellent case study for input shaping because the low frequencies allow easy visualization of the theory. Cranes are actually one of the [oldest applications of input shaping](https://code.eng.buffalo.edu/tdf/papers/acc_tut.pdf). You've probably watched them your whole life and never thought twice about why payload swaying isn't a problem. While it's easy to chalk this up to operator skill, the reality is that the crane's control systems handle this on the fly automatically.

Below is an example demonstrating input shaping on a dual hoist crane. This implementation is slightly different due to the dual trolleys, but the underlying theory is identical.

<div style="width:75%; margin:auto;">
    {% include embed/youtube.html id='on3RUdRhd2c?si=-vVhV_dNA_1YL3Xu&amp;start=6' %}
</div>
_Georgia Tech is the source of many excellent input shaping papers_

One interesting point demonstrated in this video is that input shaping can be used "in reverse" to intentionally amplify vibrations. This is akin to a human pumping on a swingset, and although clearly less practical, is cool demonstration of the technology.

It's also worth noting why cranes are inherently well suited for input shaping. The key is that there's typically a single dominant resonant frequency, and it can be determined with relative ease:
1. The spool motor can track the length of extended cable.
2. A loadcell can measure the attached payload weight.
   * If the cable is assumed to have neglible weight this isn't actually required, but improves the estimate. 
3. The resonant frequency can be estimated with equations for a [compound pendulum](https://en.wikipedia.org/wiki/Pendulum#Period_of_oscillation).

While the typical crane is quite simple, there has also been a lot of research into more advanced cases such as [dual pendulum configurations](https://www.youtube.com/watch?v=Hdxb-6wU1JA) or gantry cranes where additional yaw rotational frequencies may exist. 


### Multi-Dimensional Robot Arm Control

Most input shaping applications are done in one dimension. Even for multi-axis systems (ex. XYZ), each direction is normally treated independently. However, this example from [The No Spill Project](https://sites.google.com/view/thenospillproject) shows a far more complex (but very elegant!) multi-DOF example. It combines input shaping on all 6 degrees of freedom simultaneously to prevent a cup of water from spilling. 

<div style="width:75%; margin:auto;">
    {% include embed/youtube.html id='oR3C-feQ6f8' %}
</div>
_Multi-DOF input shaping as shown here is cutting edge_

It should be noted that this example isn't "conventional" input shaping; the underlying theory is different because it relies on minimizing tangential forces on the liquid rather than moving away from the resonant frequency. However, the general principle is the same: the motion trajectory is modified in a clever way to produce a result with reduced vibration.

Additional details on the project can be found here:
* Paper: [A Solution to Slosh-free Robot Trajectory Optimization](https://arxiv.org/abs/2210.12614)
* Paper: [Geometric Slosh-Free Tracking for Robotic Manipulators](https://arxiv.org/abs/2402.05197), [Source Code](https://github.com/jonarriza96/gsft)

<div style="width:75%; margin:auto;">
    {% include embed/youtube.html id='4kitqYVS9n8' %}
</div>
_The general theory behind this slosh control algorithm is relatively simple, but the implementation is impressive_


## Theory

So you want to learn input shaping? There are quite a few useful [learning references](#useful-references) below.

However, there's also a lot of key foundational material that's missing from existing input shaping content on the web. The goal this section is to elaborate on some of these aspects that I consider to be non-intuitive and generally aren't explained well.

### Frequency Dependence

One of the biggest fundamental aspects I consider easy to overlook is the importance of input frequency on vibrations. Everyone intuitively knows that shaking an object harder (larger amplitude) will cause it to vibrate more. What's less intuitive is that adjusting the speed of shaking (frequency) also has an equally significant effect.

Consider the animation below. Three pendulums are swung at the exact same amplitude, but with different frequencies. The middle pendulum vibrates drastically more because the input frequency is near it's resonant frequency. If we were trying to move the pendulum at this frequency we'd have vibration problems, but we could speed up or slow down to get much better results.

![Resonant Pendulums]({{ imagePath }}/resonance-animation-driven-pendulums.gif){: width="250"}
_Three identical pendulums excited with the same amplitude, but different frequency._

The behavior of these pendulums is plotted below on a transmissibility curve. 
1. At low input frequencies (slow shaking), the resulting vibration almost perfectly matches the input.
2. As the input frequency approaches the resonant frequency, the vibration gets very large.
3. As the input frequency exceeds the resonant frequency, the vibration starts to decrease again, eventually approaching zero.

If this doesn't make sense to you, try shaking something flexible like a metal ruler at different speeds and see if you can replicate the curve.

![Resonance Transmissibility Plot]({{ imagePath }}/resonance-transmissibility-curve.png){: width="600"}
_Behavior of the animated pendulums plotted over many input frequencies. The middle case occurs at a frequency ratio of 1._

This plot visualizes the most important principle of input shaping; if you move an object at frequencies near it's resonant frequency, you're going to have vibration problems. Another key realization is that we have two options to solve this: speeding up or slowing down!

It should be noted that adding damping will also reduce vibrations, as can be seen from the many curves plotted above for various damping ratios. But why would we waste money on damping when we could simply move faster instead?! This realization is one of the reasons input shaping is such an elegant solution. 


### Fourier's Theorem

So you get it: to avoid vibrations, don't move objects at their resonant frequency. But you don't want to shake your object with an amplitude and frequency; you just want to move from point A to B. How is this theory still relevant?

The theory above only applies to inputs that are a sine wave. But this generally isn't the case for most motion trajectories! Thankfully, [Fourier's theorem](https://en.wikipedia.org/wiki/Fourier_series) is to the rescue:
* A periodic function f(x) which is reasonably continuous may be expressed as the sum of a series of sine or cosine terms (called the Fourier series), each of which has specific amplitude and phase coefficients known as Fourier coefficients.

What does this actually mean? Essentially, it means we can represent any curve with sine waves. This might be hard to believe, but check out the example below: we can produce a highly complex function just by adding four sine waves together!

![Fourier Circles Animation]({{ imagePath }}/fourier-series-square-wave-circles-animation.svg){: width="400"}
_Combining four sine waves produces a highly complex curve._

Still skeptical? The next example shows how we can represent a highly complex function with sine waves. If we added infinite sine waves together we'd be able to match the line perfectly. 

![Fourier Converence Animation]({{ imagePath }}/fourier-convergence-example.gif){: width="300"}
_Even complicated functions can be represented by sine waves._

While Fourier's theorem states that we need infinite sine waves to perfectly represent any curve, a key observation is that we can get pretty close with only a few sine waves. What this ultimately means is:
* To represent a curve with sine waves, there are ususally a few dominant frequencies with large amplitude, and the rest have relatively small amplitude.

It may have clicked by now, but if not: we better make sure that none of the dominant sine wave components have frequencies near the object's resonant frequency.

To summarize, because any curve can be represented by sine waves, the input shaping theory for sine waves also works for any curve.


### Implementing Real Trajectories

So how do we actually go about input shaping for real trajectories? There are a few important points:
* Vibrations are induced by forces acting on the system.
* Forces are proportional to acceleration (F=ma).
* The [fast fourier transform](https://en.wikipedia.org/wiki/Fast_Fourier_transform) (FFT) is an easy method to decompose a function into it's sine waves (frequency components).

![Fast Fourier Transform]({{ imagePath }}/fft-frequency-spectrum-example.png){: width="500"}
_The FFT extracts frequency components (sine waves) from a time series signal._


Therefore, to determine if a trajectory will cause problematic vibrations:
1. Compute the trajectory (position vs time).
2. Differentiate it twice to get acceleration vs time.
3. Multiply by the mass to get force vs time.
4. Compute the FFT of the force vs time signal.
5. Compute the spectral density of the FFT (amplitude vs frequency).
6. Confirm that regions of the frequency spectrum near the resonant frequency have small amplitude.

That's it! If the FFT amplitude is large near the resonant frequency, there's a significant sine wave component around that frequency and we'll get bad vibrations. See [here](https://www.zaber.com/articles/input-shaping-for-vibration-reduction#Relation_to_Other_Trajectory_Modifications) for examples of this in practice.

Input shaping algorithms are just fancy methods of performing this process in reverse: target low magnitudes around the resonant frequency and work backwards to find a trajectory that accomplishes it! However, you can get a sense of how this becomes complicated quickly, for example if we wanted to target multiple resonant frequencies or enforce specific performance constraints on the trajectory. 


### Relationship with Servo Tuning

This section is included to avoid a common pitfall of the aspiring engineer: "I need my machine to do x faster, so I need better servo tuning". While this is true, servo tuning is only half the battle: input shaping is equally important!
* Get your servo tuning decent, then focus on input shaping.
* Servo controllers have their own resonant frequency. This could be significant in additon to the system's mechanical resonances. If so, make sure the input shaping works for both frequencies. 


## Useful References

Here are some useful references to learn more about input shaping. Most of these are mentioned in the article, but are also included here for convenient reference:
1. Kerr, G. (2022): [Input Shaping for Motion Control Vibration Reduction](https://www.zaber.com/articles/input-shaping-for-vibration-reduction)
2. Singer, N. C., & Seering, W. P. (1990): [Preshaping Command Inputs to Reduce System Vibration](https://www.semanticscholar.org/paper/Preshaping-Command-Inputs-to-Reduce-System-Singer-Seering/f4047c3fa2d34f4f0f887b9cd40d64bee0d88c97)
3. Singh, T., & Singhose, W. (2002): [Tutorial on Input Shaping](https://code.eng.buffalo.edu/tdf/papers/acc_tut.pdf)
4. Conker, C., Yavus, H., & Bilgic, H. H. (2016): [A review of command shaping techniques for flexible-joint manipulators](https://www.extrica.com/article/16725)
5. Huey, J. R., (2006): [The Intelligent Combination of Input Shaping and PID Feedback Control](https://hdl.handle.net/1853/11594)
6. NASA (1995): [Minimizing Structural Vibrations with Input Shaping](https://ntrs.nasa.gov/api/citations/19950024365/downloads/19950024365.pdf)
7. Klipper 3D: [Resonance Compensation](https://www.klipper3d.org/Resonance_Compensation.html) 