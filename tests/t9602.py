#!/usr/bin/env python3
## Test handling of pathological tags
#
# This test was swiped from the git 1.8.1 tree, then modified to exercise
# a lifter directly rather than through git-cvsimport.
#

'''
This repository is for testing the ability to group revisions
correctly along tags and branches.  Here is its history:

  1.  The initial import (revision 1.1 of everybody) created a
      directory structure with a file named "default" in each dir:

            ./
              default
              sub1/default
                   subsubA/default
                   subsubB/default
              sub2/default
                   subsubA/default
              sub3/default

  2.  Then tagged everyone with T_ALL_INITIAL_FILES.

  3.  Then tagged everyone except sub1/subsubB/default with
      T_ALL_INITIAL_FILES_BUT_ONE.

  4.  Then created branch B_FROM_INITIALS on everyone.

  5.  Then created branch B_FROM_INITIALS_BUT_ONE on everyone except
      /sub1/subsubB/default.

  6.  Then committed modifications to two files: sub3/default, and
      sub1/subsubA/default.

  7.  Then committed a modification to all 7 files.

  8.  Then backdated sub3/default to revision 1.2, and
      sub2/subsubA/default to revision 1.1, and tagged with T_MIXED.

  9.  Same as 8, but tagged with -b to create branch B_MIXED.

  10. Switched the working copy to B_MIXED, and added
      sub2/branch_B_MIXED_only.  (That is why the RCS file is in
      sub2/Attic/ -- it never existed on trunk.)

  11. In one commit, modified default, sub1/default, and
      sub2/subsubA/default, on branch B_MIXED.

  12. Did "cvs up -A" on sub2/default, then in one commit, made a
      change to sub2/default and sub2/branch_B_MIXED_only.  So this
      commit should be spread between the branch and the trunk.

  13. Do "cvs up -A" to get everyone back to trunk, then make a new
      branch B_SPLIT on everyone except sub1/subsubB/default,v.

  14. Switch to branch B_SPLIT (see sub1/subsubB/default disappear)
      and commit a change that affects everyone except sub3/default.

  15. An hour or so later, "cvs up -A" to get sub1/subsubB/default
      back, then commit a change on that file, on trunk.  (It is
      important that this change happened after the previous commits
      on B_SPLIT.)

  16. Branch sub1/subsubB/default to B_SPLIT, then "cvs up -r B_SPLIT"
      to switch the whole working copy to the branch.

  17. Commit a change on B_SPLIT, to sub1/subsubB/default and
      sub3/default.
'''

# pylint: disable=multiple-imports
import sys, testlifter

testlifter.verbose += sys.argv[1:].count("-v")
cc = testlifter.ConvertComparison(stem="t9602", module="module")
cc.repo.retain = ("-k" in sys.argv[1:])
cc.compare_tree("branch", "master", True)
cc.compare_tree("branch", "vendorbranch", True)
cc.compare_tree("branch", "B_FROM_INITIALS", True)
cc.compare_tree("branch", "B_FROM_INITIALS_BUT_ONE", False)
cc.compare_tree("branch", "B_MIXED", True)
cc.compare_tree("branch", "B_SPLIT", True)
cc.compare_tree("tag", "vendortag", True)
cc.compare_tree("tag", "T_ALL_INITIAL_FILES", True)
cc.compare_tree("tag", "T_ALL_INITIAL_FILES_BUT_ONE", True)
cc.compare_tree("tag", "T_MIXED", True)
cc.cleanup()
