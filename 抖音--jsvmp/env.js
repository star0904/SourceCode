const { JSDOM } = require('jsdom');

// 创建虚拟 DOM
const dom = new JSDOM(`<!DOCTYPE html><html><body></body></html>`);
const doc = dom.window.document;


function watch(obj, name) {
    return new Proxy(obj, {
        get: function (target, property, receiver) {
            try {
                if (typeof target[property] === 'function') {
                    console.log("对象 => " + name + "，读取属性：" + property + "，值为：" + "function" + "，类型为：" + (typeof target[property]))
                } else {
                    console.log("对象 => " + name + "，读取属性：" + property + "，值为：" + target[property] + "，类型为：" + (typeof target[property]))
                }
            } catch (e) {
            }
            return target[property]
        },
        set: function (target, property, newValue, receiver) {
            try {
                console.log("对象 => " + name + "，设置属性：" + property + "，值为：" + newValue + "，类型为：" + (typeof newValue))
            } catch (e) {
            }
            return Reflect.set(target, property, newValue, receiver)
        }
    })
}



function get_enviroment(proxy_array) {
    for (var i = 0; i < proxy_array.length; i++) {
        handler = '{\n' +
            '    get: function(target, property, receiver) {\n' +
            '        console.log("方法:", "get  ", "对象:", ' +
            '"' + proxy_array[i] + '" ,' +
            '"  属性:", property, ' +
            '"  属性类型:", ' + 'typeof property, ' +
            // '"  属性值:", ' + 'target[property], ' +
            '"  属性值类型:", typeof target[property]);\n' +
            '        return target[property];\n' +
            '    },\n' +
            '    set: function(target, property, value, receiver) {\n' +
            '        console.log("方法:", "set  ", "对象:", ' +
            '"' + proxy_array[i] + '" ,' +
            '"  属性:", property, ' +
            '"  属性类型:", ' + 'typeof property, ' +
            // '"  属性值:", ' + 'target[property], ' +
            '"  属性值类型:", typeof target[property]);\n' +
            '        return Reflect.set(...arguments);\n' +
            '    }\n' +
            '}'
        eval('try{\n' + proxy_array[i] + ';\n'
            + proxy_array[i] + '=new Proxy(' + proxy_array[i] + ', ' + handler + ')}catch (e) {\n' + proxy_array[i] + '={};\n'
            + proxy_array[i] + '=new Proxy(' + proxy_array[i] + ', ' + handler + ')}')
    }
}

proxy_array = ['window', 'document', 'location', 'navigator', 'history', 'screen']


window = globalThis;
window.self = window;
window.top = window;
window.outerWidth = 1707;
window.outerHeight = 1027;
window.innerWidth = 468;
window.innerHeight = 854;

window.onwheelx = {
    "_Ax": "0X21"
}
window._sdkGlueVersionMap = {
    "sdkGlueVersion": "1.0.0.64-fix.01",
    "bdmsVersion": "1.0.1.19-fix.01",
    "captchaVersion": "4.0.10"
}
window.requestAnimationFrame = function () { }
window.XMLHttpRequest = function () { }
window.XPathResult = function () { }
window.addEventListener = function (args) {
    console.log("window.addEventListener ===>", args)
    if (args === 'deviceorientation') {
        return;
    }
}
window.HTMLElement = function () { }
window.EventSource = function () { }
window.fetch = function () { }
window.requestAnimationFrame = function () { }
window.setTimeout = function () { }
window.setInterval = function () { }
window.Audio = function () { }
window.Image = function () { }
window.CanvasRenderingContext2D = function () { }

XMLHttpRequest = require('xhr2');
XMLHttpRequest.prototype.send = function () { }
XMLHttpRequest.prototype.open = function () { }



function Document() { }
Document.prototype.all = {}
Document.prototype.addEventListener = window.addEventListener;
Document.prototype.createElement = function (args) {
    console.log("document.createElement ===>", args)
    if (args === 'span') {
        return doc.createElement('span');
    }
}
Document.prototype.documentElement = function (args) {
    console.log("document.documentElement ===>", args)
}
Document.prototype.createEvent = function (args) {
    console.log("document.createEvent ===>", args)
}
Document.prototype.createElementNS = function (args) {
    console.log("document.createElementNS ===>", args)
}


function HTMLDocument() { }
Object.setPrototypeOf(HTMLDocument.prototype, Document.prototype);
document = new HTMLDocument()


Object.defineProperty(document.__proto__, Symbol.toStringTag, {
    value: "HTMLDocument",
    enumerable: false,
    configurable: true,
    writable: false
});

Object.defineProperty(Document.prototype, Symbol.toStringTag, {
    value: "Document",
    enumerable: false,
    configurable: true,
    writable: false
});


function Location() {
}
Location.prototype = {
    "ancestorOrigins": {},
    "href": "https://www.douyin.com/?recommend=1",
    "origin": "https://www.douyin.com",
    "protocol": "https:",
    "host": "www.douyin.com",
    "hostname": "www.douyin.com",
    "port": "",
    "pathname": "/",
    "search": "?recommend=1",
    "hash": ""
}
location = new Location()

Object.defineProperty(Location.prototype, Symbol.toStringTag, {
    value: "Location",
    configurable: true,
    writable: false,
    enumerable: false
});



function Navigator() {
}

Navigator.prototype = {
    appCodeName: "Mozilla",
    appName: "Netscape",
    appVersion: "5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36",
    userAgent: "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36",
    languages: [
        "zh-CN"
    ],
    platform: "Win32",
    webdriver: false,
    storage: {
        estimate: function () {
            return "estimate() { [native code] }";
        }
    }
}
Navigator.prototype.connection = watch({
        downlink: 10,
        effectiveType: "4g",
        rtt: 100,
        saveData: false,
        onchange: function () { },
    }, "Navigator.connection ===>")
navigator = new Navigator();


function Screen() {
}

Screen.prototype = {
    availHeight: 1027,
    availLeft: 0,
    availTop: 0,
    availWidth: 1707,
    colorDepth: 24,
    height: 1067,
    isExtended: false,
    onchange: null,
    pixelDepth: 24,
    width: 1707,
}

Screen.prototype.orientation = watch({
    angle: 0,
    type: "landscape-primary"
}, "Screen.orientation ===>");
screen = new Screen();

Object.defineProperty(Screen.prototype, Symbol.toStringTag, {
    value: "Screen",
    configurable: true,
    writable: false,
    enumerable: false
});



History = function History() { }
history = new History();
Object.defineProperty(History.prototype, Symbol.toStringTag, {
    value: "History",
    configurable: true,
    writable: false,
    enumerable: false
});

// console.log("============================", Object.prototype.toString.call(history))
// console.log(history.__proto__ === History.prototype);
// console.log("============================", Object.getOwnPropertyDescriptor(history.__proto__, Symbol.toStringTag))
// console.log("============================", Object.getOwnPropertyDescriptor(History.prototype, Symbol.toStringTag))

// setTimeout = function () { }
// setInterval = function () { }


get_enviroment(proxy_array)



