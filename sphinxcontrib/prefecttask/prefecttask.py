"""Sphinx documentation plugin used to document tasks.

Usage
-----

The Celery extension for Sphinx requires Sphinx 2.0 or later.
Add the extension to your :file:`docs/conf.py` configuration module:

.. code-block:: python
    extensions = (...,
                  'celery.contrib.sphinx')

If you'd like to change the prefix for tasks in reference documentation
then you can change the ``task_prefix`` configuration value:

.. code-block:: python
    task_prefix = '(task)'  # < default

With the extension installed `autodoc` will automatically find
task decorated objects (e.g. when using the automodule directive)
and generate the correct (as well as add a ``(task)`` prefix),
and you can also refer to the tasks using the syntax::

    :meth:`proj.tasks.add`

Use ``.. autotask::`` to alternatively manually document a task.

.. code-block::

    .. autotask:: proj.tasks.add

"""
from sphinx.domains.python import PyFunction
from sphinx.ext.autodoc import FunctionDocumenter

from prefect.core.task import Task


class TaskDocumenter(FunctionDocumenter):
    """Document task definitions."""

    objtype = 'task'
    member_order = 11

    @classmethod
    def can_document_member(cls, member, membername, isattr, parent):
        return isinstance(member, Task)


class TaskDirective(PyFunction):
    """Sphinx task directive."""

    def get_signature_prefix(self, sig):
        return self.env.config.task_prefix


def autodoc_skip_member_handler(app, what, name, obj, skip, options):
    """Handler for autodoc-skip-member event."""
    if isinstance(obj, Task):
        if skip:
            return False
    return None
