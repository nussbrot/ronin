Rōnin
=====

A straightforward but powerful build system based on [Ninja](https://ninja-build.org/) and
[Python](https://www.python.org/), suitable for projects both big and small.

Rōnin comes with [frustration-free packaging](https://en.wikipedia.org/wiki/Wrap_rage). Let's build
all the things!

"Based on Python" means that not only is it written in Python, but also it uses Python as the DSL
for build scripts. Many build systems invent their own DSLs, but Rōnin intentionally uses a language
that already exists. Note that you _don't_ need to be an expert in Python to use Rōnin, but the
power is there if you need it.

Currently supported out-of-the-box: all [gcc](https://gcc.gnu.org/) languages,
[Vala](https://wiki.gnome.org/Projects/Vala) (and [Genie](https://wiki.gnome.org/Projects/Genie)),
[Rust](https://www.rust-lang.org/),
[pkg-config](https://www.freedesktop.org/wiki/Software/pkg-config/),
[sdl2-config](https://wiki.libsdl.org/Installation), and
[binutils](https://sourceware.org/binutils/docs/binutils/).

Guiding lights:

1. **Powerful does not have to mean hard to use**: _optional_ auto-configuration with sensible,
   _overridable_ defaults.
2. **Complex does not have to mean complicated**: handle cross-compilation and other
   multi-configuration builds in a single script with minimal duplication of effort.

Design principles:

1. Pour some sugar on me: make common tasks easier with sweet utility functions. But make sure
   that sugar is optional, allowing the script to be more verbose when more control is necessary. 
2. Don't hide functionality behind complexity: the architecture should be straightforward. For
   example, if the user wants to manipulate a compiler command line, let them do it easily. Too many
   build systems bungle this and make it either impossible or very difficult to do something that
   would be trivial using a shell script.
3. Don't reinvent wheels: if Python or Ninja do something for us, use it. The build script is a
   plain Python program without any unnecessary cleverness. The generated Ninja file looks like
   something you could have created manually.

User Manual
-----------

[Quickstart here](https://github.com/tliron/ronin/wiki/Quick-Start).

[Full documentation on the wiki](https://github.com/tliron/ronin/wiki).

(API docs coming soon!)


FAQ
---

* _Do we really need another build system?_ Yes. The other existing ones have convoluted
  architectures, impossible to opt-out-from automatic features, or are otherwise hostile to
  straightforward hacking. After so much wasted time fighting build systems to make them work for
  us, the time came to roll out a new one that does it right.
* _Python is too hard. Why not create a simpler DSL?_ Others have done it, and it seems that the
  costs outweigh the benefits. Making a new language is not trivial. Making a _robust_ language
  could take years of effort. Python is here right now, with a huge ecosystem of libraries and
  tools. Yes, it introduces a learning curve, but getting familiar with Python is useful for so
  many practical reasons beyond writing build scripts for Rōnin. That said, if someone wants to
  contribute a simple DSL as an optional extra, we will consider!
* _Why require Ninja, a binary, instead of building everything in 100% Python?_ Because it's silly
  to reinvent wheels, especially when the wheels are so good. Ninja is a one-trick pony that does
  its job extremely well. But it's just too low-level for most users, hence the need for a frontend.
* _Why not Python 3?_ Many, many deployed systems are still locked in Python 2 for various reasons.
  We want to be able to build on them.
* _Why Ninja? It's already yesterday's news! There are even faster builders._ Eh, if you ignore the
  initial configuration phase, and are properly multithreading your build (`-j` flag in Make), then
  the time you wait for things to be done ends up depending on your compiler, not the build system.
  Ninja was chosen because of its marvelous minimalism, not its speed. Ninja is actually 
  [not much](http://david.rothlis.net/ninja-benchmark/) 
  [faster](http://hamelot.io/programming/make-vs-ninja-performance-comparison/)
  than Make. However, [tup](http://gittup.org/tup/) is interesting.


Similar Projects
----------------

* [emk](https://github.com/kmackay/emk): "A Python-based build tool."
* [CMake Ninja Generator](https://cmake.org/cmake/help/v3.0/generator/Ninja.html): "Generates
  build.ninja files (experimental)."
* [Craftr](https://craftr.net/): "Craftr is a next generation build system based on Ninja and Python
  that features modular and cross-platform build definitions at the flexibility of a Python script
  and provides access to multiple levels of build automation abstraction."
* [Meson](http://mesonbuild.com/): "Meson is an open source build system meant to be both extremely
  fast, and, even more importantly, as user friendly as possible."
* [Waf](https://waf.io/): "The meta build system."
