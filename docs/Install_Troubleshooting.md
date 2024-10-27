## Installation Troubleshooting

Here are some tips if your installation fails.

One of the first places to start is by updating all of your gems:

`bundle update`

You can also try updating RubyGems:

`gem update --system`


The WDM library can be problematic on newer versions of Ruby. For Ruby 3.1, the following was needed to install WDM:

`gem install wdm -v 0.1.1 -- --with-cflags=-Wno-implicit-function-declaration`
