<div align="center">
  <a href="https://v2.nonebot.dev/store"><img src="https://github.com/A-kirami/nonebot-plugin-template/blob/resources/nbp_logo.png" width="180" height="180" alt="NoneBotPluginLogo"></a>
  <br>
  <p><img src="https://github.com/A-kirami/nonebot-plugin-template/blob/resources/NoneBotPlugin.svg" width="240" alt="NoneBotPluginText"></p>
</div>

<div align="center">

# nonebot-plugin-sleep

_✨ NoneBot 来份精致的睡眠套餐 ✨_


<a href="./LICENSE">
    <img src="https://img.shields.io/github/license/mas-alone/nonebot-plugin-sleep.svg" alt="license">
</a>
<a href="https://pypi.python.org/pypi/nonebot-plugin-sleep">
    <img src="https://img.shields.io/pypi/v/nonebot-plugin-sleep.svg" alt="pypi">
</a>
<img src="https://img.shields.io/badge/python-3.8+-blue.svg" alt="python">

</div>

## 📖 介绍

想拥有一份精致的睡眠套餐吗? ^ ^

发送指令让bot给你吧!

## 💿 安装

<details>
<summary>使用 nb-cli 安装</summary>
在 nonebot2 项目的根目录下打开命令行, 输入以下指令即可安装

    nb plugin install nonebot-plugin-sleep

</details>

<details>
<summary>使用包管理器安装</summary>
在 nonebot2 项目的插件目录下, 打开命令行, 根据你使用的包管理器, 输入相应的安装命令

<details>
<summary>pip</summary>

    pip install nonebot-plugin-sleep
</details>
<details>
<summary>pdm</summary>

    pdm add nonebot-plugin-example
</details>
<details>
<summary>poetry</summary>

    poetry add nonebot-plugin-example
</details>
<details>
<summary>conda</summary>

    conda install nonebot-plugin-example
</details>

打开 nonebot2 项目根目录下的 `pyproject.toml` 文件, 在 `[tool.nonebot]` 部分追加写入

    plugins = ["nonebot_plugin_sleep"]

</details>

## ⚙️ 注意

bot必须为 管理员/群主 才有禁言的权限

否则只回复晚安。且无法禁言管理员！

## 🎉 使用
### 指令表
`/sleep`<br>
禁言发指令的用户8小时，bot回复晚安。<br><br>
`/sleep 10`<br>
禁言发指令的用户10小时，bot回复晚安。<br><br>
 **sleep** 后面带数字的话就禁言对应的时长，必须为整数， **最多24** 也就是1天，如果超过24则也禁言1天， **最小1** 也就是1小时，不带数字就是第一个例子了默认8小时。
