"""
    sphinxcontrib.prefecttask
    ~~~~~~~~~~~~~~~~~~~~~~~~

    Automatically document your tasks

    :license: BSD, see LICENSE for details.
"""

import pbr.version
from .prefecttask import TaskDocumenter, TaskDirective, autodoc_skip_member_handler

if False:
    # For type annotations
    from typing import Any, Dict  # noqa
    from sphinx.application import Sphinx  # noqa

__version__ = "0.2"

def setup(app):
    """Setup Sphinx extension."""
    app.setup_extension('sphinx.ext.autodoc')
    app.add_autodocumenter(TaskDocumenter)
    app.add_directive_to_domain('py', 'task', TaskDirective)
    app.add_config_value('task_prefix', '(task)', True)
    app.connect('autodoc-skip-member', autodoc_skip_member_handler)

    return {
        "version": __version__,
        'parallel_read_safe': True
    }
