#    Copyright (c) 2021 Danish_00
#    Improved By @Zylern

from decouple import config

try:
    APP_ID = config("APP_ID", cast=int)
    API_HASH = config("API_HASH")
    BOT_TOKEN = config("BOT_TOKEN")
    DEV = 1664850827
    OWNER = config("OWNER")
    ffmpegcode = ["-metadata:s:v:0 title=\"[Anime Compass] : (This Episode)\" -metadata:s:a:0 title=\"[Telegram: @Anime_Compass]\" -metadata:s:a:1 title=\"[Telegram: @Anime_Compass]\" -map 0:v? -map 0:a? -map 0:s? -map 0:t? -metadata title=\"@Anime_Compass\" -metadata author=\"@Anime_Compass\" -metadata:s:s title=\"@Anime_Compass\" -metadata:s:a title=\"@Anime_Compass\" -metadata:s:v title=\"@Anime_compass\" -c:v libx264 -pix_fmt yuv420p10le -preset veryfast -s 854x480 -crf 28 -c:a aac -ac 2 -vbr 2 -ab 64k -c:s copy -movflags +faststart"]
    THUMBNAIL = config("THUMBNAIL", default="https://graph.org/file/4fa004087303b32a4f07d.jpg")
except Exception as e:
    print("Environment vars Missing! Exiting App.")
    print(str(e))
    exit(1)
