#/usr/bin/env python
# -*- coding:utf-8 -*-
# Power by HPCM 2019-05-16 10:48:09
import psutil

# print(psutil.cpu_times())
# print(psutil.cpu_count())
# print(psutil.pids())

# print(psutil.test())    # 类似ps命令显示的结果
# print(psutil.cpu_times()) # 执行代码花费在内核/用户空间的时间
# for x in range(3):
#     print(psutil.cpu_percent(interval=0.1, percpu=True)) # 获取cpu当前占用百分比, percpu=True,表示每个cpu的百分比
# for x in range(3):
#     print(psutil.cpu_times_percent(interval=1, percpu=False)) # 获取cpu执行消耗时间, 意思类似cpu_time()
# print(psutil.cpu_count(logical=False))  # 获取cpu核数, logincal=False,则排除超线程cpu
# print(psutil.Process().cpu_affinity())  # 获取可用的CPU个数
# print(psutil.cpu_stats())  # cpu切换/中断/调用次数统计
# print(psutil.cpu_freq(percpu=True))  # cpu主频检测
# print(psutil.getloadavg())  # cpu执行与等待的进程个数的负载
# print(psutil.virtual_memory())  # 内存使用信息
# print(psutil.swap_memory())  # 交换内存信息
# print(psutil.disk_partitions(all=False))   # 获取系统分区/挂载点/盘符类型, all是否忽略/dev等内存分区
# print(psutil.disk_usage("/"))     # 获取磁盘使用情况
# print(psutil.disk_io_counters(perdisk=False, nowrap=False))  # 测试
for i in psutil.net_io_counters(pernic=True).items():
    print(i)
for i in psutil.net_connections():
    print(i)
