---
title: Useful Reference Info
layout: page
permalink: /reference/
---

The page contains a bunch of random links and information I've found useful. There is no particular structure to it and it may be split up to individual pages in the future.

## Coding
---
- [Markdown Cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)
- [TLDR Legal](https://tldrlegal.com/) - Software Licenses in Plain English
- [Regex 101](https://regex101.com/) - testing regular expressions
- [SolidWorks 2021 API Help](https://help.solidworks.com/2021/English/api/SWHelp_List.html?id=7b437ecba4ea45bf8d4d196ff8df4807#Pg0)

### Interesting Libraries
#### C#:
- [Oxyplot](https://github.com/oxyplot/oxyplot) - amazing 2d plotting library ![GitHub](https://img.shields.io/github/license/oxyplot/oxyplot) 
- [Helix Toolkit](https://github.com/helix-toolkit/helix-toolkit) - super powerful 3D rendering library ![GitHub](https://img.shields.io/github/license/helix-toolkit/helix-toolkit)
- [Math.NET Numerics](https://github.com/mathnet/mathnet-numerics) - for advanced math ![GitHub](https://img.shields.io/github/license/mathnet/mathnet-numerics)
- [AForge.NET](http://www.aforgenet.com/) - computer vision, ai, machine learning
- [Xabe.FFmpeg](https://github.com/tomaszzmuda/Xabe.FFmpeg) - C# FFmpeg port. Audio/video converting.

#### Python:
- [OpenCV](https://github.com/opencv/opencv) - computer vision library
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/) - web scraping tool
- [openpyxl](https://pypi.org/project/openpyxl/) - excel import/export

#### Javascript:
- [Leaflet](https://github.com/Leaflet/Leaflet) - map making ![GitHub](https://img.shields.io/github/license/Leaflet/Leaflet)
- [D3](https://github.com/d3/d3) - super powerful data visualizations ![GitHub](https://img.shields.io/github/license/d3/d3)
- [Plotly.js](https://github.com/plotly/plotly.js) - plotting helper build on top of D3 ![GitHub](https://img.shields.io/github/license/plotly/plotly.js)
- [FontAwesome](https://fontawesome.com/) - big library of free icons


## Mechanical Design
---

- [Slocum Fundamentals of Design](http://pergatory.mit.edu/resources/fundamentals.html) - possibly one of the best design guides ever written
- [Precision Point](https://www.jpe-innovations.com/precision-point/) - incredibly good precision and robotics design info
- [Precision Balls Papers](https://www.precisionballs.com/tech_papers.php) - info on kinematic couplings

### CAD
- [Thingiverse](https://www.thingiverse.com/) - huge library of 3D printing and lasercutting projects with files
- [GrabCAD](https://grabcad.com/library) - huge library of CAD models

### Mechanical Reference
- [ISO fits calculator](https://amesweb.info/fits-tolerances/tolerance-calculator.aspx) - visualize shaft/hole fits
- [ISO preferred fits](https://amesweb.info/fits-tolerances/preferred-tolerances-table.aspx) - list of preferred fits
- [Press fit calculator](https://amesweb.info/press-fit/interference-fit-calculator.aspx) - super detailed loading calculator

- [MatWeb](http://www.matweb.com/search/CompositionSearch.aspx) - huge material properties database

- [Bolt torque/tightness conversions](https://www.tohnichi.com/pdf/02-bolt-tightening.pdf) - printable

- [Tap & drill size chart](https://littlemachineshop.com/images/Gallery/PDF/TapDrillSizes.pdf) - printable
- [Surface speeds list](https://littlemachineshop.com/reference/cuttingspeeds.php)

- [Friction Coefficients](https://www.engineeringtoolbox.com/friction-coefficients-d_778.html) - big list

## Software
---
- [Project Awesome](https://project-awesome.org/johnjago/awesome-free-software) - huge list of free software
- [PyCharm](https://www.jetbrains.com/pycharm/) - great python IDE
- [GitKraken](https://www.gitkraken.com/) - amazing tool for Git repo management
- [MediaWiki](https://www.mediawiki.org/wiki/MediaWiki) - host your own wiki

- [Onshape](https://www.onshape.com/en/) - free CAD software
- [Scilab](https://www.scilab.org/) - open source control systems analysis software
- [FEMM](https://www.femm.info/wiki/HomePage) - open source 2D magnetics FEA software
- [ONELAB](https://onelab.info/) - open source 3D FEA software

- [funfun.io](https://www.funfun.io/1/#/home) - really interesting plotting software combining javascript, html and excel 

- [3DF Zephyr](https://www.3dflow.net/3df-zephyr-photogrammetry-software/) - free photogrammetry software (turn pictures into 3D models)
- [Meshmixer](https://www.meshmixer.com/) - free, very powerful 3D print editing software

## Misc
---
- [12ft Ladder](https://12ft.io/) - disables website paywalls

### Music
- [Music Map](https://www.music-map.com/) - find similar music
- [MusicBrains](https://musicbrainz.org/) - huge free database of music. Includes REST API.

### Cooking
- [Budget Bytes](https://www.budgetbytes.com/)
- [AllRecipes](https://www.allrecipes.com/)
- [Well Plated](https://www.wellplated.com/)
- [Shane & Simple](https://shaneandsimple.com/recipes/) - vegetarian

## Economic Indicators

This data is embedded from [Trading Economics](https://tradingeconomics.com/indicators). The embedded iFrame can be inspected to get the underlying lightweight image link.

### Inflation Rates (CPI, YoY)
{% include embed-charts-trading-econ.html indicator="cpi+yoy" d1="19960228" d2="20200222" url2="/canada/inflation-cpi" %}

### M2 Money Supply
{% include embed-charts-trading-econ.html indicator="unitedstamonsupm2" d1="19960228" d2="20200222" url2="/canada/money-supply-m2" %}

### Central Bank Balance Sheet
{% include embed-charts-trading-econ.html indicator="unitedstacenbanbalsh" d1="19960301" d2="20160225" url2="/canada/central-bank-balance-sheet" %}

### Consumer spending
{% include embed-charts-trading-econ.html indicator="unitedstaconspe" d1="19960228" d2="20180222&" url2="/canada/consumer-spending" %}

### Unemployment Rates
{% include embed-charts-trading-econ.html indicator="usurtot" d1="19960228" d2="20200222&" url2="/canada/unemployment-rate" %}
