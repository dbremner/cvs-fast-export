#!/usr/bin/env python3
## basic test for CVS master parsing

import sys, testlifter

testlifter.verbose += sys.argv[1:].count("-v")
repo = testlifter.CVSRepository("basic.repo")
repo.init()
repo.module("module")
co = repo.checkout("module", "basic.checkout")

co.write("README", "The quick brown fox jumped over the lazy dog.\n")
co.add("README")
co.commit("This is a sample commit")

repo.cleanup()

# end
