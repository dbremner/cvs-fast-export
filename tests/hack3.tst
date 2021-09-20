#!/usr/bin/env python3
## Third example from the Hacking Guide

import sys, testlifter

testlifter.verbose += sys.argv[1:].count("-v")
repo = testlifter.CVSRepository("hack3.repo")
repo.init()
repo.module("module")
co = repo.checkout("module", "hack3.checkout")

co.write("foo.c", "The quick brown fox jumped over the lazy dog.\n")
co.add("foo.c")
co.write("bar.c", "Not an obfuscated C contest entry.\n")
co.add("bar.c")
co.commit("First commit")

co.write("bar.c", "The world will little note, nor long remember...\n")
co.commit("Second commit")

co.write("foo.c", "And now for something completely different.\n")
co.write("bar.c", "One is dead, one is mad, and I have forgotten.\n")
co.commit("Third commit")

co.branch("alternate")

co.write("foo.c", "Ceci n'est pas un sourcefile.\n")
co.commit("Fourth commit")

co.write("foo.c", "Twas brillig, and the slithy toves...\n")
co.write("bar.c", "...did gyre and gimble in the wabe.\n")
co.commit("Fifth commit")

repo.cleanup()

# end
