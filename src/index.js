const { app, BrowserWindow } = require("electron")
const fs = require('fs')
const downloadGitRepo = require('download-git-repo')
const log = require('electron-log')
const cp = require('child_process')
const path = require('path')


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


function runCommand(command) {
    return new Promise(resolve => {
        if (command) {
            try {
                cp.exec(command, () => {
                    resolve()
                })
            } catch (error) {
                log['error'](error)
                resolve()
            }
        } else {
            resolve()
        }
    })
}


// core
let coreInstance

function downloadCore() {
    return new Promise((resolve) => {
        downloadGitRepo(`AyakuraYuki/dd_monitor#backend`, appCorePath, {}, err => {
            log[err ? 'error' : 'info'](`Core download ${err ? 'error' : 'success'}`)
            resolve()
        })
    })
}

async function runPythonCore() {
    try {
        let command = 'python3'
        const params = [path.join(appCorePath, 'run-dd-monitor.py')]
        params.push('--port')
        params.push('5140')

        const commandStr = `${command} ${params.join(' ')}`
        log['debug'](`run command: ${commandStr}`)

        if (platform === 'win32') {
            let _path = process.env.path
            coreInstance = cp.execFile(command, params, {
                cwd: appCorePath,
                env: {
                    path: _path
                }
            })
        } else {
            coreInstance = cp.execFile(command, params, { cwd: appCorePath })
        }

        coreInstance.stdout.on("data", chunk => {
            log['debug'](chunk)
        })
        coreInstance.stderr.on("data", chunk => {
            // some flask logs have been marked as the error level
            log['debug'](`[core info] ${chunk}`)
        })
        coreInstance.once("exit", code => {
            log['info'](`Core exit with code ${code}`)
            coreInstance = null
        })
    } catch (error) {
        log['error']('Core check failed, cause:')
        log['error'](error)
        app.quit()
    }
}

async function buildCoreEnv() {
    const params = ['install', '-r', path.join(appCorePath, 'requirements.txt')]
    try {
        cp.execFile('pip3', params, { cwd: appCorePath }, err => {
            log['error'](err)
        })
    } catch (error) {
        log['error']('Core runtime check failed, cause:')
        log['error'](error)
        log['info']('pip not found, try to install requirements by using pip3')

        try {
            cp.execFile('pip', params, { cwd: appCorePath }, err => {
                log['error'](err)
            })
        } catch (innerError) {
            log['error']('Core runtime check failed, cause:')
            log['error'](innerError)
            app.quit()
        }
    }
}

async function initCore() {
    if (fs.existsSync(appCorePath)) {
        let pathStat = fs.statSync(appCorePath)
        if (!(pathStat.isDirectory())) {
            fs.unlinkSync(appCorePath)
            await downloadCore()
            await buildCoreEnv()
        }
    } else {
        await downloadCore()
        await buildCoreEnv()
    }
    await runPythonCore()
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
    runCommand("ps -ef | grep 'run-dd-monitor.py' | grep -v 'grep' | awk '{print $2}' | xargs kill")
        .then(() => {
            log['info']('Core closed')
        })
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
