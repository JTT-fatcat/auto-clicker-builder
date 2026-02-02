"""
安卓连点器 - 使用Kivy框架
支持自定义点击位置、频率、顺序和循环模式
"""

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.slider import Slider
from kivy.uix.textinput import TextInput
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.scrollview import ScrollView
from kivy.uix.popup import Popup
from kivy.clock import Clock
from kivy.properties import NumericProperty, ListProperty, StringProperty, BooleanProperty
import json
import os
from kivy.config import Config

# 配置窗口大小（用于桌面测试）
Config.set('graphics', 'width', '400')
Config.set('graphics', 'height', '600')


class PointItem(BoxLayout):
    """点击点列表项"""
    index = NumericProperty(0)
    x_coord = NumericProperty(0)
    y_coord = NumericProperty(0)

    def __init__(self, index, x, y, delete_callback, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'horizontal'
        self.size_hint_y = None
        self.height = 40

        self.index = index
        self.x_coord = x
        self.y_coord = y

        # 序号标签
        self.lbl_index = Label(
            text=f"{index + 1}",
            size_hint_x=0.2,
            font_size=12
        )
        self.add_widget(self.lbl_index)

        # 坐标标签
        self.lbl_coord = Label(
            text=f"({x}, {y})",
            size_hint_x=0.5,
            font_size=12
        )
        self.add_widget(self.lbl_coord)

        # 删除按钮
        btn_delete = Button(
            text="删除",
            size_hint_x=0.3,
            font_size=12
        )
        btn_delete.bind(on_press=lambda instance: delete_callback(index))
        self.add_widget(btn_delete)


class AndroidClickerApp(App):
    """安卓连点器主应用"""

    # 状态变量
    clicking = BooleanProperty(False)
    click_points = ListProperty([])
    current_index = NumericProperty(0)
    click_interval = NumericProperty(0.5)
    click_mode = StringProperty('loop')  # 'loop' 或 'sequence'
    click_times = NumericProperty(1)
    click_count = NumericProperty(0)
    config_file = "click_config_kivy.json"

    def build(self):
        """构建界面"""
        # 主布局
        root = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # 标题
        title = Label(
            text='安卓连点器',
            font_size=24,
            size_hint_y=None,
            height=50,
            bold=True
        )
        root.add_widget(title)

        # 状态显示
        self.status_label = Label(
            text='状态: 就绪',
            font_size=14,
            size_hint_y=None,
            height=30,
            color=[0, 0, 1, 1]  # 蓝色
        )
        root.add_widget(self.status_label)

        # 设置区域
        settings_box = BoxLayout(orientation='vertical', size_hint_y=None, height=200)

        # 点击间隔
        interval_box = BoxLayout(orientation='horizontal', size_hint_y=None, height=40)
        interval_box.add_widget(Label(text='间隔(秒):', size_hint_x=0.3))
        self.interval_value = Label(text='0.50', size_hint_x=0.2)
        interval_box.add_widget(self.interval_value)

        interval_slider = Slider(
            min=0.1,
            max=5.0,
            value=0.5,
            size_hint_x=0.5
        )
        interval_slider.bind(value=self.on_interval_change)
        interval_box.add_widget(interval_slider)
        settings_box.add_widget(interval_box)

        # 点击模式
        mode_box = BoxLayout(orientation='horizontal', size_hint_y=None, height=40)
        mode_box.add_widget(Label(text='模式:', size_hint_x=0.3))
        self.btn_loop = ToggleButton(
            text='循环',
            group='mode',
            size_hint_x=0.35
        )
        self.btn_loop.bind(state=self.on_mode_change)
        mode_box.add_widget(self.btn_loop)

        self.btn_sequence = ToggleButton(
            text='顺序',
            group='mode',
            size_hint_x=0.35
        )
        self.btn_sequence.bind(state=self.on_mode_change)
        mode_box.add_widget(self.btn_sequence)
        settings_box.add_widget(mode_box)

        # 点击次数
        times_box = BoxLayout(orientation='horizontal', size_hint_y=None, height=40)
        times_box.add_widget(Label(text='次数:', size_hint_x=0.3))
        self.times_input = TextInput(
            text='1',
            size_hint_x=0.7,
            font_size=14,
            multiline=False
        )
        times_box.add_widget(self.times_input)
        settings_box.add_widget(times_box)

        root.add_widget(settings_box)

        # 点击点列表区域
        list_label = Label(
            text='点击点列表:',
            font_size=14,
            size_hint_y=None,
            height=30,
            halign='left'
        )
        root.add_widget(list_label)

        # 列表容器
        self.points_container = BoxLayout(orientation='vertical', spacing=5)

        # 滚动视图
        scroll = ScrollView(size_hint=(1, 0.4))
        scroll.add_widget(self.points_container)
        root.add_widget(scroll)

        # 列表操作按钮
        list_btn_box = BoxLayout(orientation='horizontal', size_hint_y=None, height=50)

        btn_add = Button(text='添加点', font_size=14)
        btn_add.bind(on_press=self.add_click_point)
        list_btn_box.add_widget(btn_add)

        btn_clear = Button(text='清空', font_size=14)
        btn_clear.bind(on_press=self.clear_points)
        list_btn_box.add_widget(btn_clear)
        root.add_widget(list_btn_box)

        # 统计信息
        self.stats_label = Label(
            text='已点击: 0 次',
            font_size=14,
            size_hint_y=None,
            height=30
        )
        root.add_widget(self.stats_label)

        # 控制按钮区域
        control_box = BoxLayout(orientation='horizontal', size_hint_y=None, height=60)

        self.btn_start = Button(
            text='开始点击',
            font_size=16,
            background_color=[0, 1, 0, 1]  # 绿色
        )
        self.btn_start.bind(on_press=self.toggle_clicking)
        control_box.add_widget(self.btn_start)

        root.add_widget(control_box)

        # 配置按钮
        config_box = BoxLayout(orientation='horizontal', size_hint_y=None, height=50)

        btn_save = Button(text='保存配置', font_size=14)
        btn_save.bind(on_press=self.save_config)
        config_box.add_widget(btn_save)

        btn_load = Button(text='加载配置', font_size=14)
        btn_load.bind(on_press=self.load_config)
        config_box.add_widget(btn_load)
        root.add_widget(config_box)

        # 使用说明
        help_text = """
使用说明:
1. 点击"添加点"添加点击位置
2. 设置点击间隔和模式
3. 循环模式: 不断重复点击
4. 顺序模式: 按设定次数点击后停止
5. 点击"开始点击"开始连点
        """
        help_label = Label(
            text=help_text,
            font_size=10,
            color=[0.5, 0.5, 0.5, 1],
            size_hint_y=None,
            height=120,
            halign='left',
            text_size=(None, None),
            valign='middle'
        )
        root.add_widget(help_label)

        # 加载配置
        self.load_config()

        # 点击事件
        self.click_event = None

        return root

    def on_interval_change(self, instance, value):
        """间隔滑块变化"""
        self.click_interval = value
        self.interval_value.text = f'{value:.2f}'

    def on_mode_change(self, instance, value):
        """模式切换"""
        if instance == self.btn_loop and value == 'down':
            self.click_mode = 'loop'
        elif instance == self.btn_sequence and value == 'down':
            self.click_mode = 'sequence'

    def add_click_point(self, instance):
        """添加点击点"""
        # 默认添加中心位置
        self.click_points.append((540, 960))
        self.update_points_list()

    def delete_point(self, index):
        """删除指定点击点"""
        if 0 <= index < len(self.click_points):
            del self.click_points[index]
            self.update_points_list()

    def clear_points(self, instance):
        """清空所有点击点"""
        self.click_points = []
        self.update_points_list()

    def update_points_list(self):
        """更新点击点列表"""
        self.points_container.clear_widgets()
        for i, (x, y) in enumerate(self.click_points):
            item = PointItem(i, x, y, self.delete_point)
            self.points_container.add_widget(item)

    def toggle_clicking(self, instance):
        """切换点击状态"""
        if not self.clicking:
            # 开始点击
            if not self.click_points:
                self.show_popup('错误', '请先添加点击点')
                return

            try:
                self.click_times = int(self.times_input.text)
            except ValueError:
                self.show_popup('错误', '请输入有效的点击次数')
                return

            self.clicking = True
            self.click_count = 0
            self.current_index = 0
            self.btn_start.text = '停止点击'
            self.btn_start.background_color = [1, 0, 0, 1]  # 红色
            self.status_label.text = '点击中...'
            self.status_label.color = [0, 1, 0, 1]  # 绿色

            # 开始点击循环
            self.click_event = Clock.schedule_interval(self.click_loop, self.click_interval)

        else:
            # 停止点击
            self.clicking = False
            self.btn_start.text = '开始点击'
            self.btn_start.background_color = [0, 1, 0, 1]  # 绿色
            self.status_label.text = '已停止'
            self.status_label.color = [1, 0, 0, 1]  # 红色

            if self.click_event:
                self.click_event.cancel()
                self.click_event = None

    def click_loop(self, dt):
        """点击循环"""
        # 检查是否应该停止
        if self.click_mode == 'sequence':
            if self.click_count >= self.click_times * len(self.click_points):
                self.toggle_clicking(self.btn_start)
                return

        # 获取当前点击点
        if not self.click_points:
            self.toggle_clicking(self.btn_start)
            return

        x, y = self.click_points[self.current_index]

        # 执行点击（Kivy在桌面不支持，需要Android实现）
        self.perform_click(x, y)

        # 更新计数
        self.click_count += 1
        self.stats_label.text = f'已点击: {self.click_count} 次'

        # 更新索引
        self.current_index = (self.current_index + 1) % len(self.click_points)

        # 如果间隔改变，重新调度
        if self.click_event:
            self.click_event.cancel()
            self.click_event = Clock.schedule_interval(self.click_loop, self.click_interval)

    def perform_click(self, x, y):
        """在指定位置执行点击"""
        # 注意：Kivy本身不提供直接控制屏幕点击的功能
        # 在实际Android应用中，需要使用无障碍服务或其他权限

        # 模拟点击（仅用于演示）
        print(f"点击位置: ({x}, {y})")

        # TODO: 实现实际的屏幕点击功能
        # 可能需要：
        # 1. 使用Android的无障碍服务（AccessibilityService）
        # 2. 或者使用root权限
        # 3. 或者通过ADB连接

    def show_popup(self, title, message):
        """显示弹出框"""
        popup = Popup(
            title=title,
            content=Label(text=message, font_size=14),
            size_hint=(0.8, 0.3)
        )
        popup.open()

    def save_config(self, instance):
        """保存配置"""
        config = {
            'click_points': self.click_points,
            'click_interval': self.click_interval,
            'click_mode': self.click_mode,
            'click_times': self.times_input.text
        }

        try:
            with open(self.config_file, 'w', encoding='utf-8') as f:
                json.dump(config, f, indent=2, ensure_ascii=False)
            self.show_popup('成功', '配置已保存')
        except Exception as e:
            self.show_popup('错误', f'保存失败: {e}')

    def load_config(self, instance=None):
        """加载配置"""
        if not os.path.exists(self.config_file):
            return

        try:
            with open(self.config_file, 'r', encoding='utf-8') as f:
                config = json.load(f)

            self.click_points = config.get('click_points', [])
            self.click_interval = config.get('click_interval', 0.5)
            self.click_mode = config.get('click_mode', 'loop')
            click_times = config.get('click_times', '1')

            # 更新界面
            self.interval_value.text = f'{self.click_interval:.2f}'

            if self.click_mode == 'loop':
                self.btn_loop.state = 'down'
            else:
                self.btn_sequence.state = 'down'

            self.times_input.text = str(click_times)
            self.update_points_list()

        except Exception as e:
            print(f'加载配置失败: {e}')


if __name__ == '__main__':
    AndroidClickerApp().run()
