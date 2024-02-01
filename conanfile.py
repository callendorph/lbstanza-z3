# Stanza Z3 Shared/Static wrapped SLM package
#  This file contains the conan configurations
#  for building the Z3 library dependency
#  including building the wrapper. When finished,
#  this pre-built binary could be cached on
#  a conan-server or artifactory.

import sys
V = sys.version_info
if V[0] < 3:
  raise RuntimeError("Invalid Python Version - This script expects at least Python 3")

import os
import platform
from conan import ConanFile
from conan.tools.files import copy

required_conan_version = ">=2.0"

class StanzaZ3Recipe(ConanFile):
  """ Conan2 Recipe to create a Stanza/SLM deployment of the Z3 library.
  """
  name = "stanza-z3"
  package_type = "application"

  # Optional metadata
  author = "Carl Allendorph (callendorph@gmail.com)"
  url = "https://github.com/callendorph/lbstanza-z3"
  description = "Stanza Z3 Wrapper Builder"
  topics = ("stanza", "z3", "library management", "package management")

  # Binary configuration
  settings = "os", "arch", "compiler", "build_type"
  generators = "CMakeToolchain", "CMakeDeps"

  # Use `-o shared=True` on the commandline to
  #  build the dynamic version
  options = {"shared": [True, False], "fPIC": [True, False]}
  default_options = {"shared": False, "fPIC": True}

  implements = ["auto_shared_fpic"]

  def requirements(self):
    self.requires("z3/4.12.2")

  #def generate(self):
  #  g = self.python_requires["conan_lbstanza_utils"].module.LBStanzaGenerator
  #  g.generate(self, "z3/Wrapper", "stanza-z3.proj")

  # def build(self):
  #   self.output.trace("---- build() ----")
  #   v = self.python_requires["conan_lbstanza_utils"].module.myfunct()
  #   self.output.trace(f"  v = {v}")
  #   self.output.trace("----")

