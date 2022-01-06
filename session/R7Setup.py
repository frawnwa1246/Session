# frawn wa userbot 
#frawn wa  string session 
import os
from time import sleep

print("")
a = r"""
© FRAWN WA-USERBOT ©

╔══╗╔═╗╔══╗╔╦═╦╗╔═╦╗  ╔╦═╦╗╔══╗     
║═╦╝║╬║║╔╗║║║║║║║║║║  ║║║║║║╔╗║     
║╔╝─║╗╣║╠╣║║║║║║║║║║  ║║║║║║╠╣║    
╚╝──╚╩╝╚╝╚╝╚═╩═╝╚╩═╝  ╚═╩═╝╚╝╚╝   
────────────────────  ─────────      
فرعون للمعلومات    
𖤍𝙁𝙍𝘼𝙒𝙉 𝙒𝘼𖤍    
> CH › @source_frawn
~> DEVELOPER › @DEV_FRAWN
 ~ frawn wa UserBot
"""


def spinner():
    print("نﻮﺜﻴﻠﻴﺘﻟﺍ ﺔﺒﺘﻜﻣ ﻦﻣ ﺪﻛﺄﺘﻟﺍ ")
    for _ in range(3):
        for frame in r"-\|/-\|/":
            print("\b", frame, sep="", end="", flush=True)
            sleep(0.1)


def clear_screen():
    if os.name == "posix":
        os.system("clear")
    else:
        os.system("cls")


def get_api_id_and_hash():
    print(
        "ﻦﻣ يﺪﻳﺍ ﺐﻳﻻﺍﻭ شﺎﻫ ﻲﺒﻳﻻﺍ ﻰﻠﻋ ﻞﺼﺣﺍ my.telegram.org  @DEV_FRAWN \n\n",
    )
    try:
        API_ID = int(input("API_ID : "))
    except ValueError:
        print("ﺢﻴﺤﺻ ﻞﻜﺸﺑ يﺪﻳﺍ ﻲﺒﻳﻻﺍ ﺔﻤﻴﻗ ﻊﺿﻭ ﻰﺟﺮﻳ ")
        exit(0)
    API_HASH = input("API_HASH : ")
    return API_ID, API_HASH


def telethon_session():
    try:
        spinner()

        x = "\bFound an existing installation of Telethon...\nSuccessfully Imported.\n\n"
    except BaseException:
        print("Installing Telethon...")
        os.system("pip install -U telethon")

        x = "\bInstalled and imported Telethon" 
    clear_screen()
    print("JMTHON STRING SESSION ")
    print("T.ME/JMTHON")
    print(a)
    print(x)


    from telethon.errors.rpcerrorlist import ApiIdInvalidError, PhoneNumberInvalidError
    from telethon.sessions import StringSession
    from telethon.sync import TelegramClient

    API_ID, API_HASH = get_api_id_and_hash()

    # logging in
    try:
        with TelegramClient(StringSession(), API_ID, API_HASH) as barsha:
            print("ﺮﻈﺘﻧﺍ نﻮﺜﻤﺠﻟ ﺲﻜﻣﺮﻴﺗ دﻮﻛ ءﺎﺸﻧﺍ ﻢﺘﻳ")
            adi = barsha.send_message(
                "me",
                f"**كـود تيـرمكـس**:\n\n`{barsha.session.save()}`\n\n**لا تعطيه الى اي احد حتى المطورين  !**",
            )
            adi.reply("في الاعلى هو كود تيرمكس الخاص بك يجب لا تشاركه الى اي احد حتى لو ادعى أنه من المطورين\n - @DEV_FRAWN")
            print(
                "ﺔﻇﻮﻔﺤﻤﻟﺍ ﻞﺋﺎﺳﺮﻟﺍ ﻦﻣ ﺪﻛﺎﺗ ﺲﻜﻣﺮﻴﺗ دﻮﻛ ﻊﻨﺻ حﺎﺠﻨﺑ ﻢﺗ"
            )
            exit(0)
    except ApiIdInvalidError:
        print(
            "ﺔﻴﻠﻤﻌﻟﺍ ﺖﻬﺘﻧﺍ  ،  ﺎﻄﺧ شﺎﻫ ﻲﺒﻳﻻﺍ وﺍ يﺪﻳﺍ ﻲﺒﻳﻻﺍ نﺍ وﺪﺒﻳ"
        )
        exit(0)
    except ValueError:
        print("ﺔﻏﺭﺎﻓ ﻲﺒﻳﻻﺍ ﺔﻤﻴﻗ نﻮﻜﺗ ﻻ نﺍ ﺐﺠﻳ")
        exit(0)
    except PhoneNumberInvalidError:
        print("ﺔﻴﻠﻤﻌﻟﺍ ءﺎﻬﺘﻧﺍ  ،اﺩﺪﺠﻣ لﻭﺎﺣﻭ ﻒﺗﺎﻬﻟﺍ ﻢﻗﺭ ﻦﻣ ﺪﻛﺎﺗ")
        exit(0)


def main():
    clear_screen()
    print(a)
    telethon_session()
    x = input("Run again? (y/n")
    if x == "y":
        main()
    else:
        exit(0)


main()
