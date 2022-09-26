python运行指南：
osuBeatmapDownloader 是一个利用python爬取以下网站获得谱面信息：
https://osu-pps.com/#/mania/maps
https://osu-pps.com
随后调用以下镜像站进行下载：
https://chimu.moe/zh-CN/beatmaps
https://kitsu.moe/
http://v.osu.sh/home/new
基于chromedriver和selenium库进行筛选并且批量下载谱面的python程序。

第一步：
       双击'''bat'''文件安装所需库(前提是你得有个python)
       没有python(?)
       (https://www.python.org/)
       配置教程请自行搜索学习，更推荐使用pycharm和anacoda(也可以搜一搜)

第二步：
       在 https://chromedriver.chromium.org/downloads
       下载您当前浏览器版本的chromedriver
       配置方法可以参照以下网址
        (https://blog.csdn.net/zhoukeguai/article/details/113247342)
       PC上没有Chrome(?) 
       (https://www.google.cn/chrome/)

第三步：
       首先进入config/setting.py，修改web_selection参数，选择对应的筛选器网页。
       首先运行__init__.py，输入1启动谱面抓取，然后会弹出的页面，然后设置网页上的筛选器。
       包括且不限于Gamemode模式、Star难度、Length长度（单位是秒）、CS / Mania keys（重要）、风格、语言等等。
       om玩家务必记得选自己要打几键的谱和Mania选项。
       然后根据python的提示从头到尾完全运行程序。
       最后程序会将下载链接、铺面信息等信息保存至download_xml中，可以选择不同的镜像源下载。

下载1——使用自带下载器的办法：
       使用任意下载器的批量下载功能（推荐IDM：Internet Download Manager），
       选择download_xml文件夹中chimu，kit，v_osu（同sayobot）开头的任意txt文件即可开始批量下载。
       下载完成后可以把所有谱面一口气拖入ous!/Songs/中，进入游戏后刷新即可。
       运行过init.py后，这个文件夹中会生成一个download_xml的文件夹，里面会保存您每次爬取的谱面的信息。
       当您想要重新下载以前筛选过的谱面数据或者运行了__init__.py但是没有当场下载的时候，
       您可以用任意下载器重新开始下载。

下载2——不使用下载器，使用Chrome网页下载器的办法：
       打开beatmaps_xml，将其完整路径赋值给config/setting.py中的DownloadPath 。
       config/setting.py中的PauseTime可以设置每个下载任务之间的添加间隔。
       最后需要修改下载器选项DownloadStyle选择Chrome下载。
       设置完毕后重新运行__init__.py，选择0启动下载器，根据python的输出，选择之前保存的xlsx文件的名称。

下载3——不使用下载器，使用Python程序下载器的办法：
       fileNumber为此项下载专用，意思为同时开始下载的谱面数量。
       更改config/Setting.py中的选项DownloadStyle为该下载器， download_xml中有任意xlsx文件时可用，运行init.py，按照指示输入即可开始下载。
       下载好的谱面将会保存在beatmaps_xml中。

注意事项：
       使用下载2时候，判断下载是否完成的依据是Chrome下载路径download_xml下是否存在''.crdownload''文件和''.tmp''文件,
       若要使用下载2请在下载前删除该路径下的这类文件（夹），
       下载路径中若存在包含这两个英文字段的文件/夹都会导致下载完成无法跳出（仍然可以手动关闭）。

       使用下载3时，如果将fileNumber的值设置的很大会占用很多内存，有可能会导致崩溃或者下载失败，请知悉。
       遇到任何问题可以使用Ctrl + C打断程序运行。


       
