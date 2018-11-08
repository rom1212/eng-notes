<header>

### [The <small>Computer Language</small>  
Benchmarks Game](https://benchmarksgame-team.pages.debian.net/benchmarksgame/)

</header>

<article>

<div>

# Go versus Java fastest programs

<aside>

<nav>

*   [<span>vs C</span>](../faster/go-gcc.html)
*   [<span>vs C++</span>](../faster/go-gpp.html)
*   vs Java
*   [<span>vs JavaScript</span>](../faster/go-node.html)
*   [<span>vs Python</span>](../faster/go-python3.html)

</nav>

</aside>

</div>

<section>

<div>

## by faster benchmark performance

</div>

<table>

<tbody>

<tr>

<th colspan="3">[<span>pidigits</span>](../performance/pidigits.html)</th>

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

<td>[<span>Go</span>](../program/pidigits-go-3.html)</td>

<td class="best">2.04</td>

<td>8,964</td>

<td>603</td>

<td>2.04</td>

<td class="message">0% 83% 18% 0%</td>

</tr>

<tr>

<td>[<span>Java</span>](../program/pidigits-java-2.html)</td>

<td>3.13</td>

<td>37,324</td>

<td>938</td>

<td>3.35</td>

<td class="message">98% 5% 3% 3%</td>

</tr>

</tbody>

<tbody>

<tr>

<th colspan="3">[<span>mandelbrot</span>](../performance/mandelbrot.html)</th>

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

<td>[<span>Go</span>](../program/mandelbrot-go-4.html)</td>

<td class="best">5.47</td>

<td>31,040</td>

<td>905</td>

<td>21.73</td>

<td class="message">99% 99% 100% 99%</td>

</tr>

<tr>

<td>[<span>Java</span>](../program/mandelbrot-java-2.html)</td>

<td>6.96</td>

<td>76,748</td>

<td>796</td>

<td>27.07</td>

<td class="message">98% 98% 96% 98%</td>

</tr>

</tbody>

<tbody>

<tr>

<th colspan="3">[<span>fasta</span>](../performance/fasta.html)</th>

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

<td>[<span>Go</span>](../program/fasta-go-3.html)</td>

<td class="best">2.06</td>

<td>3,432</td>

<td>1358</td>

<td>5.85</td>

<td class="message">87% 30% 84% 84%</td>

</tr>

<tr>

<td>[<span>Java</span>](../program/fasta-java-5.html)</td>

<td>2.32</td>

<td>42,556</td>

<td>2473</td>

<td>6.24</td>

<td class="message">73% 85% 49% 63%</td>

</tr>

</tbody>

<tbody>

<tr>

<th colspan="3">[<span>spectral-norm</span>](../performance/spectralnorm.html)</th>

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

<td>[<span>Go</span>](../program/spectralnorm-go-4.html)</td>

<td class="best">3.95</td>

<td>2,664</td>

<td>548</td>

<td>15.70</td>

<td class="message">99% 99% 100% 100%</td>

</tr>

<tr>

<td>[<span>Java</span>](../program/spectralnorm-java-2.html)</td>

<td>4.27</td>

<td>32,960</td>

<td>950</td>

<td>16.41</td>

<td class="message">95% 97% 98% 96%</td>

</tr>

</tbody>

<tbody>

<tr>

<th colspan="3">[<span>n-body</span>](../performance/nbody.html)</th>

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

<td>[<span>Go</span>](../program/nbody-go-3.html)</td>

<td class="best">21.00</td>

<td>1,536</td>

<td>1200</td>

<td>21.00</td>

<td class="message">100% 0% 0% 1%</td>

</tr>

<tr>

<td>[<span>Java</span>](../program/nbody-java-4.html)</td>

<td>22.00</td>

<td>32,496</td>

<td>1489</td>

<td>22.07</td>

<td class="message">1% 100% 0% 1%</td>

</tr>

</tbody>

<tbody>

<tr>

<th colspan="3">[<span>fannkuch-redux</span>](../performance/fannkuchredux.html)</th>

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

<td>[<span>Go</span>](../program/fannkuchredux-go-1.html)</td>

<td class="best">17.83</td>

<td>1,480</td>

<td>900</td>

<td>71.04</td>

<td class="message">100% 100% 100% 100%</td>

</tr>

<tr>

<td>[<span>Java</span>](../program/fannkuchredux-java-1.html)</td>

<td>17.91</td>

<td>31,560</td>

<td>1282</td>

<td>70.25</td>

<td class="message">99% 98% 99% 97%</td>

</tr>

</tbody>

<tbody>

<tr>

<th colspan="3">[<span>reverse-complement</span>](../performance/revcomp.html)</th>

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

<td>[<span>Go</span>](../program/revcomp-go-2.html)</td>

<td>4.00</td>

<td>826,976</td>

<td>611</td>

<td>4.15</td>

<td class="message">5% 13% 87% 1%</td>

</tr>

<tr>

<td>[<span>Java</span>](../program/revcomp-java-8.html)</td>

<td>3.31</td>

<td>626,956</td>

<td>2183</td>

<td>7.44</td>

<td class="message">56% 60% 83% 45%</td>

</tr>

</tbody>

<tbody>

<tr>

<th colspan="3">[<span>k-nucleotide</span>](../performance/knucleotide.html)</th>

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

<td>[<span>Go</span>](../program/knucleotide-go-3.html)</td>

<td>13.06</td>

<td>148,316</td>

<td>1722</td>

<td>47.92</td>

<td class="message">90% 89% 95% 93%</td>

</tr>

<tr>

<td>[<span>Java</span>](../program/knucleotide-java-1.html)</td>

<td>8.66</td>

<td>385,768</td>

<td>1812</td>

<td>26.52</td>

<td class="message">76% 81% 74% 76%</td>

</tr>

</tbody>

<tbody>

<tr>

<th colspan="3">[<span>regex-redux</span>](../performance/regexredux.html)</th>

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

<td>[<span>Go</span>](../program/regexredux-go-2.html)</td>

<td>28.89</td>

<td>338,812</td>

<td>802</td>

<td>60.70</td>

<td class="message">41% 51% 48% 70%</td>

</tr>

<tr>

<td>[<span>Java</span>](../program/regexredux-java-3.html)</td>

<td>10.52</td>

<td>637,380</td>

<td>929</td>

<td>31.89</td>

<td class="message">75% 80% 77% 72%</td>

</tr>

</tbody>

<tbody>

<tr>

<th colspan="3">[<span>binary-trees</span>](../performance/binarytrees.html)</th>

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

<td>[<span>Go</span>](../program/binarytrees-go-4.html)</td>

<td>28.56</td>

<td>466,636</td>

<td>654</td>

<td>109.05</td>

<td class="message">96% 95% 96% 95%</td>

</tr>

<tr>

<td>[<span>Java</span>](../program/binarytrees-java-7.html)</td>

<td>8.28</td>

<td>982,224</td>

<td>835</td>

<td>27.19</td>

<td class="message">79% 86% 83% 83%</td>

</tr>

</tbody>

<tbody>

<tr>

<td>Go</td>

<td colspan="5" class="message">

go version go1.11 linux/amd64

</td>

</tr>

<tr>

<td>Java</td>

<td colspan="5" class="message">

openjdk 11 2018-09-25  
OpenJDK Runtime Environment 18.9 (build 11+28)  
OpenJDK 64-Bit Server VM 18.9 (build 11+28, mixed mode)

</td>

</tr>

</tbody>

</table>

<nav>

[all other Go programs & measurements](../measurements/go.html)

</nav>

</section>

</article>

<footer>

<nav>

*   [<span>Why toy programs?</span>](../why-measure-toy-benchmark-programs.html)
*   [<span>How programs are measured</span>](../how-programs-are-measured.html)
*   [<span>The Ultimate Benchmark</span>](../dont-jump-to-conclusions.html)

</nav>

<aside>

We want easy answers, but easy answers are often incomplete or wrong. You and I know, there's more we need to understand.

</aside>

</footer>
