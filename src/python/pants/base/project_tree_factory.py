# Copyright 2016 Pants project contributors (see CONTRIBUTORS.md).
# Licensed under the Apache License, Version 2.0 (see LICENSE).

from pants.base.build_environment import get_buildroot
from pants.base.file_system_project_tree import FileSystemProjectTree
from pants.util.memo import memoized


@memoized
def get_project_tree(options):
  """Creates the project tree for build files for use in a given pants run."""
  pants_ignore = options.pants_ignore or []
  return FileSystemProjectTree(get_buildroot(), pants_ignore)
