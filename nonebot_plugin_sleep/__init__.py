import math

from nonebot import on_command
from nonebot.params import CommandArg
from nonebot.plugin import PluginMetadata
from nonebot.adapters.onebot.v11.bot import Bot
from nonebot.adapters.onebot.v11.event import GroupMessageEvent
from nonebot.adapters.onebot.v11.message import Message, MessageSegment

__plugin_meta__ = PluginMetadata(
    name='来份精致的睡眠套餐',
    description='发送sleep禁言，参数为时间，单位：小时， 最低1小时，最高24小时',
    usage='sleep[数字]',
    config={},
    extra={}
)

sleep = on_command(
    'sleep',
    priority=1,
    block=False
)


@sleep.handle()
async def _(bot: Bot, event: GroupMessageEvent, args: Message = CommandArg()):
    sleep_time = str(args).strip()
    if sleep_time == '':
        if event.sender.role == 'member':
            self_info = await bot.get_group_member_info(group_id=event.group_id, user_id=event.self_id)
            if self_info['role'] != 'member':
                await bot.set_group_ban(group_id=event.group_id, user_id=event.user_id, duration=28800)
        await sleep.finish(MessageSegment.reply(event.message_id) + '晚安~')
    else:
        if sleep_time.replace('.', '').isdigit():
            sleep_time = round(float(sleep_time))
            if sleep_time < 1:
                sleep_time = 1
            elif sleep_time > 24:
                sleep_time = 24
            duration = int(sleep_time * 3600)
            if event.sender.role == 'member':
                self_info = await bot.get_group_member_info(group_id=event.group_id, user_id=event.self_id)
                if self_info['role'] != 'member':
                    await bot.set_group_ban(group_id=event.group_id, user_id=event.user_id, duration=duration)
            await sleep.finish(MessageSegment.reply(event.message_id) + '晚安~')
        else:
            await sleep.finish(MessageSegment.reply(event.message_id) + '请发送sleep+数字哦~')
