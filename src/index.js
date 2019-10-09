const {app, BrowserWindow} = require("electron")

function sleep(delay) {
    const start = (new Date()).getTime();
    while ((new Date()).getTime() - start < delay) {
    }
}

function createWindow() {
    let win = new BrowserWindow({
        width: 1600,
        height: 1080
    })
    sleep(2000)
    win.loadFile("./main.js")
        .then(() => console.log('win.loaded'))
}

app.on("ready", createWindow)
// app.on("quit", () =>
//     exec("ps -ef | grep 'python run-dd-monitor.py' | grep -v grep | awk '{print $2}' | xargs kill")
// )
