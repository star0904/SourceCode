
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
window.requestAnimationFrame = function(argument){
    console.log('window的requestAnimationFrame接受了', argument)
}
window.XMLHttpRequest = function(argument) {
    console.log('window的XMLHttpRequest接受了', argument)
}
window._sdkGlueVersionMap = {
    "sdkGlueVersion": "1.0.0.64-fix.01",
    "bdmsVersion": "1.0.1.19-fix.01",
    "captchaVersion": "4.0.10"
}
window.EventSource = function (argument){
    console.log('window的EventSource接受了', argument)
}


Document = function Document(){}
Document.prototype.all = []
Document.prototype.createElement = function (argument){
    console.log('document的createElement接受了:', argument)
    if (argument === 'span'){
        return ['']
    }
}
Document.prototype.documentElement = function (argument){
    console.log('document的documentElement接受了:', argument)
}
Document.prototype.createEvent = function (argument){
    console.log('document的createEvent接受了:', argument)
}

HTMLDocument  = function HTMLDocument (){}
Object.setPrototypeOf(HTMLDocument .prototype, Document.prototype)
document = new HTMLDocument ()




Navigator = function Navigator(){}
Navigator.prototype = {
    pemrissions: {
        "microphone": "granted"
    },
    appCodeName: "Mozilla",
    appName: "Netscape",
    appVersion: "5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
    language: "zh-CN",
    languages: ["zh-CN", "zh"],
    platform: "Win32",
    product: "Gecko",
    productSub: "20030107",
    userAgent: "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
    vendor: "Google Inc.",
    vendorSub: ""
}
navigator = new Navigator()



Location = function Location(){}
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




get_enviroment(proxy_array)



require('./cdoe.js')



