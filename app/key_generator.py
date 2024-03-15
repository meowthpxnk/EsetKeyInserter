from app import logger, loop

from .window_manager import WindowManager
from .eset_window import EsetWindow
from .keys import KeyIterator

class KeyGenerator:
    def __init__(self, filename):
        eset = EsetWindow()
        self.window_manager = WindowManager(eset)
        self.keys_iterator = KeyIterator(filename)

    async def run(self):
        logger.info("Runed KeyGen, waiting for open Eset")
        await self.window_manager.waiting_is_active()
        logger.info("WindowManager was started")

        loop.create_task(
            self.window_manager.waiting_of_exit()
        )

        loop.create_task(
            self.iterate_keys()
        )
    
    async def iterate_keys(self):
        keys = self.keys_iterator.iter_keys()

        while True:
            try:
                key = next(keys)
            except StopIteration:
                break
            except Exception as err:
                logger.error(f"Failed keys iteration, reason {err}")
                break
            
            logger.info(f"Handle key {key}")
            await self.window_manager.run_key_operation(key)
        
        logger.info("Finished keys finder.")
        loop.stop()
        