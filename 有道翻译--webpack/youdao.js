const {JSDOM} = require('jsdom');

// 创建虚拟 DOM
const dom = new JSDOM(`<!DOCTYPE html><html><body></body></html>`);
const doc = dom.window.document;


function get_enviroment(proxy_array) {
    for (var i = 0; i < proxy_array.length; i++) {
        handler = '{\n' + '    get: function(target, property, receiver) {\n' + '        console.log("方法:", "get  ", "对象:", ' + '"' + proxy_array[i] + '" ,' + '"  属性:", property, ' + '"  属性类型:", ' + 'typeof property, ' + // '"  属性值:", ' + 'target[property], ' +
            '"  属性值类型:", typeof target[property]);\n' + '        return target[property];\n' + '    },\n' + '    set: function(target, property, value, receiver) {\n' + '        console.log("方法:", "set  ", "对象:", ' + '"' + proxy_array[i] + '" ,' + '"  属性:", property, ' + '"  属性类型:", ' + 'typeof property, ' + // '"  属性值:", ' + 'target[property], ' +
            '"  属性值类型:", typeof target[property]);\n' + '        return Reflect.set(...arguments);\n' + '    }\n' + '}'
        eval('try{\n' + proxy_array[i] + ';\n' + proxy_array[i] + '=new Proxy(' + proxy_array[i] + ', ' + handler + ')}catch (e) {\n' + proxy_array[i] + '={};\n' + proxy_array[i] + '=new Proxy(' + proxy_array[i] + ', ' + handler + ')}')
    }
}

proxy_array = ['window', 'document', 'location', 'navigator', 'history', 'screen']


window = global;
self = window;
document = {
    createElement: function (args) {
        console.log("createElement ===>", args)
        if (args == 'span') {
            return `<span></span>`
        }
        if (args == 'template') {
            return `<template></template>`
        }
        if (args == 'a') {
            return doc.createElement('a')
        }
        if (args == 'div') {
            return doc.createElement('div')
        }
    }, documentElement: function (args) {
        console.log("documentElement ===>", args)
    }, body: {
        appendChild: function (args) {
            console.log("appendChild ===>", args)
        }
    }
}
location = {
    "ancestorOrigins": {},
    "href": "https://fanyi.youdao.com/#/TextTranslate",
    "origin": "https://fanyi.youdao.com",
    "protocol": "https:",
    "host": "fanyi.youdao.com",
    "hostname": "fanyi.youdao.com",
    "port": "",
    "pathname": "/",
    "search": "",
    "hash": "#/TextTranslate",
}


get_enviroment(proxy_array)

require("./1.js");


const d = "fanyideskweb", u = "webfanyi", p = "client,mysticTime,product", m = "1.0.0", h = "web", g = "fanyi.web",
    b = 1, f = 1, v = 1, A = "wifi", y = 0;


function _(e) {
    return window.aaa(91565).createHash("md5").update(e.toString()).digest("hex")
}

function S(e, t) {
    return _(`client=${d}&mysticTime=${e}&product=${u}&key=${t}`)
}

function k(e, t) {
    const a = (new Date).getTime();
    return {
        sign: S(a, e),
        client: d,
        product: u,
        appVersion: m,
        vendor: h,
        pointParam: p,
        mysticTime: a,
        keyfrom: g,
        mid: b,
        screen: f,
        model: v,
        network: A,
        abtest: y,
        yduuid: t || "abcdefg"
    }
}


function get_params() {
    e = {
        "keyid": "webfanyi-key-getter-2025"
    }
    t = 'yU5nT5dK3eZ1pI4j'
    return window.aaa(41034).A(window.aaa(41034).A({}, e), k(t))
}

function get_data(e, t) {
    return window.aaa(41034).A(window.aaa(41034).A({}, e), k(t))
}

function T(e) {
    return window.aaa(91565).createHash("md5").update(e).digest()
}

function decodeData(e, t, a) {
    l = (window.aaa(97815), window.aaa(25507), window.aaa(48287)["Buffer"]);

    const o = l.alloc(16, T(t)), n = l.alloc(16, T(a)), r = window.aaa(91565).createDecipheriv("aes-128-cbc", o, n);
    let s = r.update(e, "base64", "utf-8");
    return s += r.final("utf-8"), s
}

// aaaaaa = "Z21kD9ZK1ke6ugku2ccWu4n6eLnvoDT0YgGi0y3g-v0B9sYqg8L9D6UERNozYOHq6nSlDcSkvA8p63gLAgTk7RjSySjlk9mM_oHthk8E08viUV417uSWIrlksIdCHgor_iBAzSnPXsJlCP78MbRl23U0ulsXLcs2J5kXCaiMVvxA7WnPNsF7J8USw_fI8zCvn0YMjQQtFhDzgoG0aILAMslQ7pMIQck_n2wBWo-A-QqOu4xK_lNK7qBSgdV0YosbU65CKE5T8bv0jr6GBUIbQ-jzoi_MDlSyVUDlfwmPRj1wTVE6Gj4SMTJwpz0rlhPQmRRPpxU48pPPwRkSlKYl9a9I9_-2CWZGR2iw5KH4joD2UhQv2acMpI-LqRn62B_eh-ijdAbDQOjofiwsOWe0KYeaY4_OQv5vHoDWOKdaU6z3E_wUZvYjWE6EZoD1AR5L5eMs38iGlsFB62bN_jBwUmwH0UzI3ekq4hq-ZnXAurkkPYIeCHIeFUPX6Em3wyMPhPIO2jAWzADvAl0bw0pIZO4SvZjGm1ts0tKYQpBhxzVV0e2ep_ZDjKMW_om11EfD"
// console.log(decodeData(aaaaaa, "ydsecret://query/key/B*RGygVywfNBwpmBaZg*WT7SIOUP2T0C9WHMZN39j^DAdaZhAnxvGcCY6VYFwnHl", "ydsecret://query/iv/C@lZe2YzHtZ2CYgaXKSVfsb7Y4QWHjITPPZ0nQp87fBeJ!Iv6v^6fvi2WN@bYpJ4"))



