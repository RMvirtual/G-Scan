import wx

from wx.lib.floatcanvas import FloatCanvas
from gui.viewer.panels.page_view import PageView


class PageViewController:
    def __init__(self, gui: PageView):
        self._gui = gui
        self.canvas = gui.canvas

        self._initialise_bindings()

    def _initialise_bindings(self) -> None:
        self.canvas.Bind(wx.EVT_MOUSEWHEEL, self.on_wheel)
        self.canvas.Bind(wx.EVT_LEFT_DCLICK, self.fit_page_to_panel)

    def clear_display(self) -> None:
        self.canvas.ClearAll()
        self.canvas.ZoomToBB()

    def load_image(self, image: wx.Image) -> None:
        bitmap = FloatCanvas.ScaledBitmap(
            Bitmap=image, XY=(0,0), Height=image.GetHeight(), Position="bl")

        self.clear_display()
        self.canvas.AddObject(bitmap)
        self.canvas.ZoomToBB()

    def set_page_no(self, page_no) -> None:
        self._gui.page_no.SetValue(page_no)

    def set_total_pages(self, quantity: int or str) -> None:
        self._gui.set_total_pages(quantity)

    def on_wheel(self, event: wx.EVT_MOUSEWHEEL):
        zoom_factor = (1 / 1.2) if event.GetWheelRotation() < 0 else 1.2

        self.canvas.Zoom(
            zoom_factor, event.Position, "Pixel", keepPointInPlace=True)

    def fit_page_to_panel(self, _event: wx.EVT_LEFT_DCLICK = None):
        self.canvas.ZoomToBB()

    def bind_page_no(self, callback) -> None:
        self._gui.page_no.Bind(event=wx.EVT_SPINCTRL, handler=callback)

    def bind_delete(self, callback) -> None:
        self._gui.delete_button.Bind(event=wx.EVT_BUTTON, handler=callback)

    def bind_split_pages(self, callback) -> None:
        self._gui.split_button.Bind(event=wx.EVT_BUTTON, handler=callback)

    def show_all_widgets(self) -> None:
        self._gui.delete_button.Show()
        self._gui.split_button.Show()
        self._gui.page_no.Show()
        self._gui.page_quantity.Show()

    def hide_all_widgets(self) -> None:
        self._gui.delete_button.Hide()
        self._gui.split_button.Hide()
        self._gui.page_no.Hide()
        self._gui.page_quantity.Hide()

    def show_split_button(self) -> None:
        self._gui.split_button.Show()

    def hide_split_button(self) -> None:
        self._gui.split_button.Hide()
