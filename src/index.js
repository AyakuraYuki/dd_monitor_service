const { app, BrowserWindow } = require("electron")
const fs = require('fs')
const downloadGitRepo = require('download-git-repo')
const log = require('electron-log')
const { exec } = require('child_process')


// platform
const platform = process.platform


// constant

// macOS: "${HOME}/Library/Application Support/dd_monitor"
// windows & linux: "<exec_dir>"
const appPath = platform === 'darwin' ? app.getPath('userData') : process.cwd()
const appCorePath = `${appPath}/core`


// logger
const logPath = `${appPath}/logs`
log.transports.file.file = `${logPath}/dd-monitor.log`
log.transports.file.format = '{y}-{m}-{d} {h}:{i}:{s}:{ms} [{level}] {text}'
log.transports.file.maxSize = 5 * 1024 * 1024
log.transports.file.level = 'info'
log.transports.console.format = '{y}-{m}-{d} {h}:{i}:{s}:{ms} [{level}] {text}'
if (process.env.NODE_ENV === 'dev') {
    log.transports.console.level = 'debug'
} else {
    log.transports.console.level = 'info'
}


// core
let cmdStr = `./run.sh`
let workerProcess

function downloadCore() {
    return new Promise((resolve, reject) => {
        downloadGitRepo(`AyakuraYuki/dd_monitor#backend`, appCorePath, {}, err => {
            log[err ? 'error' : 'info'](`Core download ${err ? 'error' : 'success'}`)

            let pipProcess = exec('pip install -r requirements.txt', { cwd: appCorePath })

            pipProcess.stdout.on("data", (data) => {
                log['debug'](data)
            })
            pipProcess.stderr.on("data", (data) => {
                log['error'](data)
                reject()
            })
            pipProcess.on("exit", (code, signal) => {
                log['info'](`Core init complete. exit(${code})[${signal}]`)
                resolve()
            })
        })
    })
}

async function runExec() {
    workerProcess = exec(cmdStr, { cwd: appCorePath })

    workerProcess.stdout.on("data", (data) => {
        log['debug'](`core info ===== ${data}`)
    })
    workerProcess.stderr.on("data", (data) => {
        log['error'](`core exception ===== ${data}`)
    })
    workerProcess.on("close", (code, signal) => {
        log['info'](`core close ===== [code: ${code}] [signal: ${signal}]`)
    })
}

async function initCore() {
    if (fs.existsSync(appCorePath)) {
        let pathStat = fs.statSync(appCorePath)
        if (!(pathStat.isDirectory())) {
            fs.unlinkSync(appCorePath)
            await downloadCore()
        }
    } else {
        await downloadCore()
    }
    await runExec()
}


// application and window
let win

function createWindow() {
    win = new BrowserWindow({
        width: 1600,
        height: 1080,
    })

    win.loadFile('./dist/index.html')
        .then(() => {
        })
        .catch((e) => {
            console.log(e)
        })

    win.on('close', () => {
        win = null
    })
}

app.on("ready", () => {
    initCore().then(createWindow)
})

app.on("before-quit", () => {
    exec("ps -ef | grep 'run-dd-monitor.py' | grep -v 'grep' | awk '{print $2}' | xargs kill")
    log['info']('bye')
})

app.on('window-all-closed', () => {
    if (process.platform !== 'darwin') {
        app.quit()
    }
})

app.on('activate', () => {
    if (win === null) {
        createWindow()
    }
})

// function sleep(delay) {
//     const start = (new Date()).getTime();
//     while ((new Date()).getTime() - start < delay) {
//         // DO NOTHING
//     }
// }
