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
