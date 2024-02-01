
# Conan L.B.Stanza Deployer
# https://docs.conan.io/2/reference/extensions/deployers.html
# https://docs.conan.io/2/examples/extensions/deployers/sources/custom_deployer_sources.html

from conan.tools.files import copy
#from conans.errors import ConanException
import os

# lbstanza_deployer function
def deploy(graph, output_folder: str, **kwargs):
    graph.root.conanfile.output.trace("---- lbstanza_deployer deploy() ----")

    # You can access your conanfile object with graph.root.conanfile
    for name, dep in graph.root.conanfile.dependencies.items():
        graph.root.conanfile.output.trace("  Dep is_direct={}: {}".format(name.direct, dep.ref))
        ### conanfile.py (stanza-z3/None):   Dep is_direct=True: z3/4.12.2

        #if dep.folders is None or dep.folders.source_folder is None:
        #    raise ConanException(f"Sources missing for {name} dependency.\n"
        #                          "This deployer needs the sources of every dependency present to work, either building from source, "
        #                          "or by using the 'tools.build:download_source' conf.")

        ### conanfile.py (stanza-z3/None):   copying conanfile.py (stanza-z3/None) / None / /home/jwatson/dev/lbstanza-z3/dependency_sources/z3/4.12.2
        graph.root.conanfile.output.trace(f"  copying {graph.root.conanfile} / {dep.folders.source_folder} / {os.path.join(output_folder, "dependency_sources", str(dep))}")
        # TODO cp libz3.a ./lib/
        breakpoint()

        if dep.package_type=='static-library' and (dep.package_path/'lib').exists():
            for x in (dep.package_path/'lib').iterdir():
                graph.root.conanfile.output.trace(f"  TODO cp {x} output/")

        #copy(graph.root.conanfile, "*", dep.folders.source_folder, os.path.join(output_folder, "dependency_sources", str(dep)))

    graph.root.conanfile.output.trace(f"output_folder = {output_folder}")
    # conanfile.py (stanza-z3/None): output_folder = /home/jwatson/dev/lbstanza-z3
