
import re

def update_playlist():
    TOKEN_FILE = "token.txt"

    PLAYLIST_FILES = [
        "THMANYAH",
        "811FHD.m3u",
        "812FHD.m3u",
        "813FHD.m3u",
        "811SDR4k.m3u",
        "812SDR4k.m3u",
        "813SDR4k.m3u",
        "811.m3u",
        "812.m3u",
        "813.m3u",
        "814.m3u",
        "815.m3u",
        "816.m3u",
    ]

    try:
        with open(TOKEN_FILE, "r", encoding="utf-8") as f:
            new_token = f.read().strip()
    except FileNotFoundError:
        print("❌ لم يتم العثور على token.txt")
        return

    if not new_token:
        print("⚠️ التوكن فارغ")
        return

    # البحث عن أي توكن بين الدومين ومسار live
    pattern = re.compile(
        r'(https://gcp-live\.servers8\.com/)[^/\s]+(/live/)'
    )

    def replacer(match):
        return match.group(1) + new_token + match.group(2)

    for playlist_file in PLAYLIST_FILES:
        try:
            with open(playlist_file, "r", encoding="utf-8-sig") as f:
                content = f.read()

            updated_content, count = pattern.subn(replacer, content)

            if count == 0:
                print(f"⚠️ {playlist_file}: لم يتم العثور على روابط مطابقة")
                continue

            if updated_content != content:
                with open(playlist_file, "w", encoding="utf-8") as f:
                    f.write(updated_content)

                print(f"✅ {playlist_file}: تم تحديث {count} رابط")

            else:
                print(f"ℹ️ {playlist_file}: التوكن محدث مسبقاً")

        except FileNotFoundError:
            print(f"❌ الملف غير موجود: {playlist_file}")

if __name__ == "__main__":
    update_playlist()
