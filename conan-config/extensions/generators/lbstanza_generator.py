
# Conan L.B.Stanza Generator
# https://docs.conan.io/2/reference/extensions/custom_generators.html

from conan.tools.files import save

# LBStanza Generator class
class LBStanzaGenerator:

    def __init__(self, conanfile):
        self._conanfile = conanfile

    def generate(self):
        self._conanfile.output.trace(f"---- LBStanzaGenerator.generate() ----")

        outfile = "stanza-z3-wrapper.proj"
        self._conanfile.output.trace(f"  opening output file \"{outfile}\"")

        # TODO read actual library file names from package
        with open(outfile, 'w') as f:
            # note: use '\n' for line terminator on all platforms
            f.write(f'package z3/Wrapper requires :\n')
            f.write(f'  dynamic-libraries:\n')
            f.write(f'    on-platform:\n')
            f.write(f'      windows: "./deps/libs/libz3.dll"\n')
            f.write(f'      linux: "./deps/libs/libz3.so"\n')
            f.write(f'      os-x: "./deps/libs/libz3.dylib"\n')
            f.write(f'  ccfiles: "./deps/libs/libz3.a"\n')
            f.write(f'  ccflags: "-I./deps/include"\n')

        #for dep, _ in self._conanfile.dependencies.items():
            #self._conanfile.output.trace(f"  dep: {dep.ref.name}/{dep.ref.version}")
        self._conanfile.output.trace("----")
