Gravatar-Cycler
===============

Cycle through your different Gravatar.com images, changing your default avatar on interval.


Usage
-----

    cycle-gravatars.py -e <emailaddress> -p <password> -d <delayinseconds>
    
or

    cycle-gravatars.py --email=<emailaddress> -password=<password> -delay=<delayinseconds>

&lt;emailaddress&gt; and &lt;password&gt; are your [Gravatar.com](http://gravatar.com) login and password, and are required.

&lt;delayinseconds&gt; is optional, defaulting to 300 (5 minutes).

The script will run until it dies, or you kill it with Control-C.


Dependencies
------------

You may need to install the _libgravatar_ Python package:

        pip install libgravatar

[Read this](http://dabapps.com/blog/introduction-to-pip-and-virtualenv-python/) for more info on installing packages.


Why?
----

The chat board at my work uses [Gravatar.com](http://gravatar.com) for our profile images. I wrote this to have some fun with it. Every few minutes, I have my profile image choose between four images that I already uploaded to Gravatar.com - different rotations of my avatar.

This doesn't solve any of the world's problems - it just allows you to have some random fun.


PROTIP
------

When someone asks why your avatar keeps changing, look confused and say that you have no idea what they're talking about, and suggest "maybe it's a bug?".


Disclamer
---------

Use at your own risk. At the time of this writing, this doesn't appear to violate any terms of service in [Gravatar's Developer Resources](http://en.gravatar.com/site/implement/). I'm a Python newb, so this is most likely terrible code, with almost zero error-handling. I'll update it at some point.


One More Disclaimer
-------------------

I often say "I'll update it at some point", and then never look back.
