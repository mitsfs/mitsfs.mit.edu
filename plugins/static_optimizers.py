#coding:utf-8

import subprocess
from cactus.static.external import External


class ClosureJSOptimizer(External):
    supported_extensions = ('js',)
    output_extension = 'js'

    def _run(self):
        subprocess.check_call([
            'closure-compiler',
            '--language_in', 'ECMASCRIPT5',
            '--js', self.src,
            '--js_output_file', self.dst,
            '--compilation_level', 'SIMPLE_OPTIMIZATIONS'
])


class YUIJSOptimizer(External):
    supported_extensions = ('js',)
    output_extension = 'js'

    def _run(self):
        subprocess.check_call([
            'yui-compressor',
            '--type', 'js',
            '-o', self.dst,
            self.src,
        ])


class YUICSSOptimizer(External):
    supported_extensions = ('css',)
    output_extension = 'css'

    def _run(self):
        subprocess.check_call([
            'yui-compressor',
            '--type', 'css',
            '-o', self.dst,
            self.src,
])

def preBuild(site):
    """
    Registers optimizers as requested by the configuration.
    Be sure to read the plugin to understand and use it.
    """

    # Inspect the site configuration, and retrieve an `optimize` list.
    # This lets you configure optimization selectively.
    # You may want to use one configuration for staging with no optimizations, and one
    # configuration for production, with all optimizations.
    optimize = site.config.get("optimize", [])

    if "js" in optimize:
        # If `js` was found in the `optimize` key, then register our JS optimizer.
        # This uses closure, but you could use cactus.contrib.external.yui.YUIJSOptimizer!
        site.external_manager.register_optimizer(ClosureJSOptimizer)

    if "css" in optimize:
        # Same thing for CSS.
        site.external_manager.register_optimizer(YUICSSOptimizer)

    # Add your own types here!
