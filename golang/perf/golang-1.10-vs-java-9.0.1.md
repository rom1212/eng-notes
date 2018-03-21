<header id="top">

# [The Computer Language  
Benchmarks Game](https://benchmarksgame.alioth.debian.org/)

</header>

<article>

<div>

## Go programs versus Java

<aside>

[all other Go programs & measurements](./measurements.php?lang=go)

</aside>

</div>

<section>

<div>

### by benchmark task performance

</div>

<table>

<tbody>

<tr>

<th colspan="3">[<span>reverse-complement</span>](./revcomp.html)</th>

<th colspan="3"></th>

</tr>

<tr>

<th>source</th>

<th>secs</th>

<th>mem</th>

<th>gz</th>

<th>cpu</th>

<th>cpu load</th>

</tr>

<tr>

<td>[<span>Go</span>](./program.php?test=revcomp&lang=go&id=6)</td>

<td class="best">0.63</td>

<td>89,120</td>

<td>1338</td>

<td>1.00</td>

<td class="message">39% 43% 27% 57%</td>

</tr>

<tr>

<td>[<span>Java</span>](./program.php?test=revcomp&lang=java&id=8)</td>

<td>1.03</td>

<td>191,064</td>

<td>2183</td>

<td>2.31</td>

<td class="message">52% 57% 43% 74%</td>

</tr>

</tbody>

<tbody>

<tr>

<th colspan="3">[<span>pidigits</span>](./pidigits.html)</th>

<th colspan="3"></th>

</tr>

<tr>

<th>source</th>

<th>secs</th>

<th>mem</th>

<th>gz</th>

<th>cpu</th>

<th>cpu load</th>

</tr>

<tr>

<td>[<span>Go</span>](./program.php?test=pidigits&lang=go&id=3)</td>

<td class="best">2.02</td>

<td>9,256</td>

<td>603</td>

<td>2.02</td>

<td class="message">0% 0% 100% 0%</td>

</tr>

<tr>

<td>[<span>Java</span>](./program.php?test=pidigits&lang=java&id=2)</td>

<td>3.12</td>

<td>36,788</td>

<td>938</td>

<td>3.31</td>

<td class="message">6% 3% 4% 96%</td>

</tr>

</tbody>

<tbody>

<tr>

<th colspan="3">[<span>fannkuch-redux</span>](./fannkuchredux.html)</th>

<th colspan="3"></th>

</tr>

<tr>

<th>source</th>

<th>secs</th>

<th>mem</th>

<th>gz</th>

<th>cpu</th>

<th>cpu load</th>

</tr>

<tr>

<td>[<span>Go</span>](./program.php?test=fannkuchredux&lang=go&id=1)</td>

<td class="best">14.72</td>

<td>1,540</td>

<td>900</td>

<td>58.65</td>

<td class="message">100% 100% 99% 100%</td>

</tr>

<tr>

<td>[<span>Java</span>](./program.php?test=fannkuchredux&lang=java&id=1)</td>

<td>17.26</td>

<td>32,116</td>

<td>1282</td>

<td>67.75</td>

<td class="message">98% 99% 97% 99%</td>

</tr>

</tbody>

<tbody>

<tr>

<th colspan="3">[<span>fasta</span>](./fasta.html)</th>

<th colspan="3"></th>

</tr>

<tr>

<th>source</th>

<th>secs</th>

<th>mem</th>

<th>gz</th>

<th>cpu</th>

<th>cpu load</th>

</tr>

<tr>

<td>[<span>Go</span>](./program.php?test=fasta&lang=go&id=3)</td>

<td class="best">2.08</td>

<td>3,640</td>

<td>1358</td>

<td>5.69</td>

<td class="message">84% 66% 70% 56%</td>

</tr>

<tr>

<td>[<span>Java</span>](./program.php?test=fasta&lang=java&id=5)</td>

<td>2.33</td>

<td>43,924</td>

<td>2473</td>

<td>6.07</td>

<td class="message">53% 71% 63% 74%</td>

</tr>

</tbody>

<tbody>

<tr>

<th colspan="3">[<span>mandelbrot</span>](./mandelbrot.html)</th>

<th colspan="3"></th>

</tr>

<tr>

<th>source</th>

<th>secs</th>

<th>mem</th>

<th>gz</th>

<th>cpu</th>

<th>cpu load</th>

</tr>

<tr>

<td>[<span>Go</span>](./program.php?test=mandelbrot&lang=go&id=4)</td>

<td class="best">5.48</td>

<td>30,912</td>

<td>905</td>

<td>21.79</td>

<td class="message">99% 99% 99% 100%</td>

</tr>

<tr>

<td>[<span>Java</span>](./program.php?test=mandelbrot&lang=java&id=2)</td>

<td>6.04</td>

<td>76,528</td>

<td>796</td>

<td>23.34</td>

<td class="message">98% 97% 97% 97%</td>

</tr>

</tbody>

<tbody>

<tr>

<th colspan="3">[<span>spectral-norm</span>](./spectralnorm.html)</th>

<th colspan="3"></th>

</tr>

<tr>

<th>source</th>

<th>secs</th>

<th>mem</th>

<th>gz</th>

<th>cpu</th>

<th>cpu load</th>

</tr>

<tr>

<td>[<span>Go</span>](./program.php?test=spectralnorm&lang=go&id=4)</td>

<td class="best">3.94</td>

<td>2,344</td>

<td>548</td>

<td>15.71</td>

<td class="message">100% 100% 100% 100%</td>

</tr>

<tr>

<td>[<span>Java</span>](./program.php?test=spectralnorm&lang=java&id=2)</td>

<td>4.23</td>

<td>34,472</td>

<td>950</td>

<td>16.27</td>

<td class="message">96% 97% 97% 96%</td>

</tr>

</tbody>

<tbody>

<tr>

<th colspan="3">[<span>n-body</span>](./nbody.html)</th>

<th colspan="3"></th>

</tr>

<tr>

<th>source</th>

<th>secs</th>

<th>mem</th>

<th>gz</th>

<th>cpu</th>

<th>cpu load</th>

</tr>

<tr>

<td>[<span>Go</span>](./program.php?test=nbody&lang=go&id=1)</td>

<td class="best">21.37</td>

<td>1,536</td>

<td>1310</td>

<td>21.38</td>

<td class="message">0% 0% 100% 0%</td>

</tr>

<tr>

<td>[<span>Java</span>](./program.php?test=nbody&lang=java&id=5)</td>

<td>22.10</td>

<td>33,136</td>

<td>1429</td>

<td>22.20</td>

<td class="message">31% 1% 1% 70%</td>

</tr>

</tbody>

<tbody>

<tr>

<th colspan="3">[<span>k-nucleotide</span>](./knucleotide.html)</th>

<th colspan="3"></th>

</tr>

<tr>

<th>source</th>

<th>secs</th>

<th>mem</th>

<th>gz</th>

<th>cpu</th>

<th>cpu load</th>

</tr>

<tr>

<td>[<span>Go</span>](./program.php?test=knucleotide&lang=go&id=3)</td>

<td>12.77</td>

<td>148,052</td>

<td>1722</td>

<td>47.35</td>

<td class="message">87% 97% 94% 95%</td>

</tr>

<tr>

<td>[<span>Java</span>](./program.php?test=knucleotide&lang=java&id=1)</td>

<td>8.70</td>

<td>375,568</td>

<td>1812</td>

<td>27.17</td>

<td class="message">80% 72% 74% 88%</td>

</tr>

</tbody>

<tbody>

<tr>

<th colspan="3">[<span>regex-redux</span>](./regexredux.html)</th>

<th colspan="3"></th>

</tr>

<tr>

<th>source</th>

<th>secs</th>

<th>mem</th>

<th>gz</th>

<th>cpu</th>

<th>cpu load</th>

</tr>

<tr>

<td>[<span>Go</span>](./program.php?test=regexredux&lang=go&id=2)</td>

<td>28.21</td>

<td>323,820</td>

<td>802</td>

<td>59.87</td>

<td class="message">69% 46% 50% 48%</td>

</tr>

<tr>

<td>[<span>Java</span>](./program.php?test=regexredux&lang=java&id=3)</td>

<td>10.34</td>

<td>627,224</td>

<td>929</td>

<td>29.88</td>

<td class="message">74% 72% 65% 79%</td>

</tr>

</tbody>

<tbody>

<tr>

<th colspan="3">[<span>binary-trees</span>](./binarytrees.html)</th>

<th colspan="3"></th>

</tr>

<tr>

<th>source</th>

<th>secs</th>

<th>mem</th>

<th>gz</th>

<th>cpu</th>

<th>cpu load</th>

</tr>

<tr>

<td>[<span>Go</span>](./program.php?test=binarytrees&lang=go&id=4)</td>

<td>28.80</td>

<td>434,632</td>

<td>654</td>

<td>109.58</td>

<td class="message">94% 95% 95% 97%</td>

</tr>

<tr>

<td>[<span>Java</span>](./program.php?test=binarytrees&lang=java&id=7)</td>

<td>8.34</td>

<td>893,008</td>

<td>835</td>

<td>28.20</td>

<td class="message">87% 79% 96% 81%</td>

</tr>

</tbody>

<tbody>

<tr>

<td>Go</td>

<td colspan="5" class="message">

go version go1.10 linux/amd64

</td>

</tr>

<tr>

<td>Java</td>

<td colspan="5" class="message">

java 9.0.1  
Java(TM) SE Runtime Environment (build 9.0.1+11)  
Java HotSpot(TM) 64-Bit Server VM (build 9.0.1+11, mixed mode)

</td>

</tr>

</tbody>

</table>

<nav>

*   [<span>vs C</span>](./compare.php?lang=go&lang2=gcc)
*   [<span>vs C++</span>](./compare.php?lang=go&lang2=gpp)
*   vs Java
*   [<span>vs JavaScript</span>](./compare.php?lang=go&lang2=node)
*   [<span>vs Python</span>](./compare.php?lang=go&lang2=python3)

</nav>

</section>

</article>

<footer>

<nav>

*   [<span>toy programs</span>](../why-measure-toy-benchmark-programs.html)
*   [<span>details</span>](../how-programs-are-measured.html)
*   [<span>conclusions</span>](../dont-jump-to-conclusions.html)

</nav>

<aside>

We want easy answers, but easy answers are often incomplete or wrong. You and I know, [<span>there's more we need to understand</span>](../index.html).

</aside>

</footer>

<script>window.ga=window.ga||function(){(ga.q=ga.q||[]).push(arguments)};ga.l=+new Date; ga('create', 'UA-37137205-1', 'auto'); ga('send', 'pageview');</script>
