# README

* * *

## 文件说明

| 文件名 | 内容 |
| --- | --- |
| extend1 | 拓展一 |
| extend2 | 拓展二 |
| extend3 | 拓展三 |
| extend4 | 拓展四 |
| origin|原始实验|

* * *

## 工具安装说明

### 基础实验配置方法

* * *

1. 安装virtualbox，配置虚拟机环境

>virtualbox下载地址:
>https://www.virtualbox.org/wiki/Downloads

2. 下载seedubuntu虚拟机

>http://www.cis.syr.edu/~wedu/seed/lab_env.html

3. 安装相关工具

>ida: 下载地址: https://pan.baidu.com/s/1c3R6iZY 密码: tvsn
>gdb: 终端下输入命令sudo apt-get install gdb

4. 阅读实验指导书

>http://www.cis.syr.edu/~wedu/seed/Labs_16.04/Software/Return_to_Libc/Return_to_libc.pdf

* * *
### 拓展实验配置方法

* * *

#### 环境的搭建

* * *

1. Ubuntu16.04 64位

>下载地址：
>http://releases.ubuntu.com/16.04/ubuntu-16.04.5-desktop-amd64.iso

2. 在virtual下安装16.04虚拟机教程

>https://blog.csdn.net/u012732259/article/details/70172704/

* * *

#### 工具的准备

* * *

1. IDA

>交互式反汇编器专业版（Interactive Disassembler Professional），人们常称其为IDA Pro，或简称为IDA。是目前最棒的一个静态反编译软件，为众多0day世界的成员和ShellCode安全分析人士不可缺少的利器！
>下载地址: https://pan.baidu.com/s/1c3R6iZY 密码: tvsn

2. GDB

>UNIX及UNIX-like下的调试工具。或许，各位比较喜欢那种图形界面方式的，像VC、BCB等IDE的调试，但如果你是在 UNIX平台下做软件，你会发现GDB这个调试工具相比于VC、z的优点是具有修复网络断点以及恢复链接等功能，比BCB的图形化调试器有更强大的功能。
>安装方法：ubuntu命令行下输入sudo apt-get install gdb

3. ROPgadget:

>此工具可让您在二进制文件中搜索gadget，以方便您的ROP利用。 ROPgadget支持x86，x64，ARM，ARM64，PowerPC，SPARC和MIPS架构上的ELF / PE / Mach-O格式。
>安装方法：命令行下输入pip install ROPgadget

4. pwntools

>pwntools是一个CTF框架和漏洞利用开发库，用Python开发，由rapid设计，旨在让使用者简单快速的编写exploit。
>安装地址：https://github.com/Gallopsled/pwntools

5. libc-database

>根据已知的函数偏移查找对应的libc。
>安装地址：https://github.com/niklasb/libc-database

6. gcc

>GNU编译器套件（GNU Compiler Collection）包括C、C++、Objective-C、Fortran、Java、Ada和Go语言的前端，也包括了这些语言的库（如libstdc++、libgcj等等）。
>安装方法：命令行下输入sudo apt-get install gcc

7. binutils

>GNU binutils是一组二进制工具集,包含strings、objdump等常用工具。
>安装方法：命令行下输入sudo apt-get install binutils

* * *



