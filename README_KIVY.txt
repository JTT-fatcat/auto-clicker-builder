安卓连点器使用说明 (Kivy版本)
=============================

Kivy是打包APK最成熟的Python框架！

功能特点:
✓ 自定义点击位置和频率
✓ 支持循环点击和顺序点击
✓ 点击点列表管理
✓ 配置保存和加载
✓ 流畅的触控界面
✓ 可直接打包APK

安装依赖:
-----------
pip install -r requirements_kivy.txt

Windows用户还需要:
pip install kivy.deps.sdl2
pip install kivy.deps.glew
pip install kivy.deps.gstreamer

运行程序:
-----------
python android_clicker_kivy.py

打包APK (推荐使用Buildozer):
============================

1. 安装Buildozer:
   pip install buildozer

2. 初始化项目:
   buildozer init

3. 编辑buildozer.spec文件:
   - 修改title = "安卓连点器"
   - 修改package.name = "android.clicker"
   - 修改package.domain = "org.clicker"

4. 下载依赖并编译:
   buildozer android debug

5. 打包APK (耗时较长，第一次需要10-30分钟):
   buildozer android release

打包注意事项:
--------------
1. 需要Linux环境:
   - 推荐: WSL2 (Windows Subsystem for Linux)
   - 或者: Ubuntu虚拟机
   - 或者: 云服务器

2. 必需的依赖:
   - Python 3.7+
   - JDK 8+
   - Android SDK
   - Android NDK
   - zlib-dev
   - openjdk-8-jdk

3. Ubuntu/WSL安装命令:
   sudo apt-get update
   sudo apt-get install -y \
       python3-pip \
       build-essential \
       git \
       ffmpeg \
       libsdl2-dev \
       libsdl2-image-dev \
       libsdl2-mixer-dev \
       libsdl2-ttf-dev \
       libportmidi-dev \
       libswscale-dev \
       libavformat-dev \
       libavcodec-dev \
       zlib1g-dev \
       libgstreamer1.0-dev \
       gstreamer1.0-plugins-base \
       gstreamer1.0-plugins-good

快速开始 (Windows用户):
-----------------------
方式1: 使用Repl.it (在线编译)
1. 上传代码到Repl.it
2. 选择Kivy模板
3. 自动编译APK

方式2: 使用GitHub Actions
1. 将代码推送到GitHub
2. 配置GitHub Actions
3. 自动编译APK

方式3: 使用在线服务
1. Kivy Buildozer VM (虚拟机镜像)
2. 下载并运行，一键打包

屏幕点击实现:
--------------
Kivy版本目前只提供UI框架，实际点击功能需要额外实现：

方案A: 无障碍服务 (推荐，无需root)
1. 创建AccessibilityService
2. 通过performGlobalAction()点击
3. 需要用户授权

方案B: Root权限
1. 使用su命令
2. 通过input tap x y命令
3. 需要设备已root

方案C: ADB连接 (最简单)
1. 通过ADB连接电脑
2. 使用adb shell input tap命令
3. 需要USB调试

测试使用:
-----------
1. 在电脑上运行查看UI效果
2. 使用Android模拟器测试
3. 真实设备需要打包APK

Kivy vs Toga 对比:
------------------
Kivy:
✓ 打包APK最成熟
✓ 文档丰富
✓ 社区活跃
✓ 性能好
✗ 界面风格独特

Toga:
✓ 原生风格界面
✓ 代码简洁
✗ 打包相对复杂
✗ 文档较少

推荐使用Kivy！
