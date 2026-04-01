Function.prototype.toString_ = Function.prototype.toString;
Function.prototype.toString_ = function () {
    debugger
};


(() => {
    const origin_log = console.log;;
    console_log = function () {
        return origin_log(...arguments)
    }
})();;;    // 防止检测console.log


!(function () {
    watch = function (obj, name) {
        return new Proxy(obj, {
            get(target, p, receiver) {
                // 过滤没用的信息，不进行打印
                if (name)
                    if (p === "Math" || p === "Number" || p === "parseFloat" || p === "Object" || p === "String" || p === "Symbol" || p === "Proxy" || p === "Promise" || p === "Array" || p === "isNaN" || p === "encodeURI" || p === "Uint8Array" || p.toString().indexOf("Symbol(") != -1) {
                        var val = Reflect.get(...arguments);
                        return val
                    }

                    else {
                        var val = Reflect.get(...arguments);

                        if (typeof val === 'function') {
                            console_log(`取值:`, name, '.', p, ` =>`, 'function');
                        }
                        else {
                            console_log(`取值:`, name, '.', p, ` =>`, val);
                        }

                        return val
                    }
            },
            set(target, p, value, receiver) {
                var val = Reflect.set(...arguments)
                if (typeof value === 'function') {
                    console_log(`设置值:${name}.${p}=>function `,);
                }
                else {
                    console_log(`设置值:${name}.${p}=> `, value);
                }
                return val
            },
            has(target, key) {
                console_log(`检查属性存在性: ${name}.${key.toString()}`);
                return key in target;
            },
            ownKeys(target) {
                console_log(`ownKeys检测: ${name}`);
                return Reflect.ownKeys(...arguments)
            }
        })
    }
})();    // 环境代理

function makeFunction(name) {
    // 动态创建一个函数
    var func = new Function(`
        return function ${name}() {
            console_log('函数传参.${name}',arguments)
        }
    `)();
    safeFunction(func)
    func.prototype = watch(func.prototype, `方法原型:${name}.prototype`)
    func = watch(func, `方法本身:${name}`)
    return func;
};    // makeFunction保护函数

(() => {
    Function.prototype.$call = Function.prototype.call
    const $toString = Function.toString;
    const myFunction_toString_symbol = Symbol('('.concat('', ')_'));
    const myToString = function toString() {
        return typeof this == 'function' && this[myFunction_toString_symbol] || $toString.$call(this);
    };

    function set_native(func, key, value) {
        Object.defineProperty(func, key, {
            "enumerable": false,
            "configurable": true,
            "writable": true,
            "value": value
        })
    }

    delete Function.prototype['toString'];

    set_native(Function.prototype, "toString", myToString);

    set_native(Function.prototype.toString, myFunction_toString_symbol, "function toString() { [native code] }");

    safeFunction = (func) => {
        set_native(func, myFunction_toString_symbol, `function ${func.name}() { [native code] }`);
    };
})();;;    // 函数名保护


Object.getOwnPropertyDescriptor_ = Object.getOwnPropertyDescriptor;
Object.getOwnPropertyDescriptor = function getOwnPropertyDescriptor(target, prop) {
    var val = Object.getOwnPropertyDescriptor_(target, prop);
    val = watch(val, `${prop}描述符`);
    return val;
}; safeFunction(Object.getOwnPropertyDescriptor);     // 对属性描述符检测的hook


Object.getPrototypeOf_ = Object.getPrototypeOf;
Object.getPrototypeOf = function getPrototypeOf(target) {
    var val = Object.getPrototypeOf_(target);
    val = watch(val, 'getPrototypeOf原型');
    return val;
}; safeFunction(Object.getPrototypeOf);    // 对原型检测的hook



window = globalThis;
window.top = window;
window.self = window
window.addEventListener = makeFunction("addEventListener");

window.name = "";
window.DOMParser = makeFunction("DOMParser");
window.XMLHttpRequest = makeFunction('XMLHttpRequest');
window.XMLHttpRequest.prototype.open = makeFunction('open');
window.XMLHttpRequest.prototype.send = makeFunction('send');
window.indexedDB = watch({
    open: makeFunction('open')
}, "indexedDB");
window.fetch = makeFunction('fetch');
window.Request = makeFunction('Request');
window.chrome = watch({
}, 'chrome');
window.MutationObserver = makeFunction('MutationObserver');
MutationObserver.prototype.observe = makeFunction('observe');
window.CanvasRenderingContext2D = makeFunction('CanvasRenderingContext2D');
CanvasRenderingContext2D.prototype.getImageData = makeFunction('getImageData');
window.HTMLCanvasElement = makeFunction('HTMLCanvasElement');
HTMLCanvasElement.prototype.toBlob = makeFunction('toBlob');
HTMLCanvasElement.prototype.toDataURL = makeFunction('toDataURL');
window.HTMLFormElement = makeFunction('HTMLFormElement');
window.setInterval = function () { }
window.setTimeout = function () { }


navigator = {
    userAgent: 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36',
    webkitPersistentStorage: watch({}, "webkitPersistentStorage"),
    getBattery: makeFunction("getBattery"),
    webdriver: false,
    connection: watch({
        downlink: 10,
        effectiveType: "4g",
        onchange: null,
        rtt: 50,
        saveData: false
    }, "connection"),
};
window.clientInformation = navigator;


document = {
    visibilityState: "visible",
    cookie: 'aisteUv=17567967404052155117954; aisiteJsSessionId=17567967404061377865045; pgv_info=; jDwkDWjIm6GRP=0OoJaTEz45rDZIYYCOmVxw9ahuvItdBHO9BA.Ho6vbUN7jDQNXkFkBvtSOADrTyMyhpY397ijCsfRto1bZYSXG8zgeoMFeInfUsa6Cs0KBWDsdqTBwZn87KKEuOvoq24diS9XPuQlQpoN04WMCeMaKgoH7fOmEr5qO2a76ukjjyvAH5veBhoCooZCBI5iJNdgCbkQ_xvF3YbMFL8Rv9NW1hw_zHgUQDPQ50Mtece6Tl29Es699KEzRv8Vi8_NK7xEHRA8QumoOMkQoeTEk9CZT8Gt846wRmpvh.xKHAfalXoUrScoGZKOwLhQ7J1lWdIlrbg9DuvfBD8BCVxPFMxm9Rhhqfp92xyZDCULakvSUnL3xaAxtgIiAxLP41RZ1sm4',
    addEventListener: makeFunction('addEventListener'),
    all: watch([], 'all'),
    createElement: function (argument) {
        console.log('document的createElement接受了:', arguments)
        if (argument === 'div') {
            return watch({
                getElementsByTagName: function (argument) {
                    console.log('getElementsByTagName接受参数:', arguments)
                    if (argument === 'i') {
                        return watch({}, "i")
                    }
                }
            }, 'div')
        }
    },
    appendChild: function (argument) {
        console.log('appendChild接受参数:', arguments)
    },
    removeChild: function (argument) {
        console.log('removeChild:', arguments)
    },
    getElementsByTagName: function (argument) {
        console.log('getElementsByTagName接受参数:', arguments)
        if (argument === "script") {
            return watch([
                {
                    type: "text/javascript",
                    src: "/uiFramework/js/counting/ea.js?random=15648",
                    getAttribute: function (argument) {
                        console.log('script的getAttribute接受了:', argument)
                        if (argument === 'r') {
                            return null
                        }
                    }
                },
            ], "script")
        }
        if (argument === "base") {
            return watch({ length: 0 }, "base")
        }
    },
    getElementById: function (argument) {
        console.log('document的getElementById接受了:', argument)
    },
    documentElement: function (argument) {
        console.log('document的documentElement接受了:', argument)
    },
    attachEvent: function (argument) {
        console.log('document的attachEvent接受了:', argument)
    },
};
location = {
    "ancestorOrigins": {},
    "href": "https://www.jscq.com.cn/",
    "origin": "https://www.jscq.com.cn",
    "protocol": "https:",
    "host": "www.jscq.com.cn",
    "hostname": "www.jscq.com.cn",
    "port": "",
    "pathname": "/",
    "search": "",
    "hash": ""
}
history = {
    replaceState: makeFunction("replaceState")
};
screen = {};
sessionStorage = {
    "$_YWTU": "dOcT3a8JLP5zy8nWcbaGWk.MhqfgnWWJNgT_L46A18q",
    "$_YVTX": "JO9",
    setItem: function (key, value) {
        this[key] = value;
    },
    getItem: function (key) {
        console_log('getItem', key)
        return this[key];
    },
}
localStorage = {
    "$_YWTU": "dOcT3a8JLP5zy8nWcbaGWk.MhqfgnWWJNgT_L46A18q",
    "_$rc": "2.bv5KAPJclSOM2hlwyFPvBB41lCIUgarPtdxZsmY84bcFZv0pp..ZLJVxBBGaZ3izUnCgSXMlA_UHXtnI9HuvRpQAl.yE0v594yFJIIoCt89sQutl5NHvf0Cmvvh82Zd_1oP8jEVe3_tBCdQb508KUV2lDvUPE1QWujvXxUqgKsvBhWZOrfN6hUktjiABy2TVRyTNbSU.TavLR2A8M0Trm1mtz8b71j5bGh629_Jib6z4P1bY0xV9sdQnvtVUYTi3VN2Qx0nY7Z4BZnWq4yt..BuGQIrTvaiRsVIUkKAUuooAcvcU6701XetzjzN_kFUezQr2DG7gnlRPXJTBYPlJFejag3GuARA5E6rdpqJsLyv8mihScKQP4r1__.vu5Sl3GOJzzxeSJAMFjm.sk87Xs7M7SR4i.xOmk_HAvy9Ccd6ZskzBkFMM_DLtku5.lqzvwpIqzwXsiH_JHO24Bfb4cXfJ_RBMdr_FYlhaH_7Dh.r0a2754AMaw7FvCndR.EoSDha6kexvqE_Ky2RAdMCvs7SjawhIGRWYy3s3Xy7weZTnxmnoXvL_NVh.Yhbjhy11Xy9asS1wCHXBqlRbz0KtkXnWdke4wrs1xcKvoUj5zkXlgQfDcWne3bGIHrmt_jvVtOR4lZiEoJRccVryaepoIwgFPuGojTvzE0fwRClA5ErfJ_12rJND7kTv.MpSymXOGTBh.0njQJqFm6yuebAk_7HKVfc6ZGos31lpmC.HAKhc3PWrfVeouYuRq",
    "__#classType": "localStorage",
    "$_YVTX": "JO9",
    setItem: function (key, value) {
        this[key] = value;
    },
    getItem: function (key) {
        console_log('getItem', key)
        return this[key];
    },
    removeItem: function (key) {
        delete this[key];
    }
}




window = watch(window, "window");
document = watch(document, "document");
navigator = watch(navigator, "navigator");
location = watch(location, "location");
screen = watch(screen, "screen");
history = watch(history, "history");
sessionStorage = watch(sessionStorage, "sessionStorage");
localStorage = watch(localStorage, "localStorage");


require("./1.js");

console_log(document.cookie)