from pywinauto import Desktop
from pywinauto.controls.uiawrapper import UIAWrapper

class TooManyAttempts(Exception):
    def __init__(self) -> None:
        super().__init__("Too many failed attempts to enter the correct activation key.")

class EsetWindow:
    window: UIAWrapper
    def __init__(self):
        dlg = Desktop(backend="uia")
        for window in dlg.windows():
            window = window
            if window.get_properties()["class_name"] == "EsetBaseWindow":
                self.window = window
                break
        if self.window == None:
            raise Exception("Not found eset window")
        
    @property
    def is_failed(self) -> bool:
        text = "activation failed"
        too_many_attempts_text = "many failed attempts"
        props = self.window.get_properties()
        win_texts: str = props["texts"]

        is_failed_flag = False

        for txt in win_texts:
            if text in txt.lower():
                is_failed_flag = True
            if too_many_attempts_text in txt.lower():
                raise TooManyAttempts
        return is_failed_flag

    @property
    def is_active(self) -> bool:
        return self.window.is_active()