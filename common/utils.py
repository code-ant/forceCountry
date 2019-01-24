import time


def sleep_count(seconds):
    for i in range(seconds, -1, -1):
        print('\r', '倒计时 %s 秒！' % str(i).zfill(3), end='')
        time.sleep(1)
    print('\r', '{:^20}'.format('计时结束！'))
