# dd_monitor

> Here's a genius who made a more functional [DD Monitor](https://github.com/zhimingshenjun/DD_Monitor), pls go check it.

> As a reminder, you are looking at the `backend` branch, I split the master branch to the frontend and the backend, make it easy for me to maintain.
> 
> 在这里提醒一下，你现在查看的是后端的部分，我将master分支拆分成前端部分和后端部分，让我维护起来更轻松。

DD monitor, which means a monitor for DDs (DD means `誰でも大好き`), can let you watch multiple YouTube streams (if the stream is enabled to be embedded outside YouTube) in one screen at the same time.

In the beginning, I was planning to see the multi-view of Hololive's Project Winter collab streams, but it is very difficult to allocate space for browsers. So I decide to build this program to make things easier.

When I noticed that hey if I can use YouTube embed link, I can watch not only the Project Winter streams but also every stream which supports to play outside YouTube.

So this is it, a simple but functionally DD monitor.

DD监视器，你要来当监视房里的老大爷吗？这个工具可以让你同时观看多个（允许在YouTube外部播放的）油管直播。

一开始的时候我打算看当时Hololive的Project Winter联动直播，但是一起8个视角，给浏览器分配空间太难了。所以我决定搞一个工具来把事情变得容易解决。

然而当我注意到，当我使用油管的外部嵌入链接时，我不但可以用来看Project Winter联动直播，还可以看任何支持在油管外播放的直播。

所以，这就是一个简单但很好用的DD监视器。

## Environment

<p>
    <a href="https://www.python.org/" target="_blank">
        <img src="https://img.shields.io/badge/Python-3.7.4-blue?logo=python&style=flat-square" alt="">
    </a>
    <a href="https://palletsprojects.com/p/flask/" target="_blank">
        <img src="https://img.shields.io/badge/Flask-1.1.1-blue?logo=flask&style=flat-square" alt="">
    </a>
    <a href="https://www.sqlite.org/index.html" target="_blank">
        <img src="https://img.shields.io/badge/sqlite3-3.24.0-green?logo=sqlite&style=flat-square" alt="">
    </a>
</p>

## Instruction

### Get source codes

```bash
git clone https://github.com/AyakuraYuki/dd_monitor.git
cd dd_monitor
```

If you are in `master` branch, continue to run the following script:

```bash
git checkout backend
```

### Get Python

> If you already installed python, you can skip this step.
>
> Make sure you have (or download and install) `Python >= 3.7`.

* Python

    https://www.python.org/downloads/

### Get virtualenv

> Python virtual environments are used to isolate package installation from the system. For more information of `virtualenv`, please visit [virtualenv in pypi](https://pypi.org/project/virtualenv/)
>
> If you already installed `virtualenv`, you can skip this step.
>
> I highly recommend you to use `virtualenv`, but if you want to use installed `python` and `pip`, I won't stop you.

```bash
pip install virtualenv
```

### Build environment

#### If you use `virtualenv`, run the following script before build the environment.

> `venv` is the folder name of the virtual environment, you can replace with whatever you want. For the example, I will use `venv`.

* Linux/macOS

```bash
virtualenv venv
source venv/bin/activate
```

* Windows

```powershell
virtualenv venv
venv/Scripts/activate
```

#### After prepared `python`, use the following scripts to setup environment.

```bash
pip install -r requirements.txt
```

### Run

> Sorry guys, I didn't make the release version. I'll do this stuff if I have time to.

```bash
chmod +x run.sh
./run.sh
```

And now, try `curl "http://localhost:5140/player/list"`. Port `5140` is the default port I used.

## 使用指导

### 获取源代码

```bash
git clone https://github.com/AyakuraYuki/dd_monitor.git
cd dd_monitor
```

如果你正处于`master`分支下，请继续执行下面的命令，切换到后端分支：

```bash
git checkout backend
```

### 获取Python

> 如果你已经安装了，你可以跳过这一步。
>
> 在继续之前，确保你安装的Python大于版本3.7.x。

* Python

    https://www.python.org/downloads/

### 获取virtualenv

> Python虚拟环境被用来将安装的依赖包从系统中隔离出来。想知道更多关于`virtualenv`的信息，可以访问[virtualenv in pypi](https://pypi.org/project/virtualenv/)。
>
> 如果你已经安装了`virtualenv`，你可以跳过这一步。
>
> 我强烈建议使用`virtualenv`，但是如果你一定要用本地的`python`和`pip`，也是可以的。

```bash
pip install virtualenv
```

### 构建环境

如果你是用`virtualenv`，在构建环境之前，你需要执行下面的脚本。

> `venv`是`virtualenv`环境的目录名称，你可以替换成你想要的任何名称，这里为了举例我选用了`venv`

* Linux/macOS

```bash
virtualenv venv
source venv/bin/activate
```

* Windows

```powershell
virtualenv venv
venv/Scripts/activate
```

#### 当你准备好后，用下面的脚本构建运行环境

```bash
pip install -r requirements.txt
```

### 运行

> 我还没有打包发布版本，如果我有时间我会去做的。

```bash
chmod +x run.sh
./run.sh
```

现在，你可以尝试在shell中输入`curl "http://localhost:5140/player/list"`来获取播放列表了。端口`5140`是程序的默认端口。

## TODO

* Release version
