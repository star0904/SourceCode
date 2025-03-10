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



Document = function Document(){}
Document.prototype.createElement = function (argument){
    console.log('document的createElement接受了:', argument)
    if (argument === 'div'){
        return {
            getElementsByTagName: function (argument){
                console.log('div的getElementsByTagName接受了:', argument)
                if (argument === 'i'){
                    return []
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
    if (argument === 'root-hammerhead-shadow-ui'){
        return null
    }
    if (argument === 'a'){
        return null
    }
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
    "href": "http://www.sgcc.com.cn/",
    "origin": "http://www.sgcc.com.cn",
    "protocol": "http:",
    "host": "www.sgcc.com.cn",
    "hostname": "www.sgcc.com.cn",
    "port": "",
    "pathname": "/",
    "search": "",
    "hash": ""
}
location = new Location()



Navigator = function Navigator(){}
Navigator.prototype = {
    "appCodeName": "Mozilla",
    "appName": "Netscape",
    "appVersion": "5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36",
    "platform": "Win32",
    "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0"
}
navigator = new Navigator()



get_enviroment(proxy_array)


setTimeout = function (){}
setInterval = function (){}



'tsCode'



'functionCode'




function get_cookie(){
    return document.cookie
}

