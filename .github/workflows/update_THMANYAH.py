import re

def update_playlist():
    # أسماء الملفات
    TOKEN_FILE = "token.txt"
    PLAYLIST_FILE = "THMANYAH"  # <--- تم التعديل هنا (بدون امتداد)

    # 1. قراءة التوكن الجديد من الملف
    try:
        with open(TOKEN_FILE, 'r', encoding='utf-8') as f:
            new_token = f.read().strip() # .strip() لإزالة أي مسافات أو أسطر جديدة
    except FileNotFoundError:
        print("❌ خطأ: لم يتم العثور على ملف token.txt")
        return

    if not new_token:
        print("⚠️ تحذير: ملف token.txt فارغ!")
        return

    # 2. قراءة ملف القائمة
    try:
        with open(PLAYLIST_FILE, 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"❌ خطأ: لم يتم العثور على ملف {PLAYLIST_FILE}")
        return

    # 3. البحث والاستبدال (Regex)
    # نمط يبحث عن الدومين ثم التوكن (الذي يبدأ بـ eyJ) ثم /live/
    pattern = r'(https://gcp-live\.servers8\.com/)(eyJ[a-zA-Z0-9_\-\.]+)(/live/)'
    
    # استبدال التوكن القديم بالجديد
    updated_content = re.sub(pattern, r'\g<1>' + new_token + r'\g<3>', content)

    # 4. التحقق من حدوث تغيير
    if content == updated_content:
        print("ℹ️ لا توجد تغييرات. إما أن التوكن محدث بالفعل أو أن النمط غير موجود.")
        return

    # 5. حفظ الملف المحدث
    with open(PLAYLIST_FILE, 'w', encoding='utf-8') as f:
        f.write(updated_content)
    
    print(f"✅ تم تحديث ملف {PLAYLIST_FILE} بنجاح بالتوكن الجديد!")

if __name__ == "__main__":
    update_playlist()
