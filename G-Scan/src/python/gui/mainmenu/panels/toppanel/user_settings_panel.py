import wx
import date.date as date

from gui.mainmenu.panels.panel import Panel

class UserSettingsPanel(Panel):
    """A class modelling the user settings panel window found in the
    top panel of the main menu GUI.
    """

    def __init__(self, top_panel):
        """Creates a new user settings panel widget."""

        super().__init__(
            top_panel,
            size = (420, 255),
            position = (425, 0)
        )

        self.__create_widgets()

    def __create_widgets(self):
        """Creates the widgets required for the user settings panel."""

        self.__create_paperwork_type_widgets()
        self.__create_input_mode_widgets()
        self.__create_multi_page_handling_widgets()

    def __create_paperwork_type_widgets(self):
        """Creates the widgets related to the paperwork type settings
        in the GUI."""

        # Paperwork type heading label.
        self.__paperwork_type_label = wx.StaticText(
            self,
            label = "Paperwork Type",
            size = (60, 25),
            pos = (0, 0)
        )

        self.__paperwork_type_label.SetFont(self.get_body_font())

        # "Customer Paperwork" paperwork type radio button.
        self.__customer_paperwork_radio_button = wx.RadioButton(
            self,
            label = "Customer Paperwork",
            size = (160, 25),
            pos = (0, 25),
            style = wx.RB_GROUP
        )

        self.__customer_paperwork_radio_button.SetFont(self.get_button_font())

        # "Loading List" paperwork type radio button.
        self.__loading_list_radio_button = wx.RadioButton(
            self,
            label = "Loading List",
            size = (90, 25),
            pos = (160, 25),
        )

        self.__loading_list_radio_button.SetFont(self.get_button_font())

        # "POD" paperwork type radio button.
        self.__pod_radio_button = wx.RadioButton(
            self,
            label = "POD",
            size = (45, 25),
            pos = (265, 25)
        )

        self.__pod_radio_button.SetFont(self.get_button_font())

        # Autoprocessing checkbox.
        self.__autoprocessing_checkbox = wx.CheckBox(
            self,
            label = "Autoprocess",
            size = (85, 25),
            pos = (320, 25)
        )

        self.__autoprocessing_checkbox.SetFont(wx.Font(
            9, wx.MODERN, wx.NORMAL, wx.NORMAL, False, u"calibri"))

    def __create_input_mode_widgets(self):
        """Creates the widgets for setting the input mode in the
        GUI."""

        # Input Mode heading label.
        self.__input_mode_label = wx.StaticText(
            self,
            label = "Input Mode",
            size = (60, 25),
            pos = (0, 85)
        )

        self.__input_mode_label.SetFont(self.get_body_font())

        # Normal Mode radio button.
        self.__normal_mode_radio_button = wx.RadioButton(
            self,
            label = "Normal Mode",
            size = (120, 25),
            pos = (0, 110),
            style = wx.RB_GROUP
        )

        self.__normal_mode_radio_button.SetFont(self.get_button_font())

        # Quick Mode radio button.
        self.__quick_mode_radio_button = wx.RadioButton(
            self,
            label = "Quick Mode",
            size = (90, 25),
            pos = (160, 110),
        )

        self.__quick_mode_radio_button.SetFont(self.get_button_font())

        # Months dropdown box.
        month_options = date.get_months_as_strings()
        current_month = date.get_current_month().get_full_code()

        self.__months_dropdown_box = wx.ComboBox(
            self,
            value = current_month,
            size = (120, 25),
            pos = (275, 110),
            choices = month_options,
            style = wx.CB_DROPDOWN | wx.CB_READONLY
        )

        self.__months_dropdown_box.SetFont(self.get_button_font())
        self.__months_dropdown_box.SetBackgroundColour("LIGHT GREY")

        # Years dropdown box.
        year_options = date.get_years_as_strings()
        current_year = date.get_current_year().get_full_code()

        self.__years_dropdown_box = wx.ComboBox(
            self,
            value = current_year,
            size = (120, 25),
            pos = (275, 140),
            choices = year_options,
            style = wx.CB_DROPDOWN | wx.CB_READONLY
        )

        self.__years_dropdown_box.SetFont(self.get_button_font())
        self.__years_dropdown_box.SetBackgroundColour("LIGHT GREY")

    def __create_multi_page_handling_widgets(self):
        """Creates the widgets responsible for setting multi-page
        handling's behaviour in the program."""

        # Multi-Page Handling heading label.
        self.__multi_page_handling_label = wx.StaticText(
            self,
            label = "Multi-Page Handling",
            size = (160, 25),
            pos = (0, 175)
        )

        self.__multi_page_handling_label.SetFont(self.get_body_font())

        # Split radio button.
        self.__split_radio_button = wx.RadioButton(
            self,
            label = "Split Documents",
            size = (120, 25),
            pos = (0, 200),
            style = wx.RB_GROUP
        )

        self.__split_radio_button.SetFont(self.get_button_font())

        # Do Not Split radio button.
        self.__do_not_split_radio_button = wx.RadioButton(
            self,
            label = "Do Not Split Documents",
            size = (90, 25),
            pos = (160, 200)
        )

        self.__do_not_split_radio_button.SetFont(self.get_button_font())