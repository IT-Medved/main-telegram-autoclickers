import os
import random
from utils.yescoin import YesCoin
from utils.core import logger
from aiohttp.client_exceptions import ContentTypeError
import asyncio
from data import config


async def start(thread: int, session_name: str, phone_number: str, proxy: [str, None]):
    yes = YesCoin(session_name=session_name, phone_number=phone_number, thread=thread, proxy=proxy)
    account = session_name + '.session'

    if await yes.login():
        logger.success(f"Thread {thread} | {account} | Login")

        error_cnt = 0
        update = False
        balance = await yes.get_balance()
        (single_coin_value, special_box_left_recovery_count, coin_pool_recovery_level,
         coin_pool_recovery_upgrade_cost, coin_pool_left_recovery_count) = await yes.get_account_build_info()
        while True:
            try:
                if update:
                    (single_coin_value, special_box_left_recovery_count, coin_pool_recovery_level,
                        coin_pool_recovery_upgrade_cost, coin_pool_left_recovery_count) = await yes.get_account_build_info()
                    update = False
                energy = await yes.get_energy()

                if energy > config.MINIMUM_ENERGY:
                    points = await yes.collect_points((energy-config.MINIMUM_ENERGY)//(single_coin_value*2))
                    logger.success(f"Thread {thread} | {account} | Collect {points} points!")
                    balance += points

                if energy < 100 and coin_pool_left_recovery_count and config.BOOSTERS['USE_RECOVERY']:
                    if await yes.recover_coin_pool():
                        logger.success(f"Thread {thread} | {account} | Made a full energy recovery!")
                        coin_pool_left_recovery_count -= 1

                if special_box_left_recovery_count and config.BOOSTERS['USE_CHESTS']:
                    if await yes.get_recover_special_box():
                        box_type, special_box_total_count = await yes.get_special_box_info()
                        special_box_left_recovery_count -= 1
                        await asyncio.sleep(9)

                        collect_points = await yes.collect_special_box_coin(box_type, special_box_total_count)
                        balance += collect_points
                        logger.success(f"Thread {thread} | {account} | Collect {collect_points} points from box!")

                if (coin_pool_recovery_level <= config.AUTOUPGRADE_FILL_RATE[1] and balance > coin_pool_recovery_upgrade_cost
                        and config.AUTOUPGRADE_FILL_RATE[0]):
                    if await yes.upgrade():
                        logger.success(f"Thread {thread} | {account} | Made fill rate upgrade")
                        balance = await yes.get_balance()
                        update = True

                if config.COMPLETE_TASKS:
                    for task in await yes.get_tasks():
                        if not task['taskStatus']:
                            status, bonus = await yes.finish_task(task['taskId'])

                            if status: logger.success(f"Thread {thread} | {account} | Complete task «{task['taskName']}» and got {bonus}")
                            else: logger.error(f"Thread {thread} | {account} | Can't complete task «{task['taskName']}»")
                            await asyncio.sleep(random.uniform(*config.DELAYS['TASKS']))

                await asyncio.sleep(random.uniform(*config.DELAYS['CLICKS']))

                await yes.logout()
                logger.success(f"Thread {thread} | {account} | All activities in yescoin completed")
                return 0
            except ContentTypeError as e:
                logger.error(f"Thread {thread} | {account} | Error: {e}")
                await asyncio.sleep(52)
                error_cnt += 1
                if (error_cnt >= config.ERRORS_BEFORE_STOP):
                    await yes.logout()
                    return 0
            except Exception as e:
                logger.error(f"Thread {thread} | {account} | Error: {e}")
                await asyncio.sleep(52)
                error_cnt += 1
                if (error_cnt >= config.ERRORS_BEFORE_STOP):
                    await yes.logout()
                    return 0

    await yes.logout()