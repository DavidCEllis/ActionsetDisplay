from windows_toasts import (
    WindowsToaster,
    ToastImageAndText2,
    ToastDisplayImage,
    ToastDuration,
)

from .base import BaseNotifier
from ..data import icon_file


class ToastNotifier(BaseNotifier):
    FRONTEND_NAME = "toast"

    def __init__(self, *, settings):
        super().__init__(settings=settings)
        self.toaster = WindowsToaster(self.settings["title"])

        self.image = ToastDisplayImage.fromPath(icon_file, circleCrop=False)

        self.toast = ToastImageAndText2()
        self.toast.SetSuppressPopup(False)
        self.toast.SetDuration(ToastDuration.Short)
        self.toast.AddImage(self.image)
        self.toast.SetHeadline(self.settings["header"])

    def display(self, message):
        self.toast.SetFirstLine(message)
        self.toaster.show_toast(self.toast)
