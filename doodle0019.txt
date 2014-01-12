Title: [Emacs] C-n and C-p
Author: doubletony
Date: 28 August 2012

# Purpose

In most cases, C-n and C-p work well enough to go to next and previous line. However, when I read a long document,
I always press C-l after C-n or C-P to center the buffer. It may look much "geeky" when some one press keyboard frequently.
However, I'm a lazy one.  Why don't simply bind a new keystroke to do that?


# Solution

It's pretty straightforward. Since M-n and M-p are not bound to any command, I bind them to those two keys.

     ;; redefine the next line and previous line stuff

     (defun my-next-line ()
       (interactive)
       (next-line)
       (recenter)
       )


     (defun my-previous-line ()
       (interactive)
       (previous-line)
       (recenter)
       )


     (global-set-key (kbd "M-n") 'my-next-line)
     (global-set-key (kbd "M-p") 'my-previous-line)


