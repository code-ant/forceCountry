import os
import random
from common.utils import sleep_count


def short_wait():
    sleep_count(random.randrange(2, 3))
    print("模拟人操作断延时，随机延迟2-3秒")


def long_wait():
    sleep_count(random.randrange(3, 5))
    print("模拟人操作长延时，随机延迟3-5秒")


# adb路径
adb_path = 'adb'
adb_path = os.path.join('"D:\\', 'Program Files', 'Microvirt', 'MEmu', 'adb.exe"')
# memuc路径
memuc_path = 'memuc'
memuc_path = os.path.join('"D:\\', 'Program Files', 'Microvirt', 'MEmu', 'memuc.exe"')


# 阅读文章
def read_article():
    # 订阅号选择
    touch('963', '1806')
    touch('435', '83')
    # 选择新华社
    touch('83', '306')
    # 文章
    article_cates = ['65 389', '170 667', '280 945', '425 1223', '555 1501']
    for index in range(len(article_cates)):
        # 选择文章
        touch(article_cates[index], '')
        print('阅读第' + str(index) + '篇文章')
        swipe_article()
        collect()
        send_comment('赞！')
        share()
        back_previous_page()
    back_previous_page()
    back_previous_page()


# 滑动文章
def swipe_article():
    # 滑动文章内容
    for ti in range(5):
        swipe('545', '1760', '545', '280', '500', '阅读文章')
        print('滑动一屏内容………………')
    # 防止文章过长看不完
    touch('852', '1889')


# 返回
def back_previous_page():
    os.popen(adb_path + ' shell input tap 38 80')
    short_wait()
    print('操作完成，返回上一页')


# 评论
def send_comment(string):
    # 评论输入框
    touch('463', '1889')
    # 输入内容
    input_word(string)
    # 发表按钮
    touch('1024', '1792')
    print('发表观点成功………………')


# 模拟触摸
def touch(x, y):
    os.popen(adb_path + ' shell input tap ' + x + ' ' + y)
    short_wait()
    print('模拟触摸:(' + x + ',' + y + ')')


# 滑动
def swipe(x1, y1, x2, y2, swipe_time, location):
    os.popen(adb_path + ' shell input swipe ' + x1 + ' ' + y1 + ' ' + x2 + ' ' + y2 + ' ' + swipe_time)
    long_wait()
    return '窗口:' + location + '滑动屏幕:从（' + x1 + ',' + y1 + ')到(' + x2 + ',' + y2 + ').用时:' + swipe_time + 'ms'


# 收藏
def collect():
    touch('940', '1890')
    print('收藏成功')


# 分享
def share():
    touch('1027', '1890')
    print('分享按钮')
    touch('130', '1426')
    print('分享到站内')
    touch('185', '555')
    print('分享给小助手')
    input_word("666")
    touch('867', '1128')
    print('分享成功')


# 输入文字
def input_word(string):
    input_cmd = os.popen(memuc_path + ' -i 0 input "' + string + '"')
    result = input_cmd.read()
    short_wait()
    print('输入文字:' + string + ' ' + result)


# 视频
def videos():
    # 选择视频板块
    touch('756', '1865')
    print('进入视频页面')
    touch('380', '167')
    print('进入新闻联播频道')
    '''
    使用新闻联播板块，其他板块不统一，无法批量处理
    此模块视频长度大部分在5分钟以内，所以此处设置5分钟，应该不会有太大影响
    '''
    video_cates = ['167 1037', '167 1204', '167 1363', '167 1500', '167 1648']
    for index in range(len(video_cates)):
        # 选择文章分类
        play(video_cates[index], '')
        print('播放第' + str(index) + '个视频')


# 播放
def play(x, y):
    touch(x, y)
    print('开始播放')
    # 等待视频播放完成
    sleep_count(300)
    print('播放完成')
    # 返回列表
    back_previous_page()


# 返回文章页面停留一小时
def back_to_article():
    init_app()
    # 选择第一篇文章
    touch('248', '363')
    print('开始每天一小时积分×2')
    sleep_count(60*60)


def init_app():
    touch('545', '1865')
    print('初始化……………………')
    long_wait()
    print('初始化完成…………………………')


def main():
    init_app()
    print('adb路径:' + adb_path)
    print('memuc路径:' + memuc_path)
    read_article()
    videos()
    back_to_article()
    print('今日任务已完成')


if __name__ == '__main__':
    main()
