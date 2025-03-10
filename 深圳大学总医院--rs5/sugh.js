delete __filename
delete __dirname
delete global


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


window  = globalThis;
window.top = window
window.self = window
window.addEventListener = function (arguments){
    console.log('window的addEventListener接受了参数：', arguments)
}
window.ActiveXObject = function (){}


document = {
    createElement: function (arguments){
        console.log('document的createElement接受了参数：', arguments)
        if (arguments === 'div'){
           return {
               getElementsByTagName:  function (arguments){
                   console.log('div的getElementsByTagName接受了参数：', arguments)
                   if (arguments === 'i') {
                       return {}
                   }
               }
           }
       }
        if (arguments === 'form'){
            return {}
        }
        if (arguments === 'a'){
            return {}
        }
    },
    getElementsByTagName: function (arguments){
        console.log('document的getElementsByTagName接受了参数：', arguments)
        if (arguments === 'meta'){
            return [
                {},
                {},
                {},
                {},
                {},
                {},
                {},
                {
                    content: "'content'",
                    parentNode: {
                        removeChild: function (argument){
                            return `<meta>`
                        }
                    }
                },
            ]
        }
        if (arguments === 'base'){
            return []
        }
        if (arguments === 'script'){
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
                }
            ]
        }
    },
    getElementById: function (argument){
        console.log('document的getElementById接受了:', argument)
    },
    addEventListener: function (argument){
        console.log('document的addEventListener接受了:', argument)
    },
    documentElement:  {
        addEventListener: function (argument){
            console.log('document的documentElement的addEventListener接受了:', argument)
        }
    }
}


location = {
    hash: "",
    host: "sugh.szu.edu.cn",
    hostname: "sugh.szu.edu.cn",
    href: "https://sugh.szu.edu.cn/Html/News/Columns/6/Index.html",
    origin: "https://sugh.szu.edu.cn",
    pathname: "/Html/News/Columns/6/Index.html",
    port: "",
    protocol: "https:",
}


navigator = {
    connection: {
        downlink: 10,
        effectiveType: "4g",
        onchange: null,
        rtt: 200,
        saveData: false
    },
    languages: ["zh-CN", "en", "en-GB", "en-US"],
    platform: "Win32",
    webdriver: false,
    webkitPersistentStorage: {},
    userAgent: "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0",
}


setTimeout = function(){}
setInterval = function(){}



get_enviroment(proxy_array)



'tsCode'




!'functionCode'

function get_cookie(){
    return document.cookie
}
