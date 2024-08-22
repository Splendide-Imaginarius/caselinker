# CaseLinker

CaseLinker is a tool for generating symlinks to simulate a case-insensitive filesystem. Many Windows games assume case-insensitivity; you can use CaseLinker to facilitate playing Windows games on case-sensitive filesystems like Linux and macOS typically use.

## Instructions

First, you'll need the source code for the game in question, e.g. the Ruby source code for RPG Maker games.

Then do the following:

```
./caselinker-convert.sh ./path/to/source/code/folder
./caselinker.py --source-code ./path/to/source/code/folder --assets ./path/to/source/code/folder
```

The game now should work on Linux.

## How does CaseLinker compare to [cicpoffs](https://github.com/adlerosn/cicpoffs)?

* CaseLinker is probably faster in-game. Resolving symlinks is typically faster than proxying through FUSE, and CaseLinker only incurs overhead for assets that have a case error. However, I've never actually tried to compare them on a benchmark. If you have benchmark results, please let me know.
* CaseLinker requires a preprocessing step. cicpoffs runs your game immediately.
* CaseLinker assumes that games do sane things. As Alan Turing famously proved, CaseLinker will never work with 100% of arbitrary games that do arbitrary things to decide where to look for assets. cicpoffs should work even with games that do insane things. However, if you find a real-world game where CaseLinker doesn't work and cicpoffs does, please file a bug so I can look into it.

## How does CaseLinker compare to [mkxp-z](https://github.com/mkxp-z/mkxp-z)'s path cache?

Basically the same as above, subject to the following:

* mkxp-z's path cache shouldn't adversely affect run-time speed once the game has booted like cicpoffs does, but it does increase the game's boot time significantly. CaseLinker should yield much quicker boot times than mkxp-z's path cache.
* mkxp-z's path cache happens to sidestep a [PhysicsFS multithreading bottleneck](https://github.com/icculus/physfs/issues/13). Thus, games that load assets on background threads will probably be much faster in-game with mkxp-z's path cache than with CaseLinker.

## Does CaseLinker magically let me play Windows games on Linux without Wine?

You'll still need to port whatever engine your games are using to run on Linux. CaseLinker may simplify the engine porting effort by avoiding the need to emulate case-insensitive paths inside the engine.

## Which games run with CaseLinker?

I'm intending to set up a proper compatibility list in the future, but in general, games that use RPG Maker XP / VX / VX Ace have a good chance of working via mkxp-z.

## Credits

Copyright 2023-2024 Splendide Imaginarius.

This is not a license requirement, but if you use CaseLinker for a project such as a game port or remaster, it would be greatly appreciated if you credit me. Example credits: "Case errors were fixed with CaseLinker by Splendide Imaginarius." Linking back to this Git repository would also be greatly appreciated.

CaseLinker is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

CaseLinker is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with CaseLinker. If not, see [https://www.gnu.org/licenses/](https://www.gnu.org/licenses/).

There appears to be [some prior art](https://old.reddit.com/r/linuxquestions/comments/z9sdhj/is_it_possible_to_create_a_symbolic_link_to_a/) (which I didn't know about when I started working on CaseLinker) from Greevar.
