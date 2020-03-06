const { app, BrowserWindow } = require("electron")
const fs = require('fs')
const exec = require('child_process').exec
const downloadGitRepo = require('download-git-repo')
const log = require('electron-log')

// constant
const appPath = app.getPath('userData')
const appCorePath = `${appPath}/core`
const logFolder = `${appPath}/logs`

// logger
export const logPath = `${logFolder}/dd-monitor.log`
log.transports.file.file = logPath
log.transports.file.format = '{y}-{m}-{d} {h}:{i}:{s}:{ms} [{level}] {text}'
log.transports.file.maxSize = 5 * 1024 * 1024
log.transports.file.level = 'info'
log.transports.console.format = '{y}-{m}-{d} {h}:{i}:{s}:{ms} [{level}] {text}'
if (process.env.NODE_ENV === 'dev') {
    log.transports.console.level = 'debug'
} else {
    log.transports.console.level = 'info'
}

let win

function initCore() {
    log['debug'](`appPath: ${appPath}`)
    log['debug'](`appCorePath: ${appCorePath}`)

    if (fs.existsSync(appCorePath)) {
        let pathStat = fs.statSync(appCorePath)
        if (!(pathStat.isDirectory())) {
            fs.unlinkSync(appCorePath)
            downloadGitRepo(`AyakuraYuki/dd_monitor#backend`, appCorePath, err => {
                log[err ? 'error' : 'info'](`Core download ${err ? 'error' : 'success'}`)
            })
        }
    } else {
        downloadGitRepo(`AyakuraYuki/dd_monitor#backend`, appCorePath, err => {
            log[err ? 'error' : 'info'](`Core download ${err ? 'error' : 'success'}`)
        })
    }
}

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
    initCore()
    createWindow()
})

app.on("before-quit", () => {

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

// app.on("quit", () =>
//     exec("ps -ef | grep 'python run-dd-monitor.py' | grep -v grep | awk '{print $2}' | xargs kill")
// )

// function sleep(delay) {
//     const start = (new Date()).getTime();
//     while ((new Date()).getTime() - start < delay) {
//         // DO NOTHING
//     }
// }
