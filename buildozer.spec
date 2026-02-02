[app]

# (str) Title of your application
title = 安卓连点器

# (str) Package name
package.name = androidclicker

# (str) Package domain (needed for android/ios packaging)
package.domain = org.clicker

# (str) Source files where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas,json

# (list) List of inclusions using pattern matching
source.include_patterns = assets/*,images/*.png

# (list) Source files to exclude (let empty to not exclude anything)
#source.exclude_exts = spec

# (str) Application versioning (method 1)
version = 0.1

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy

# (str) Presplash of the application
#presplash.filename = %(source.dir)s/data/presplash.png

# (str) Icon of the application
#icon.filename = %(source.dir)s/data/icon.png

# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
orientation = portrait

# (list) List of allowed to be used on iOS/Android
android.permits = INTERNET

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

#
# Android specific
#

# (list) Permissions
android.permissions = INTERNET,SYSTEM_ALERT_WINDOW

# (int) Target Android API, should be as high as possible.
#android.api = 31

# (int) Minimum API your APK will support.
#android.minapi = 21

# (int) Android NDK version to use
#android.ndk = 23b

# (int) Android NDK API to use. This is the minimum API your app will support, it should usually match android.minapi.
#android.ndk_api = 21

# (bool) If True, then skip trying to update the Android sdk
# This can be useful to avoid excess Internet downloads or save time
# when an update is due and a local build already exists.
android.skip_update = False

# (bool) If True, then automatically accept SDK license
# agreements. This is intended for automation only. If set to False,
# the default, you will have to manually accept sdk licenses when
# asked.
android.accept_sdk_license = True

# (str) Android entry point, default is ok for Kivy-based app
#android.entrypoint = org.kivy.android.PythonActivity

# (str) Android app theme, default is ok for Kivy-based app
#android.apptheme = "@android:style/Theme.NoTitleBar"

# (list) Pattern to whitelist for the whole project
#android.whitelist =

# (str) Path to a custom whitelist file
#android.whitelist_src =

# (str) Path to a custom blacklist file
#android.blacklist_src =

# (list) List of Java .jar files to add to the libs so that pyjnius can access
# their classes. Don't add jars that you do not need, since extra jars can slow
# down the build process. Allowed wildcards are * and ?
#android.add_jars = foo.jar,bar.jar,

# (list) List of Java files to add to the android project (can be java or a
# directory containing the files)
#android.add_src =

# (list) Android AAR archives to add (currently works only with sdl2 gradle
# bootstrap)
#android.add_aars =

# (list) Gradle dependencies to add (currently works only with sdl2 gradle
# bootstrap)
android.gradle_dependencies =

# (list) add java compile options
# this can help to reduce deps size or enable building with new java versions
#android.add_compile_options =

# (list) Java jars to add to the project (can be a file or a directory)
#android.add_jars =

# (list) Android ndk flags
#android.ndk =

# (bool) If True, then android.add_jars will also add any
# aar's built into the project and not just their jars
#android.add_aars = False

# (list) Java classpath to (respectively) include jnius or pyjnius
android.bootstrap = sdl2

# (str) Android entry point, default is ok for Kivy-based app
#android.entrypoint = org.kivy.android.PythonActivity

# (str) Android app theme, default is ok for Kivy-based app
#android.apptheme = "@android:style/Theme.NoTitleBar"

# (list) Pattern to whitelist for the whole project
#android.whitelist =

# (str) Path to a custom whitelist file
#android.whitelist_src =

# (str) Path to a custom blacklist file
#android.blacklist_src =

# (list) List of Java .jar files to add to the libs so that pyjnius can access
# their classes. Don't add jars that you do not need, since extra jars can slow
# down the build process. Allowed wildcards are * and ?
#android.add_jars = foo.jar,bar.jar,

# (list) List of Java files to add to the android project (can be java or a
# directory containing the files)
#android.add_src =

# (list) Android AAR archives to add (currently works only with sdl2 gradle
# bootstrap)
#android.add_aars =

# (list) Gradle dependencies to add (currently works only with sdl2 gradle
# bootstrap)
#android.gradle_dependencies =

# (list) add java compile options
# this can help to reduce deps size or enable enable building with new java versions
#android.add_compile_options =

# (list) Java jars to add to the project (can be a file or a directory)
#android.add_jars =

# (list) Android ndk flags
#android.ndk =

# (bool) If True, then android.add_jars will also add any
# aar's built into the project and not just their jars
#android.add_aars = False

# (list) Java classpath to (respectively) include jnius or pyjnius
#android.javaclasspath =

# (str) python-for-android branch to use, defaults to master
#p4a.branch = master

# (str) python-for-android specific flags to pass
#p4a.flags =

# (str) python-for-android fork to use, defaults to upstream kivy
#p4a.fork = kivy

# (str) python-for-android specific flags to pass
#p4a.local_recipes =

# (str) Specific python-for-android branch to use
#p4a.branch =

# (int) python-for-android revision to use
#p4a.revision =

# (list) python-for-android specific modules to use (e.g. android.billing)
#p4a.modules =

# (list) Python for Android Android specific modules to use (e.g. android.billing)
#p4a.android_modules =

# (int) port number for the buildozer server to listen on
#buildozer.server_port =

# (int) Number of workers to use when building in parallel
#buildozer.workers =

# (bool) Whether to preserve intermediate files for faster rebuilds
#buildozer.preserve_artifacts =

# (bool) Whether to clean buildozer cache before building
#buildozer.clean_build =

# (bool) Whether to create a debug APK or release APK
#android.release = False

# (str) Key alias for signing the release APK
#android.key_alias =

# (str) Key password for signing the release APK
#android.key_pass =

# (str) Path to the keystore file for signing the release APK
#android.keystore =

# (str) Keystore password for signing the release APK
#android.keystore_pass =

# (str) Build architecture for the Android application
#android.arch = arm64-v8a

# (list) Android app libraries to add (can be a file or a directory)
#android.library_libs =

# (list) Android app libraries to add
#android.libs =

# (str) Android extra libraries to add
#android.extra_libs =

# (bool) Android aapt extra options
#android.aapt_ignore =

# (list) Android AAR archives to add
#android.add_aars =

# (list) Android add src
#android.add_src =

# (str) Android entrypoint
#android.entrypoint = org.kivy.android.PythonActivity

# (str) Android min api
#android.minapi = 21

# (str) Android ndk
#android.ndk =

# (str) Android ndk api
android.ndk_api =24
android.api = 33


# (str) Android preserve apk path
#android.preserve_apk_path =

# (str) Android sdk
#android.sdk =

# (str) Android skip update
#android.skip_update =

# (str) Android whitelist src
#android.whitelist_src =
