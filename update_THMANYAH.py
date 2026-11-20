import re

def update_playlist():
    TOKEN_FILE = "token.txt"
    PLAYLIST_FILES = [
        "THMANYAH",
        "811.m3u",
        "812.m3u",
        "813.m3u",
        "814.m3u",
        "815.m3u",
        "816.m3u",
    ]

    # 1. قراءة التوكن الجديد
    try:
        with open(TOKEN_FILE, 'r', encoding='utf-8') as f:
            new_token = f.read().strip()
    except FileNotFoundError:
        print("❌ خطأ: لم يتم العثور على ملف token.txt")
        return

    if not new_token:
        print("⚠️ تحذير: ملف token.txt فارغ!")
        return

    # النمط: الدومين + التوكن القديم + /live/
    pattern = re.compile(r'(https://gcp-live\.servers8\.com/)(eyJ[a-zA-Z0-9_\-\.]+)(/live/)')

    # استخدام دالة للاستبدال لتجنب مشاكل الرموز الخاصة في التوكن
    def replacer(match):
        return match.group(1) + new_token + match.group(3)

    # 2. معالجة كل ملف
    for playlist_file in PLAYLIST_FILES:
        try:
            with open(playlist_file, 'r', encoding='utf-8') as f:
                content = f.read()
        except FileNotFoundError:
            print(f"❌ لم يتم العثور على ملف {playlist_file}")
            continue

        updated_content = pattern.sub(replacer, content)

        if content == updated_content:
            print(f"ℹ️ {playlist_file}: لا توجد تغييرات (التوكن محدث أو النمط غير موجود).")
            continue

        with open(playlist_file, 'w', encoding='utf-8') as f:
            f.write(updated_content)

        print(f"✅ تم تحديث {playlist_file} بنجاح!")

if __name__ == "__main__":
    update_playlist()
