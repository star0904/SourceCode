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

proxy_array = ['window', 'document', 'location', 'navigator', 'history', 'screen', "xhr"]



window = globalThis;
window.requestAnimationFrame = function () { }
window.XMLHttpRequest = require("xhr2").XMLHttpRequest;


location = {
    "href": "https://www.douyin.com/"
}

navigator = {
    appCodeName: "Mozilla",
    appName: "Netscape",
    appVersion: "5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36",
    userAgent: "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36",
    languages: [
        "zh-CN"
    ],
    platform: "Win32",
    webdriver: false,
}

screen = {
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

get_enviroment(proxy_array)
require("./2.js");

var xhr = new XMLHttpRequest();

xhr.bdmsInvokeList = [
    {
        "args": [
            "GET",
            "https://www.douyin.com/aweme/v1/web/comment/list/?device_platform=webapp&aid=6383&channel=channel_pc_web&aweme_id=7535398939915341075&cursor=10&count=10&item_type=0&insert_ids=&whale_cut_token=&cut_version=1&rcFT=&update_version_code=170400&pc_client_type=1&pc_libra_divert=Windows&support_h265=1&support_dash=1&cpu_core_num=8&version_code=170400&version_name=17.4.0&cookie_enabled=true&screen_width=1707&screen_height=1067&browser_language=zh-CN&browser_platform=Win32&browser_name=Chrome&browser_version=135.0.0.0&browser_online=true&engine_name=Blink&engine_version=135.0.0.0&os_name=Windows&os_version=10&device_memory=8&platform=PC&downlink=10&effective_type=4g&round_trip_time=50&webid=7535733156143760935&uifid=4be83ecefa579a300714166db9e569bafd8689fc248d1e190e384db8df203b815b8199a58a174972f5fde36fbd95c3a539bd68f757a697115e7279bf753ee78adf079e3778cac30bcb1585a4c1f5434643e93a7da334100f70c7bb489804a735406aa29d59891c0633da3e28df9e96a43e516a77acadbc74f8a8a55226337b93a446c5ceee3f7d2c32ee9893d52956568d2c1453256c23cbdfe7bc008bc9d86c&msToken=fJLcsohyCsxTLIPS5-Ti0rc4HflOGcwbcZYFVyHqNLOxaQqlQzk6QQo3dayBN32ZmVSYqOeHEd5lZH--osK3wre-MhM_cCXqM4o2QCJSDDgZ6ATn_uBerlLrz9zWTXeojmjPFwmvVxxdkX1KSCxrpdZqHqH-3vil5g_9lAGp4CMzgK184RARfg%3D%3D",
            true
        ],
        func: function () { }
    },
    {
        "args": [
            "Accept",
            "application/json, text/plain, */*"
        ],
        func: function () { }
    },
    {
        "args": [
            "uifid",
            "4be83ecefa579a300714166db9e569bafd8689fc248d1e190e384db8df203b815b8199a58a174972f5fde36fbd95c3a539bd68f757a697115e7279bf753ee78adf079e3778cac30bcb1585a4c1f5434643e93a7da334100f70c7bb489804a735406aa29d59891c0633da3e28df9e96a43e516a77acadbc74f8a8a55226337b93a446c5ceee3f7d2c32ee9893d52956568d2c1453256c23cbdfe7bc008bc9d86c"
        ],
        func: function () { }
    }
]
get_enviroment([
    "xhr"
])
window.encryption.apply(xhr, [null])


