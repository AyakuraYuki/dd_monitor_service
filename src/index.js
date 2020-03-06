const { app, BrowserWindow } = require("electron")
// const appConfigDir = app.getPath('userData')
// const appCoreDownloadDir = `${appConfigDir}/dd_monitor_core`

let win

function sleep(delay) {
    const start = (new Date()).getTime();
    while ((new Date()).getTime() - start < delay) {
        // DO NOTHING
    }
}

function createWindow() {
    win = new BrowserWindow({
        width: 1600,
        height: 1080,
    })

    sleep(100)

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

app.on("ready", createWindow)

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
