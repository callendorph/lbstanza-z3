
# Conan L.B.Stanza Utilities - https://lbstanza.org/ https://jitx.com/

# This is a Conan "python_requires" package
# This package does not create binaries, only python support files
# https://docs.conan.io/2/reference/extensions/python_requires.html

# https://docs.conan.io/2/reference/extensions/custom_generators.html
# https://docs.conan.io/2/reference/extensions/deployers.html
# https://docs.conan.io/2/examples/extensions/deployers/sources/custom_deployer_sources.html

from conan import ConanFile
from conan.tools.files import save

# self.python_requires["conan_lbstanza_utils"].module.myvar
myvar = 123

# self.python_requires["conan_lbstanza_utils"].module.myfunct()
def myfunct():
    return 234

# python_require wrapper class
class ConanLBStanzaUtils(ConanFile):
    name = "conan_lbstanza_utils"
    version = "0.0"
    package_type = "python-require"


# LBStanza Generator class
class LBStanzaGenerator:
    
    def generate(self, pkgname, outfile):
        self.output.trace(f"---- LBStanzaGenerator.generate({pkgname}, {outfile}) ----")
        
        self.output.trace(f"  opening output file \"{outfile}\"")
        
        for dep, _ in self.dependencies.items():
            self.output.trace(f"  dep: {dep.ref.name}/{dep.ref.version}")
            self.output.trace(f"  TODO: project_dir paths for dep")
              # package z3/Wrapper requires :
              #   dynamic-libraries:
              #     on-platform:
              #       windows: "./build/content/libz3.dll"
              #       linux: "./build/content/libz3.so"
              #       os-x: "./build/content/libz3.dylib"
              #   ccfiles: "./build/content/libz3.a"
              #   ccflags: "-I./build/content/include"
        self.output.trace("----")


# lbstanza_deployer function
def deploy(graph, output_folder: str, **kwargs):
    graph.root.conanfile.output.trace("---- lbstanza_deployer deploy() ----")

    # You can access your conanfile object with graph.root.conanfile
    for require, dependency in graph.root.conanfile.dependencies.items():
         graph.root.conanfile.output.trace("  Dependency is direct={}: {}".format(require.direct, dependency.ref))
         # EXAMPLE copy(graph.root.conanfile, "*", dep.folders.source_folder, os.path.join(output_folder, "dependency_sources", str(dep)))

    graph.root.conanfile.output.trace("----")
    graph.root.conanfile.output.trace(f"graph = {graph}")
    graph.root.conanfile.output.trace(f"output_folder = {output_folder}")
    graph.root.conanfile.output.trace(f"kwargs = {kwargs}")
    graph.root.conanfile.output.trace("----")

    graph.root.conanfile.output.trace("----")
