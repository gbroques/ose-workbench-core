from typing import List, Optional

from .cut_list_item import CutListItem
from .cut_list_task_panel_factory import CutListTaskPanelFactory
from .cut_list_task_type import CutListTaskType
from .task_panel import CopyCutListToClipboardTaskPanel


def create_copy_cut_list_to_clipboard_task_panel(
        cut_list_items: List[CutListItem],
        merge_cut_list_items_by_length: bool = False,
        note: Optional[str] = None) -> CopyCutListToClipboardTaskPanel:
    """Create a task panel to copy a cut-list to the user's clipboard.

    **Simple Usage**

    .. code-block:: python

        cut_list = [
            {'quantity': '1', 'description': 'Foo', 'length': '3 in'},
            {'quantity': '1', 'description': 'Bar', 'length': '3 in'}]
        panel = create_copy_cut_list_to_clipboard_task_panel(cut_list)
        Gui.Control.showDialog(panel)

    .. figure:: /_static/copy-cut-list-to-clipboard-task-panel.png
       :alt: Copy Cut List to Clipboard Task Panel
       :align: center

       Copy Cut List to Clipboard Task Panel

    **Merge Cut List Items by Length**

    .. code-block:: python

        cut_list = [
            {'quantity': '1', 'description': 'Foo', 'length': '3 in'},
            {'quantity': '1', 'description': 'Bar', 'length': '3 in'}]
        panel = create_copy_cut_list_to_clipboard_task_panel(cut_list,
            merge_cut_list_items_by_length=True)
        Gui.Control.showDialog(panel)

    .. figure:: /_static/copy-cut-list-to-clipboard-task-panel-merge-items.png
       :alt: Copy Cut List to Clipboard Task Panel with Merged Items
       :align: center

       Copy Cut List to Clipboard Task Panel with Merged Items

    :param cut_list_items: A cut list.
    :type cut_list_items: List[CutListItem]
    :param merge_cut_list_items_by_length: Whether to merge cut-list items by length, defaults to ``False``
    :type merge_cut_list_items_by_length: bool, optional
    :param note: A note to display underneath cut-list table, defaults to None
    :type note: str, optional
    :return: Copy Cut List to Clipboard Task Panel
    :rtype: CopyCutListToClipboardTaskPanel
    """
    factory = CutListTaskPanelFactory(
        cut_list_items,
        merge_cut_list=merge_cut_list_items_by_length,
        note=note)
    return factory.create(CutListTaskType.CopyToClipboard)
