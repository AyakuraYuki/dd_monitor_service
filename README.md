# dd_monitor

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
    <a href="https://cli.vuejs.org/" target="_blank">
        <img src="https://img.shields.io/badge/vue--cli-3.10.0-brightgreen?logo=vue-cli&style=flat-square" alt="">
    </a>
    <a href="https://vuejs.org/" target="_blank">
        <img src="https://img.shields.io/badge/vue-2.6.10-brightgreen?logo=vue&style=flat-square" alt="">
    </a>
</p>

## Instruction

### Get source codes

```shell script
git clone https://github.com/AyakuraYuki/dd_monitor.git
cd dd_monitor
```

### Get Python and Node.js

> If you already installed both two, you can skip this step.

* Python

    https://www.python.org/downloads/

* Node.js

    https://nodejs.org/en/download/

### Get virtualenv

> If you already installed virtualenv, you can skip this step. For more information of virtualenv, please visit [virtualenv in pypi](https://pypi.org/project/virtualenv/)
>
> Python virtual environments are used to isolate package installation from the system. I highly recommend you to use virtualenv, but if you want to use installed python and pip, I won't stop you.
>
> To continue, make sure you have `Python 3.7.x`.

```shell script
pip install virtualenv
```

### Build environment

If you use virtualenv, run the following script before build the environment.

> `venv` is the folder name of the virtual environment, you can replace with whatever you want. For the example, I will use `venv`.

* Linux/macOS

```shell script
virtualenv venv
source venv/bin/activate
```

* Windows

```powershell
virtualenv venv
venv/Scripts/activate
```

After prepared Python or virtualenv, and Node, use the following scripts to build the environment.

> Here I presented a script called `build.sh` for Linux/macOS, soon I'll make a `build.bat` for Windows users.

```shell script
pip install -r requirements.txt
chmod +x build.sh
./build.sh
```

### Before running

You need to create a sqlite database file, use this script to continue.

```shell script
flask init-schemas
```

### Run

I didn't package this program, I'll do this stuff if I have time to.

```shell script
flask run
```

And now, visit http://127.0.0.1:5140

## 使用指导

### 获取源代码

```shell script
git clone https://github.com/AyakuraYuki/dd_monitor.git
cd dd_monitor
```

### 获取Python和Node.js

> 如果你已经安装了，你可以跳过这一步

* Python

    https://www.python.org/downloads/

* Node.js

    https://nodejs.org/en/download/

### 获取virtualenv

> 如果你已经安装了virtualenv， 你可以跳过这一步。想知道更多关于virtualenv的信息，可以访问[virtualenv in pypi](https://pypi.org/project/virtualenv/)。
>
> Python虚拟环境被用来将安装的依赖包从系统中隔离出来，我强烈建议你使用virtualenv，但是如果你一定要用本地的Python和pip，我不会阻止你的。
>
> 在继续之前，确保你安装的Python大于3.7.x版本

```shell script
pip install virtualenv
```

### 构建环境

如果你是用virtualenv，在构建环境之前，你需要执行下面的脚本。

> `venv`是virtualenv环境的目录名称，你可以替换成你想要的任何名称，这里为了举例我选用了`venv`

* Linux/macOS

```shell script
virtualenv venv
source venv/bin/activate
```

* Windows

```powershell
virtualenv venv
venv/Scripts/activate
```

当你准备好Python或者virtualenv，以及Node之后，用下面的脚本构建运行环境

> 这里我为Linux/macOS用户准备了`build.sh`构建运行环境，之后我会很快为Windows用户准备`build.bat`

```shell script
pip install -r requirements.txt
chmod +x build.sh
./build.sh
```

### 运行之前

运行之前你需要用下面的命令创建sqlite存储库

```shell script
flask init-schemas
```

### 运行

我还没有打包这个工具，如果我有时间我会去做的，现在暂时用flask直接运行

```shell script
flask run
```

然后访问 http://127.0.0.1:5140 即可
