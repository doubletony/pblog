Title: [VirtualBox] VT-x is not available 
Author: doubletony
Date: 26 July 2012

## Quick fix

Make sure that the memory of your virtual machine is a bit smaller than
than 4GB (4096 MB). Otherwise, that's the reason why you get this
error message:

> "VT-x is not available.(VERR\_VMX\_NO\_VMX) "

To fix it, just set a smaller amount of memory (e.g. 3096 MB) and then
you will get rid of this error. (Please note that set the memory as
something like (4095 MB or 4000 MB) still won't work.)

If you already set the memory below to 4GB and still have this
problem, google a bit more then. ( sorry, this post is not helpful :( )
