from typing import List, Optional

from .cut_list_item import CutListItem
from .cut_list_task_panel_factory import CutListTaskPanelFactory
from .cut_list_task_type import CutListTaskType
from .task_panel import SaveCutListAsCsvTaskPanel


def create_save_cut_list_to_file_task_panel(
        cut_list_items: List[CutListItem],
        merge_cut_list_items_by_length: bool = False,
        note: Optional[str] = None) -> SaveCutListAsCsvTaskPanel:
    """Create a task panel to save a cut-list to the user's filesystem.

    **Simple Usage**

    .. code-block:: python

        cut_list = [
            {'quantity': '1', 'description': 'Foo', 'length': '3 in'},
            {'quantity': '1', 'description': 'Bar', 'length': '3 in'}]
        panel = create_save_cut_list_to_file_task_panel(cut_list)
        Gui.Control.showDialog(panel)

    .. figure:: /_static/save-cut-list-to-file-task-panel.png
       :alt: Save Cut List to File Task Panel
       :align: center

       Save Cut List to File Task Panel

    **Merge Cut List Items by Length & Note**

    .. code-block:: python

        cut_list = [
            {'quantity': '1', 'description': 'Foo', 'length': '3 in'},
            {'quantity': '1', 'description': 'Bar', 'length': '3 in'}]
        panel = create_save_cut_list_to_file_task_panel(cut_list,
            merge_cut_list_items_by_length=True, note='example note')
        Gui.Control.showDialog(panel)

    .. figure:: /_static/save-cut-list-to-file-task-panel-merge-items-note.png
       :alt: Save Cut List to File Task Panel with Merged Items & Note
       :align: center

       Save Cut List to File Task Panel with Merged Items & Note

    :param cut_list_items: A cut list.
    :type cut_list_items: List[CutListItem]
    :param merge_cut_list_items_by_length: Whether to merge cut-list items by length, defaults to ``False``
    :type merge_cut_list_items_by_length: bool, optional
    :param note: A note to display underneath cut-list table, defaults to None
    :type note: str, optional
    :return: Save Cut List to File Task Panel
    :rtype: SaveCutListAsCsvTaskPanel
    """
    factory = CutListTaskPanelFactory(
        cut_list_items,
        merge_cut_list=merge_cut_list_items_by_length,
        note=note)
    return factory.create(CutListTaskType.SaveToFile)
