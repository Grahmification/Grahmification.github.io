---
title: Investing Reference Info
layout: page
permalink: /reference/investing/
---

A misc collection of information related to investing.

## Reference Info
- [Canadian Couch Potato](https://canadiancouchpotato.com/) - Excellent guide to passive index investing

Calculators:
- [The Measure of a Plan](https://themeasureofaplan.com/) - An excellent online resource with various financial tools. Has a great stock tracking spreadsheet.


## Online Tools

Some handy tools are listed here. Also check out [Novel Investor](https://novelinvestor.com/financial-tools/) for another big list.

Taxes:
- [RRSP Contribution Optimizer](https://www.rrspcontribution.ca/) - Optimize how much you should contribute to your RRSP

ETFs:
- [ETFdb](https://etfdb.com/) - Massive database of ETFs
- [ETF Breakdown](https://www.etfbreakdown.com/) - Compares underlying holdings for an ETF portfolio

General News:
- [Seeking Alpha](https://seekingalpha.com/)
- [Moody's](https://www.moodys.com/)

Detailed Stats:
- [Finviz](https://finviz.com/) - Highly detailed stock tracking (Note: US exchanges only)
  - Check out the [Finviz Map](https://finviz.com/map.ashx?t=sec)
- [Whale Wisdom](https://whalewisdom.com/) - Use to look up percent ownership of a stock
- <a href="http://openinsider.com/" data-proofer-ignore>Open Insider</a> - Insider trading stats for US companies
- [Insider Tracking](https://www.insidertracking.com/) - Insider trading stats for Canadian companies
- [SEC Filings](https://www.sec.gov/search-filings) - Look up specific company filings
- [Fitch Ratings](https://www.fitchratings.com/) - Look up bond ratings for Canadian companies

## Economic Indicators

This data is embedded from [Trading Economics](https://tradingeconomics.com/indicators). The embedded iFrame can be inspected to get the underlying lightweight image link.

### Interest Rates
{% include embed-charts-trading-econ.html indicator="fdtr" d1="1982-01-01" d2="2014-11-30" url2="/canada/interest-rate" %}

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
