Title: A little hack
Author: doubletony
Date:  3 July 2012

## Emacs's **today** function

[pueblo](http://mikeshea.net/pueblo.html ) needs a header as follows to make every post nice.

    Title: A little hack
    Author: doubletony
	Date:  3 July 2012

However, manually typing the repeated information seems not reasonable
to me :) Thus, the first thing came up to me was how to avoid typing
the date. Thanks to
[this post](http://stackoverflow.com/questions/251908/how-can-i-insert-current-date-and-time-into-a-file-using-emacs
), I got my today function working nicely.

    (defun today ()
    "Insert string for today's date nicely formatted in American style,
    e.g. Sunday, September 17, 2000."
          (interactive)                 ; permit invocation in minibuffer
          (insert (format-time-string "%e %B %Y")))

## YASnippet

After this tiny progress, it's time to make the entire header info be
a snippet. [YASnippet](https://github.com/capitaomorte/yasnippet )
does have several snippet for markdown-mode. It should be easy to
follow the snippet of "*ol*" (order list) to create my snippet for
header. Shortly, I came up the following snippet:

    # name: head for post on pblog
    # key: head
    # --
    Title: ${}
    Author: doubletony
    Date: `(today)`

    $0
	




