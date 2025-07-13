[app]

# اسم التطبيق
title = Simple Kivy App

# اسم الحزمة (يجب أن يكون فريداً)
package.name = simpleapp

# اسم المجال (لإنشاء package.domain.package.name)
package.domain = com.example

# مسار الملف الرئيسي
source.dir = .

# اسم الملف الرئيسي للتشغيل
source.main = main.py

# إصدار التطبيق
version = 1.0

# متطلبات التطبيق (المكتبات)
requirements = python3,kivy

# إعدادات نظام الأذونات (لا حاجة لأذونات خاصة هنا)
android.permissions = 

# إصدار نظام التشغيل الأدنى
android.api = 28
android.minapi = 21

# إصدار SDK الهدف
android.sdk = 28

# إعدادات توجيه الشاشة
orientation = portrait

# نظام التحكم في السعة (fullscreen)
fullscreen = 0

# إعدادات البناء
[buildozer]

# مستوى تسجيل الأحداث (log)
log_level = 2

# مجلد البناء الافتراضي
build_dir = ./.buildozer

# مسار مجلد البنية (bin)
bin_dir = ./bin