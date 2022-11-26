

### [The Computer Language  <br>22.05 Benchmarks Game](https://benchmarksgame-team.pages.debian.net/benchmarksgame/index.html)

Fastest cpu secs Go versus Java
===============================

* [vs C# .NET](../fastest/go-csharpcore.html)
* [vs C++](../fastest/go-gpp.html)
* vs Java
* [vs Python](../fastest/go-python3.html)
* [vs Rust](../fastest/go-rust.html)

Always look at the source code.

If the fastest programs are hand-written vector instructions, does the host language matter? You might be more interested in the less optimised programs — more cpu seconds, less gz source code.

| [fannkuch-redux](../performance/fannkuchredux.html) |     |     |     |
| --- | --- | --- | --- |
| source | mem | gz  | cpu |
| [Go #3](../program/fannkuchredux-go-3.html) | 2,260 | 969 | 32.88 |
| [Java #3](../program/fannkuchredux-java-3.html) | 35,324 | 1257 | 41.17 |
| [Java](../program/fannkuchredux-java-1.html) | 35,824 | 1282 | 41.74 |
| [Java #2](../program/fannkuchredux-java-2.html) | 34,244 | 514 | 44.98 |
| [Go](../program/fannkuchredux-go-1.html) | 2,956 | 900 | 47.36 |
| [Go #2](../program/fannkuchredux-go-2.html) | 11,316 | 896 | 47.56 |
| [n-body](../performance/nbody.html) |     |     |     |
| source | mem | gz  | cpu |
| [Go #3](../program/nbody-go-3.html) | 1,136 | 1200 | 6.38 |
| [Go](../program/nbody-go-1.html) | 1,136 | 1310 | 6.58 |
| [Java #5](../program/nbody-java-5.html) | 34,252 | 1429 | 6.79 |
| [Java #4](../program/nbody-java-4.html) | 34,076 | 1489 | 6.79 |
| [Go #2](../program/nbody-go-2.html) | 1,132 | 1215 | 6.94 |
| [Java #3](../program/nbody-java-3.html) | 34,612 | 1430 | 7.50 |
| [Java #2](../program/nbody-java-2.html) | 34,704 | 1424 | 7.50 |
| [Java](../program/nbody-java-1.html) | 37,380 | 1430 | 7.83 |
| [spectral-norm](../performance/spectralnorm.html) |     |     |     |
| source | mem | gz  | cpu |
| [Go](../program/spectralnorm-go-1.html) | 2,452 | 411 | 5.33 |
| [Go #4](../program/spectralnorm-go-4.html) | 1,952 | 548 | 5.67 |
| [Go #2](../program/spectralnorm-go-2.html) | 1,420 | 668 | 5.68 |
| [Java #3](../program/spectralnorm-java-3.html) | 38,428 | 756 | 5.94 |
| [Java](../program/spectralnorm-java-1.html) | 37,288 | 514 | 9.76 |
| [Java #2](../program/spectralnorm-java-2.html) | 37,368 | 950 | 10.07 |
| [mandelbrot](../performance/mandelbrot.html) |     |     |     |
| source | mem | gz  | cpu |
| [Go #4](../program/mandelbrot-go-4.html) | 33,812 | 905 | 14.85 |
| [Go #3](../program/mandelbrot-go-3.html) | 34,028 | 894 | 14.91 |
| [Java #4](../program/mandelbrot-java-4.html) | 66,304 | 660 | 16.16 |
| [Java #2](../program/mandelbrot-java-2.html) | 68,860 | 796 | 16.21 |
| [Java #6](../program/mandelbrot-java-6.html) | 67,432 | 802 | 16.92 |
| [Go](../program/mandelbrot-go-1.html) | 32,600 | 823 | 19.58 |
| [Go #2](../program/mandelbrot-go-2.html) | 33,196 | 837 | 27.07 |
| [Go #6](../program/mandelbrot-go-6.html) | 32,764 | 700 | 27.25 |
| [Java](../program/mandelbrot-java-1.html) | 34,252 | 665 | 27.75 |
| [Java #3](../program/mandelbrot-java-3.html) | 69,200 | 903 | 29.18 |
| [pidigits](../performance/pidigits.html) |     |     |     |
| source | mem | gz  | cpu |
| [Java #3](../program/pidigits-java-3.html) | 35,700 | 764 | 0.82 |
| [Go #4](../program/pidigits-go-4.html) | 8,732 | 683 | 0.87 |
| [Go #3](../program/pidigits-go-3.html) | 9,320 | 603 | 1.18 |
| [Go](../program/pidigits-go-1.html) | 9,496 | 708 | 1.21 |
| [Java #2](../program/pidigits-java-2.html) | 38,328 | 938 | 1.53 |
| [Go #2](../program/pidigits-go-2.html) | 9,032 | 733 | 1.59 |
| [Go #8](../program/pidigits-go-8.html) | 9,924 | 720 | 2.54 |
| [Go #7](../program/pidigits-go-7.html) | 8,620 | 696 | 5.05 |
| [Java](../program/pidigits-java-1.html) | 513,728 | 800 | 8.94 |
| [regex-redux](../performance/regexredux.html) |     |     |     |
| source | mem | gz  | cpu |
| [Go #5](../program/regexredux-go-5.html) | 306,476 | 810 | 5.97 |
| [Java](../program/regexredux-java-1.html) | 924,116 | 868 | 17.12 |
| [Java #6](../program/regexredux-java-6.html) | 728,332 | 740 | 17.16 |
| [Java #3](../program/regexredux-java-3.html) | 741,028 | 929 | 17.34 |
| [Go #4](../program/regexredux-go-4.html) | 355,844 | 829 | 34.99 |
| [Go #3](../program/regexredux-go-3.html) | 358,472 | 829 | 67.28 |
| [Go](../program/regexredux-go-1.html) | 297,048 | 741 | 68.45 |
| [fasta](../performance/fasta.html) |     |     |     |
| source | mem | gz  | cpu |
| [Java #4](../program/fasta-java-4.html) | 36,800 | 1524 | 3.41 |
| [Java #6](../program/fasta-java-6.html) | 42,416 | 2543 | 3.52 |
| [Go](../program/fasta-go-1.html) | 1,112 | 1053 | 3.64 |
| [Go #2](../program/fasta-go-2.html) | 10,980 | 1404 | 3.84 |
| [Go #3](../program/fasta-go-3.html) | 3,168 | 1358 | 3.98 |
| [Java #5](../program/fasta-java-5.html) | 42,532 | 2473 | 4.14 |
| [Java #2](../program/fasta-java-2.html) | 36,812 | 1257 | 4.46 |
| [k-nucleotide](../performance/knucleotide.html) |     |     |     |
| source | mem | gz  | cpu |
| [Java](../program/knucleotide-java-1.html) | 349,544 | 1812 | 16.17 |
| [Java #6](../program/knucleotide-java-6.html) | 343,684 | 1607 | 25.67 |
| [Java #3](../program/knucleotide-java-3.html) | 344,652 | 1635 | 25.73 |
| [Go #7](../program/knucleotide-go-7.html) | 159,432 | 1607 | 28.49 |
| [Go #6](../program/knucleotide-go-6.html) | 149,712 | 1590 | 29.40 |
| [Go #4](../program/knucleotide-go-4.html) | 144,528 | 1543 | 30.22 |
| [Go #3](../program/knucleotide-go-3.html) | 149,984 | 1722 | 30.25 |
| [Java #4](../program/knucleotide-java-4.html) | 199,824 | 1882 | 37.48 |
| [Java #5](../program/knucleotide-java-5.html) | 210,368 | 2219 | 43.27 |
| [reverse-complement](../performance/revcomp.html) |     |     |     |
| source | mem | gz  | cpu |
| [Go #2](../program/revcomp-go-2.html) | 826,796 | 611 | 1.94 |
| [Go #3](../program/revcomp-go-3.html) | 826,544 | 605 | 2.13 |
| [Go #5](../program/revcomp-go-5.html) | 1,483,756 | 996 | 2.26 |
| [Go #6](../program/revcomp-go-6.html) | 1,289,572 | 1338 | 2.48 |
| [Java #8](../program/revcomp-java-8.html) | 665,804 | 2183 | 3.49 |
| [Java #6](../program/revcomp-java-6.html) | 2,024,016 | 752 | 4.15 |
| [Java #5](../program/revcomp-java-5.html) | 1,088,392 | 1108 | 4.92 |
| [Java #3](../program/revcomp-java-3.html) | 1,170,232 | 1722 | 5.09 |
| [Java #4](../program/revcomp-java-4.html) | 1,881,900 | 651 | 5.41 |
| [Java #7](../program/revcomp-java-7.html) | 1,030,892 | 1647 | 23.16 |
| [Go](../program/revcomp-go-1.html) |     | Failed |     |
| [binary-trees](../performance/binarytrees.html) |     |     |     |
| source | mem | gz  | cpu |
| [Java #3](../program/binarytrees-java-3.html) | 2,106,820 | 540 | 5.19 |
| [Java #6](../program/binarytrees-java-6.html) | 2,093,916 | 529 | 5.35 |
| [Java #4](../program/binarytrees-java-4.html) | 2,079,388 | 840 | 5.44 |
| [Java #2](../program/binarytrees-java-2.html) | 1,877,464 | 552 | 5.45 |
| [Java #7](../program/binarytrees-java-7.html) | 2,460,388 | 835 | 7.73 |
| [Go #6](../program/binarytrees-go-6.html) | 411,424 | 611 | 29.23 |
| [Go #2](../program/binarytrees-go-2.html) | 632,396 | 666 | 48.67 |
| [Go #3](../program/binarytrees-go-3.html) | 328,700 | 799 | 50.09 |
| [Go #5](../program/binarytrees-go-5.html) | 394,800 | 950 | 50.52 |
| [Go](../program/binarytrees-go-1.html) | 240,292 | 482 | 51.02 |
| [Go #7](../program/binarytrees-go-7.html) | 259,088 | 525 | 51.41 |
| Go  | go version go1.18 linux/amd64 |     |     |
| Java | openjdk 18 2022-03-22  <br>OpenJDK Runtime Environment  <br>(build 18+36-2087)  <br>OpenJDK 64-Bit Server VM  <br>(build 18+36-2087,  <br>mixed mode, sharing) |     |     |

* [all Go programs & measurements](../measurements/go.html)
* [all Java programs & measurements](../measurements/java.html)

* [How programs are measured](../how-programs-are-measured.html)
