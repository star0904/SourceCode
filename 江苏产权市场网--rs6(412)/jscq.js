delete __filename
delete __dirname


function get_enviroment(proxy_array) {
    for(var i=0; i<proxy_array.length; i++){
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
proxy_array = ['window', 'document', 'location', 'navigator', 'history','screen']



window = globalThis;
window.top = window
window.self = window
window.addEventListener = function (argument){
    console.log('window的addEventListener接受了:', argument)
}
window.ActiveXObject = function (){}
window.XMLHttpRequest = function (){
    return 'XMLHttpRequest() { [native code] }'
}
window.DOMParser = function (){
    return 'DOMParser() { [native code] }'
}
window.localStorage = {
    "$_YVTX": "Ja",
    "_$rc": "l9TaBdK6hfkUHCHKAivBJY4ufq56itAP3YHyhAoawgEyRlJjO2GbNoiVxjFRMmqvJtStakEa2CAlcqt3E7mJ98hcVQx1vK6BY58WR2lPsPQbSubWnwbRFyQt8cGSFG0WuHHsrX23oT7aLKjwGvH87PZgbESCJbBHvXlW82dibbR_i0Kc_XVh5iL3wHXX_TY7x2_tD4AJXgitlHbM4pR6H..148dPfv7IehMaQgRKK4chSImeZVBgH929t2MBEGD.f8qDMUmIWbqwiDtER32SweU135ZQ2O3bm5rWfnxCifxIjBbRQ9Z6Ix.xTtYV2LWqXWHnfEO6PMpz6sjdt.1j68WCLB0tO077PGQhEG1AkmuY3xNT3NCFbXdjk4qyE3TGcHsC3N89uoYfjAuNgonyIaUawt017G8ZOsxOxWcJyynumk1udMVVIB5oScB0M.lJIJ10bdOMShRl_Fq_f5Un8ZJj97fkj8TdqWDwCghQ70lU97i9h9V34lSxfzS0sYQPm8bMfyy5vO8CMYIL0zKB4KGujCnjTo4CRJl9.dkNstHyiPmbJPC73YrDiDXxy4ql3W83KUDU8NPhqHrn4fUoHSWUTUAH1NNMNbe_7JiKQsesBTghlWdOHgTZEy6ws1RMEOiJjRkqyDVPkAsXWYvsosyaF.EcttCPIkfIdkMldec0bVDvKAhhNeo_GWiq.i.D3QC0ZLzHbTCy7RvnT7FnDpffCmdGW9L1UqEms1KpMWXeiXwKYBbmXQZeFwAERvvVaC9qkA",
    "__#classType": "localStorage",
    "$_YWTU": "x.xd76SLxEsKSCGlEPXfienOSpoxR0OSfiHcXlLpf03"
}
window.sessionStorage = {
    "$_YVTX": "Ja",
    "$_YWTU": "x.xd76SLxEsKSCGlEPXfienOSpoxR0OSfiHcXlLpf03"
}
window.name = '$_YWTU=x.xd76SLxEsKSCGlEPXfienOSpoxR0OSfiHcXlLpf03&$_YVTX=Ja&vdFm='
window.indexedDB = {}
window.PointerEvent = function (){
    return 'PointerEvent() { [native code] }'
}
window.webkitRequestFileSystem = function (){
    return 'webkitRequestFileSystem() { [native code] }'
}
window.CanvasRenderingContext2D = function (){
    return 'CanvasRenderingContext2D() { [native code] }'
}
window.HTMLCanvasElement = function (){
    return 'HTMLCanvasElement() { [native code] }'
}
window.innerHeight = 791
window.innerWidth = 198
window.outerHeight = 912
window.outerWidth = 1707




Document = function Document(){}
Document.prototype.visibilityState = 'visible'

Document.prototype.createElement = function (argument){
    console.log('document的createElement接受了:', argument)
    if (argument === 'div'){
        return {
            getElementsByTagName: function (argument){
                console.log('div的getElementsByTagName接受了:', argument)
                if (argument === 'i'){
                    return {}
                }
            }
        }
    }
    if (argument === 'a'){
        return `<a></a>`
    }
    if (argument === 'form'){
        return `<form></form>`
    }
}
Document.prototype.getElementsByTagName = function (argument){
    console.log('document的getElementsByTagName接受了:', argument)
    if (argument === 'script'){
        return [
            {
                type: "text/javascript",
                getAttribute: function (argument){
                    console.log('script的getAttribute接受了:', argument)
                    if (argument === 'r'){
                        return 'm'
                    }
                },
                parentElement: {
                    removeChild: function (argument){
                        console.log('script的parentElement的removeChild接受了:', argument)
                    }
                }
            },
            {
                type: "text/javascript",
                getAttribute: function (argument){
                    if (argument === 'r'){
                        return 'm'
                    }
                },
                parentElement: {
                    removeChild: function (argument){
                        console.log('script的parentElement的removeChild接受了:', argument)
                    }
                }
            }
        ]
    }
    if (argument === 'meta'){
        return [
            {
                "http-equiv": "Content-Type",
                content: "text/html; charset=utf-8",
            },
            {
                id: "8WaRMCSEfLnj",
                content: "'content'",
                getAttribute: function (argument){
                    console.log('meta的getAttribute接受了:', argument)
                    if (argument === 'r'){
                        return 'm'
                    }
                },
                parentNode: {
                    removeChild: function (argument){
                        console.log('meta的parentNode的removeChild接受了:', argument)
                    }
                }
            }
        ]
    }
    if (argument === 'base'){
        return []
    }
}
Document.prototype.documentElement = function (argument){
    console.log('document的documentElement接受了:', argument)
}
Document.prototype.addEventListener = function (argument){
    console.log('document的addEventListener接受了:', argument)
}
Document.prototype.getElementById = function (argument){
    console.log('document的getElementById接受了:', argument)
    if (argument === '8WaRMCSEfLnj'){
        return {
            getAttribute: function (argument){
                console.log('meta的getAttribute接受了:', argument)
                if (argument === 'r'){
                    return 'm'
                }
            },
            parentNode: {
                    removeChild: function (argument){
                        console.log('meta的parentNode的removeChild接受了:', argument)
                    }
                }
        }
    }
    if(argument === 'a'){
        return null
    }
    if(argument === 'div'){
        return null
    }
}
Document.prototype.removeChild = function (argument){
    console.log('document的removeChild接受了:', argument)
}
Document.prototype.appendChild = function (argument){
    console.log('document的appendChild接受了:', argument)
}
Document.prototype.documentElement =  {
    addEventListener: function (argument){
        console.log('document的documentElement的addEventListener接受了:', argument)
    }
}


HTMLDocument  = function HTMLDocument(){}
Object.setPrototypeOf(HTMLDocument.prototype, Document.prototype)
document = new HTMLDocument()



Location = function Location(){}
Location.prototype = {
    "ancestorOrigins": {},
    "href": "https://www.jscq.com.cn/jscq/cqjy/jygg/cqzr/index.shtml",
    "origin": "https://www.jscq.com.cn",
    "protocol": "https:",
    "host": "www.jscq.com.cn",
    "hostname": "www.jscq.com.cn",
    "port": "",
    "pathname": "/jscq/cqjy/jygg/cqzr/index.shtml",
    "search": "",
    "hash": ""
}
location = new Location()



Navigator = function Navigator(){}
Navigator.prototype = {
    appCodeName: "Mozilla",
    appName: "Netscape",
    appVersion: "5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0",
    userAgent: "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0",
    platform: 'win32',
    webkitPersistentStorage: {},
    connection: {
        downlink: 10,
        effectiveType: "4g",
        onchange: null,
        rtt: 50,
        saveData: false
    }
}
Navigator.prototype.getBattery = function (){
    return 'getBattery() { [native code] }'
}
navigator = new Navigator()


History = function History(){}
History.prototype = {
    length: 4,
    scrollRestoration: "auto",
    state: null
}
History.prototype.replaceState = function (argument){
    console.log('history的replaceState接受了:', argument)
}
history = new History()




setInterval = function (){}

get_enviroment(proxy_array)


require("./1.js");



'tsCode'



'functionCode'




function get_cookie(){
    return document.cookie
}

