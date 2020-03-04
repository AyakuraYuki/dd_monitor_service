# dd_monitor

> As a reminder, you are looking at the `frontend` branch, I split the master branch to the frontend and the backend, make it easy for me to maintain.
> 
> 在这里提醒一下，你现在查看的是前端的部分，我将master分支拆分成前端部分和后端部分，让我维护起来更轻松。

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
    <a href="https://cli.vuejs.org/" target="_blank">
        <img src="https://img.shields.io/badge/vue--cli-3.10.0-brightgreen?logo=vue-cli&style=flat-square" alt="">
    </a>
    <a href="https://vuejs.org/" target="_blank">
        <img src="https://img.shields.io/badge/vue-2.6.10-brightgreen?logo=vue&style=flat-square" alt="">
    </a>
</p>

## Instruction

### Get source codes

```bash
git clone https://github.com/AyakuraYuki/dd_monitor.git
cd dd_monitor
git checkout ui
```

### Get Node.js

> If you already installed, you can skip this step.

* Node.js

    https://nodejs.org/en/download/

### Build environment

```bash
npm install
```

### Run

```bash
npm run serve
```

## 使用指导

### 获取源代码

```bash
git clone https://github.com/AyakuraYuki/dd_monitor.git
cd dd_monitor
git checkout ui
```

### 获取Node.js

> 如果你已经安装了，你可以跳过这一步

* Node.js

    https://nodejs.org/en/download/

### 构建环境

```bash
npm install
```

### 运行

```bash
npm run serve
```

## TODO

* Do electron.js support and packaging...
