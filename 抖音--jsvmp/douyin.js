
require('./env.js');
require('./code');


require_ = require;
process_ = process;
delete global;
delete Buffer;
delete process;
delete require;
delete module;
delete exports;
delete __filename;
delete __dirname;



window.bdms.init({
    "aid": 6383,
    "pageId": 6241,
    "paths": [
        "^/webcast/",
        "^/aweme/v1/",
        "^/aweme/v2/",
        "/v1/message/send",
        "^/live/",
        "^/captcha/",
        "^/ecom/"
    ],
    "boe": false,
    "ddrt": 8.5,
    "ic": 8.5
})


mouseObj = {
    isTrusted: true,
    altKey: false,
    bubbles: true,
    button: 0,
    buttons: 0,
    cancelBubble: false,
    cancelable: true,
    clientX: 496,
    clientY: 285,
    composed: true,
    ctrlKey: false,
    currentTarget: document,
    defaultPrevented: false,
    detail: 0,
    eventPhase: 3,
    fromElement: null,
    layerX: 44,
    layerY: -722,
    metaKey: false,
    movementX: 0,
    movementY: 0,
    offsetX: 44,
    offsetY: 67,
    pageX: 496,
    pageY: 285,
    relatedTarget: null,
    returnValue: true,
    screenX: 496,
    screenY: 458,
    shiftKey: false,
    sourceCapabilities: {
        firesTouchEvents: false
    },
    srcElement: document.documentElement,
    target: document.documentElement,
    timeStamp: 13658.599999999627,
    toElement: document.documentElement,
    type: "mouseover",
    view: window,
    which: 0,
    x: 496,
    y: 285
}
window.mouseover.apply(document, [mouseObj]);
// window.mouseout.apply(document, [mouseObj]);
// window.mousemove.apply(document, [mouseObj]);



// const msToken = 'QYFiy97ptszoPn2QVYiQG-sl1E9uzhgMyQSeUg7dO1Q2DLkoOb_NdjiJzJ8AVc6cMT31rXGmWjrWsbqafsV0MJoLvQ_t3mOAto7QY0RaX5qF2zNLMaAKzIefB_60eikM-y2NyQCcBKYh9q8OcTBE0OOG6x5VRzErUT1qNVw41hwk8h4dtXpkTIOU'

var xhr = new XMLHttpRequest();
xhr.bdmsInvokeList = [
    {
        "args": [
            "GET",
            `https://www.douyin.com/aweme/v1/web/comment/list/?device_platform=webapp&aid=6383&channel=channel_pc_web&aweme_id=7517243155194383656&cursor=10&count=10&item_type=0&insert_ids=&whale_cut_token=&cut_version=1&rcFT=&update_version_code=170400&pc_client_type=1&pc_libra_divert=Windows&support_h265=1&support_dash=1&cpu_core_num=8&version_code=170400&version_name=17.4.0&cookie_enabled=true&screen_width=1707&screen_height=1067&browser_language=zh-CN&browser_platform=Win32&browser_name=Chrome&browser_version=135.0.0.0&browser_online=true&engine_name=Blink&engine_version=135.0.0.0&os_name=Windows&os_version=10&device_memory=8&platform=PC&downlink=10&effective_type=4g&round_trip_time=50&webid=7535424956948891155&uifid=4be83ecefa579a300714166db9e569bafd8689fc248d1e190e384db8df203b815b8199a58a174972f5fde36fbd95c3a5b639dcae58c63256cf73f7019d5a14f2802680df52249405c4525cf462be4640d2235fab4dd9ff84f7e1c6f23e201b1d80e0814fc4a97dccf7d1b21dba3d8d2f914ebf7f4fbfd4d90236f66c3745acacf69594a3eb44cae9cf297643e5e1e88a0271e6153243698ffa30a139451ed845&verifyFp=verify_mdzuthwe_i3lxmdaR_fcSd_4UsD_B5EB_0A2T3DbSVsBP&fp=verify_mdzuthwe_i3lxmdaR_fcSd_4UsD_B5EB_0A2T3DbSVsBP&msToken=QYFiy97ptszoPn2QVYiQG-sl1E9uzhgMyQSeUg7dO1Q2DLkoOb_NdjiJzJ8AVc6cMT31rXGmWjrWsbqafsV0MJoLvQ_t3mOAto7QY0RaX5qF2zNLMaAKzIefB_60eikM-y2NyQCcBKYh9q8OcTBE0OOG6x5VRzErUT1qNVw41hwk8h4dtXpkTIOU`,
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
            "4be83ecefa579a300714166db9e569bafd8689fc248d1e190e384db8df203b815b8199a58a174972f5fde36fbd95c3a5c31228f5a47264406fb9d153b277b0053ccc3bb2d253f3cb687646e758aa937f4e0ceefa8927a642169f07d3a87f7c920ae128f353d8af51e985c5c4b38674402ff2552e9185b093e6ac3bb050887f840c15088331877de04755c99b6094606fc48cc596f4aca5071485aeec8b459ea2"
        ],
        func: function () { }
    },
    {
        "args": [
            "bd-ticket-guard-ree-public-key",
            "BB0szRuah4iobJC8kGHuFaeoC4btTwWpRZbs7lgLxPLiN0HZYLb0SxwbP4Wm5hKlEkRuPytzqohp5XMs/Gm+vaY="
        ],
        func: function () { }
    },
    {
        "args": [
            "bd-ticket-guard-web-version",
            2
        ],
        func: function () { }
    },
    {
        "args": [
            "bd-ticket-guard-web-sign-type",
            1
        ],
        func: function () { }
    },
    {
        "args": [
            "bd-ticket-guard-version",
            2
        ],
        func: function () { }
    },
    {
        "args": [
            "bd-ticket-guard-iteration-version",
            1
        ],
        func: function () { }
    },
    {
        "args": [
            "bd-ticket-guard-client-data",
            "eyJ0c19zaWduIjoidHMuMi40NjQ5OGVjY2M2MjU4MzMxOWQ4NTczYWVmOWI3NDYxMTYyMDUzNzQ5NDcyMDAyNWZkODliOGJiYzVjYmM4NzBiYzRmYmU4N2QyMzE5Y2YwNTMxODYyNGNlZGExNDkxMWNhNDA2ZGVkYmViZWRkYjJlMzBmY2U4ZDRmYTAyNTc1ZCIsInJlcV9jb250ZW50IjoidGlja2V0LHBhdGgsdGltZXN0YW1wIiwicmVxX3NpZ24iOiJpL2xFZ3FjNEhOcFhoZ3BHS0NuNGhCb1JMNzJ5MnRkbjBEckRZVTE1dTAwPSIsInRpbWVzdGFtcCI6MTc1NDU0ODIyNX0="
        ],
        func: function () { }
    }
]

// xhr.send(null)
window.encryption.apply(xhr, null);
console.log(window.a_bogus, `=============> ${window.a_bogus.length}`)