import asyncio
import pyautogui
import time

from app import logger, loop

from .eset_window import EsetWindow, TooManyAttempts

class WindowManager:
    window: EsetWindow
    def __init__(self, window):
        self.window = window

    async def waiting_is_active(self):
        while True:
            if self.window.is_active:
                break
            await asyncio.sleep(0.1)
    
    async def waiting_is_failed(self):
        while True:
            try:
                if self.window.is_failed:
                    logger.info("Key was failed")
                    break
                await asyncio.sleep(0.1)
            except TooManyAttempts:
                logger.error("Too many attempts, use vpn")
                self.force_stop()
    
    async def waiting_of_exit(self):
        while True:
            if not self.window.is_active:
                self.force_stop()
            await asyncio.sleep(0.1)
    
    @staticmethod
    def force_stop():
        logger.error("Force stop the programm")
        loop.stop()
        exit(1)

    async def run_key_operation(self, key):
        self.goto_entering_page()
        self.enter_key(key)
        await self.waiting_is_failed()
        self.goto_home_page()
        
    @classmethod
    def goto_entering_page(cls):
        logger.debug("Goto enter page")
        cls.press_tab()
        cls.press_tab()
        cls.press_enter()

    @classmethod
    def enter_key(cls, key):
        logger.debug(f"Enter key {key}")

        cls.press_tab()
        cls.enter_text(key)
        cls.press_enter()
        
    @classmethod
    def goto_home_page(cls):
        logger.debug("Goto home page")

        cls.press_tab()
        cls.press_tab()
        cls.press_tab()
        cls.press_tab()
        cls.press_enter()

    @staticmethod
    def press_tab():
        logger.debug(f"Pressing tab")

        pyautogui.press("tab")

    @staticmethod
    def press_enter():
        logger.debug("Pressing Enter")

        pyautogui.press("enter")

    @staticmethod
    def enter_text(text):
        logger.debug(f"Enter text {text}")
        
        pyautogui.write(text)
        