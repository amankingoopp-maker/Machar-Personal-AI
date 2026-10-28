
[app]

title = Machar Personal AI
package.name = macharpersonalai
package.domain = com.machar

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json,txt,ttf,ogg,wav

version = 1.0

requirements = python3,kivy

orientation = portrait
fullscreen = 0

android.permissions = INTERNET,RECORD_AUDIO

android.api = 35
android.minapi = 23
android.archs = arm64-v8a

android.accept_sdk_license = True

[buildozer]

log_level = 2
warn_on_root = 1
