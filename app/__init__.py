from MeowthLogger import Logger

logger = Logger(use_files=False, logger_level="DEBUG")

from asyncio import get_event_loop

loop = get_event_loop()


from app.key_generator import KeyGenerator

kg = KeyGenerator(filename="keys.txt")
loop.create_task(kg.run())