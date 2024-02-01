
# Conan L.B.Stanza Generator
# https://docs.conan.io/2/reference/extensions/custom_generators.html

from conan.tools.files import save

# LBStanza Generator class
class LBStanzaGenerator:

    def __init__(self, conanfile):
        self._conanfile = conanfile

    def generate(self):
        self._conanfile.output.trace(f"---- LBStanzaGenerator.generate() ----")
        
        #self.output.trace(f"  opening output file \"{outfile}\"")
        
        for dep, _ in self._conanfile.dependencies.items():
            self._conanfile.output.trace(f"  dep: {dep.ref.name}/{dep.ref.version}")
            self._conanfile.output.trace(f"  TODO: project_dir paths for dep")
              # package z3/Wrapper requires :
              #   dynamic-libraries:
              #     on-platform:
              #       windows: "./build/content/libz3.dll"
              #       linux: "./build/content/libz3.so"
              #       os-x: "./build/content/libz3.dylib"
              #   ccfiles: "./build/content/libz3.a"
              #   ccflags: "-I./build/content/include"
        self._conanfile.output.trace("----")
