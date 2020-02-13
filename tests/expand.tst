#!/usr/bin/env python
## Test keyword expansion

import sys, testlifter

testlifter.verbose += sys.argv[1:].count("-v")
repo = testlifter.CVSRepository("expand.repo")
repo.init()
repo.module("module")
co = repo.checkout("module", "expand.checkout")

co.write("README", "$Revision$ should expand to something with 1.1 in it.\n")
co.add("README")
co.commit("This is a sample commit")

co.write("README", "$Revision$ should expand to something with 1.2 in it.\n")
co.commit("This is another sample commit")

co.write("README", "$Revision: 1.3 $ should expand to something with 1.3 in it.\n")
co.commit("Yet another sample commit")

repo.cleanup()

# end
