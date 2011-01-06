# Copyright 2011 Josh Kearney

"""Pre-commit hook plugin for Bazaar"""

import subprocess

from bzrlib import branch
from bzrlib import errors


CHECK_PEP8 = True
CHECK_TESTS = False


def pre_commit_hook(
    local,
    master,
    old_revno,
    old_revid,
    future_revno,
    future_revid,
    tree_delta,
    future_tree):
    """Ensure code is PEP8 compliant and all unit tests pass."""
    if CHECK_PEP8:
        if subprocess.call([
            "pep8",
            "--repeat",
            "--show-source",
            "--show-pep8",
            "./nova"]):
            raise errors.BzrError("Code is not PEP8 compliant.")

    if CHECK_TESTS:
        if subprocess.call("./run_tests.sh"):
            raise errors.BzrError("Unit tests did not pass.")


branch.Branch.hooks.install_named_hook(
    "pre_commit",
    pre_commit_hook,
    "pre_commit hook")
