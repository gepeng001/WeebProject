# Copyright (C) 2021 Bian Sepang
# All Rights Reserved.
#

import nekos

from userbot import CMD_HELP
from userbot.events import register

arguments = [
    "feet",
    "yuri",
    "trap",
    "futanari",
    "hololewd",
    "lewdkemo",
    "solog",
    "feetg",
    "cum",
    "erokemo",
    "les",
    "wallpaper",
    "lewdk",
    "ngif",
    "tickle",
    "lewd",
    "feed",
    "gecg",
    "eroyuri",
    "eron",
    "cum_jpg",
    "bj",
    "nsfw_neko_gif",
    "solo",
    "nsfw_avatar",
    "gasm",
    "poke",
    "anal",
    "slap",
    "hentai",
    "avatar",
    "erofeet",
    "holo",
    "keta",
    "blowjob",
    "pussy",
    "tits",
    "holoero",
    "lizard",
    "pussy_jpg",
    "pwankg",
    "classic",
    "kuni",
    "waifu",
    "pat",
    "8ball",
    "kiss",
    "femdom",
    "neko",
    "spank",
    "cuddle",
    "erok",
    "fox_girl",
    "boobs",
    "random_hentai_gif",
    "smallboobs",
    "hug",
    "ero",
    "goose",
    "baka",
    "woof",
    "kemonomimi",
    "smug",
]


@register(outgoing=True, pattern=r"^\.nekos(?: |$)(.*)")
async def nekos_img(event):
    args = event.pattern_match.group(1)
    if not args or args not in arguments:
        return await event.edit("`Ketik “.help nekos” untuk melihat argumen yang tersedia.`")
    await event.edit("`Mengambil data dari nekos...`")
    pic = nekos.img(args)
    await event.client.send_file(
        event.chat_id,
        pic,
        caption=f"[Sumber]({pic})",
    )
    await event.delete()


CMD_HELP.update(
    {
        "nekos": "`.nekos [argumen]`"
        "\n➥  Untuk mengambil gambar dari nekos."
        "\n\n**Argumen** : `8ball`, `anal`, `avatar`, `baka`, `bj`,"
        "`blowjob`, `boobs`, `classic`, `cuddle`, `cum`,"
        "`cum_jpg`, `ero`, `erofeet`, `erok`, `erokemo`,"
        "`eron`, `eroyuri`, `feed`, `feet`, `feetg`,"
        "`femdom`, `fox_girl`, `futanari`, `gasm`, `gecg`,"
        "`goose`, `hentai`, `holo`, `holoero`, `hololewd`,"
        "`hug`, `kemonomimi`, `keta`, `kiss`, `kuni`,"
        "`les`, `lewd`, `lewdk`, `lewdkemo`, `lizard`,"
        "`neko`, `ngif`, `nsfw_avatar`, `nsfw_neko_gif`, `pat`,"
        "`poke`, `pussy`, `pussy_jpg`, `pwankg`, `random_hentai_gif`,"
        "`slap`, `smallboobs`, `smug`, `solo`, `solog`,"
        "`spank`, `tickle`, `tits`, `trap`, `waifu`,"
        "`wallpaper`, `woof`, `yuri`"
    }
)
