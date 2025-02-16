from typing import Callable

import wx

from configuration import Configuration
from controllers.mediator import ApplicationMediator
from departments import Department
from documents import DocumentType
from gui.main_menu.document_selection import DocumentSelectionPanel
from gui.main_menu.main_menu import MainMenu
from gui.window import Window


class MainMenuController:
    def __init__(
            self, root: ApplicationMediator, config: Configuration, window: Window
    ) -> None:
        self.root = root
        self.config = config
        self.panel = MainMenu(window, config.departments)

        window.set_panel(self.panel)

        # Callbacks.
        self.panel.Bind(wx.EVT_CLOSE, self.on_close)
        
        depts_panel = self.panel.panel
        dept_buttons = depts_panel.dept_btns

        for department in self.config.departments:
            dept_buttons[department.short_code].Bind(
                wx.EVT_BUTTON, self._department_selection_lambda(department))

        depts_panel.quick_start_btn.Bind(wx.EVT_BUTTON, self.on_quick_start)
        depts_panel.settings_btn.Bind(wx.EVT_BUTTON, self.on_settings)
        depts_panel.exit_btn.Bind(wx.EVT_BUTTON, self.on_exit)

        f4_shortcut_id = wx.NewId()
        self.panel.Bind(wx.EVT_MENU, self.on_f4, id=f4_shortcut_id)

        self.panel.SetAcceleratorTable(wx.AcceleratorTable([(
            wx.ACCEL_NORMAL, wx.WXK_F4, f4_shortcut_id)]))

        self.panel.SetFocus()
    
    def on_f4(self, event: wx.Event) -> None:
        self.launch_exit()

    def on_department_selection(
            self, event: wx.Event, department: Department) -> None:
        doc_select_panel = DocumentSelectionPanel(
            self.panel, department.document_types)
        
        self.panel.switch_to(doc_select_panel)

        # Setup callbacks to new department window.
        for document in department.document_types:
            doc_btn = doc_select_panel.option_btns[document] 
            callback = self._final_selection_lambda(department, document)
            doc_btn.Bind(wx.EVT_BUTTON, callback)

    def on_back_to_departments(self, event: wx.Event) -> None:
        self.config.department = None

    def on_quick_start(self, event: wx.Event) -> None:
        self.launch_image_viewer()

    def on_exit(self, event: wx.Event) -> None:
        self.launch_exit()

    def on_settings(self, event: wx.Event) -> None:
        self.launch_settings()

    def on_close(self, event: wx.Event) -> None:
        self.panel.Destroy()

    def launch_image_viewer(self) -> None:
        self.panel.Close()
        self.root.launch_image_viewer(self.config)

    def launch_settings(self) -> None:
        self.panel.Close()
        self.root.launch_settings()

    def launch_exit(self) -> None:
        self.panel.Close()
        self.root.exit()

    def on_selection(
            self, event: wx.Event, department: Department, 
            document: DocumentType
    ) -> None:
        self.config.department = department
        self.config.document_type = document

        self.launch_image_viewer()

    def _final_selection_lambda(
            self, department: Department, document: DocumentType
    ) -> Callable[[wx.Event], None]:
        """Used to create lambdas referencing specific departments 
        and documents within a loop as referencing specific departments 
        but without using the department as a lambda parameter will just
        end up updating all the lambdas to use the last department 
        rather than a self-contained lambda for each one. 
        Not just a hacky misunderstanding of lambdas.
        """
        return lambda event: self.on_selection(event, department, document)

    def _department_selection_lambda(
            self, department: Department) -> Callable[[wx.Event], None]:
        """Used to create lambdas referencing specific departments 
        as when trying to create multiple lambdas via a loop 
        referencing specific departments but without using the 
        department as a lambda parameter will just end up updating all 
        the lambdas to use the last department rather than a 
        self-contained lambda for each one. 
        Not just a hacky misunderstanding of lambdas.
        """
        return lambda event: self.on_department_selection(event, department)

