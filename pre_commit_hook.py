#   Copyright 2011 Josh Kearney
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

"""Pre-commit hook plugin for Bazaar"""

import subprocess

from bzrlib import branch
from bzrlib import errors


RUN_PEP8 = True
RUN_TESTS = False

PEP8_PATH = "./nova"
UNIT_TESTS = "./run_tests.sh"


def pre_commit_hook(local, master, old_revno, old_revid, future_revno,
                    future_revid, tree_delta, future_tree):
    """Ensure code is PEP8 compliant and all unit tests pass."""
    if RUN_PEP8:
        if subprocess.call(["pep8", "--repeat", "--show-source", PEP8_PATH]):
            raise errors.BzrError("Code is not PEP8 compliant.")

    if RUN_TESTS:
        if subprocess.call(UNIT_TESTS):
            raise errors.BzrError("Unit tests did not pass.")


branch.Branch.hooks.install_named_hook("pre_commit", pre_commit_hook,
                                       "pre_commit hook")
