import math
import random


def slide_track(offset):
    """
    根据输入的偏移值生成一个轨迹数组

    :param offset: 偏移值
    :return: 轨迹数组
    """
    trajectory = []
    length = max(20, int(offset / 10))  # 动态调整轨迹点的数量
    z_interval = 100  # z 值的间隔

    for i in range(length):
        # 计算 z 值
        z = i * z_interval + (i // 10) * 10

        # 计算 x 和 y 值
        if i == 0:
            x = 0
            y = 0
        elif i < 5:
            x = 0
            y = 0
        elif i < 10:
            x = 0
            y = 0
        elif i < 15:
            x = math.floor(i * offset / length)
            y = 1
        else:
            x = offset
            y = -math.floor((i - 15) * 10)

        # 添加到轨迹数组
        trajectory.append([x, y, z])

    # 调整最后几个点
    if len(trajectory) >= 5:
        trajectory[-5][0] = offset
        trajectory[-5][1] = -15
        trajectory[-4][0] = offset
        trajectory[-4][1] = -15
        trajectory[-3][0] = offset
        trajectory[-3][1] = -15
        trajectory[-2][0] = offset
        trajectory[-2][1] = -14
        trajectory[-1][0] = offset
        trajectory[-1][1] = -13

    return trajectory, trajectory[-1][2]


def __ease_out_expo(sep):
    '''
        轨迹相关操作
    '''
    if sep == 1:
        return 1
    else:
        return 1 - pow(2, -10 * sep)


def get_slide_track(distance):
    """
    根据滑动距离生成滑动轨迹
    :param distance: 需要滑动的距离
    :return: 滑动轨迹<type 'list'>: [[x,y,t], ...]
        x: 已滑动的横向距离
        y: 已滑动的纵向距离, 除起点外, 均为0
        t: 滑动过程消耗的时间, 单位: 毫秒
    """

    if not isinstance(distance, int) or distance < 0:
        raise ValueError(f"distance类型必须是大于等于0的整数: distance: {distance}, type: {type(distance)}")
    # 初始化轨迹列表
    slide_track = [
        # [random.randint(-50, -10), random.randint(-50, -10), 0],
        [0, 0, 0],
    ]
    # 共记录count次滑块位置信息
    count = 10 + int(distance / 2)
    # 初始化滑动时间
    t = random.randint(50, 100)
    # 记录上一次滑动的距离
    _x = 0
    _y = 0
    for i in range(count):
        # 已滑动的横向距离
        x = round(__ease_out_expo(i / count) * distance)
        # y = round(__ease_out_expo(i / count) * 14)
        # 滑动过程消耗的时间
        t += random.randint(10, 50)
        if x == _x:
            continue
        slide_track.append([x, _y, t])
        _x = x
    slide_track.append(slide_track[-1])
    return slide_track, slide_track[-1][2]


print(get_slide_track(100))
