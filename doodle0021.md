Title: Bibtex: "I found no \\bibdata command"
Author: doubletony
Date: 16 September 2012

## Problem

I recently use emacs and auctex to write latex document. Something weirdly happening is that sometimes the bibtex doesn't work and bark with two errors:

> I found no \bibdata command---while reading file xxx.aux


> I found no \bibstyle command---while reading file xxx.aux

## Solution

Actually, the culprit is me. I forgot to close the preview pdf file and run the latex command. So the solution is simple, close the pdf, run latex, run bibtex, run latex twice.
