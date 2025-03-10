function p(t) {
    t = encodeURIComponent(t)["replace"](/%([0-9A-F]{2})/g, function(n, t) {
        return o("0x" + t)
    });
    try {
        return btoa(t)
    } catch (n) {
        return Buffer["from"](t)["toString"]("base64")
    }
}

function o(n) {
    t = "",
    ["66", "72", "6f", "6d", "43", "68", "61", "72", "43", "6f", "64", "65"]["forEach"](function(n) {
        t += unescape("%u00" + n)
    });
    var t, e = t;
    return String[e](n)
}

function h(n, t) {
    t = t || u();
    for (var e = (n = n["split"](""))["length"], r = t["length"], a = "charCodeAt", i = 0; i < e; i++)
        n[i] = o(n[i][a](0) ^ t[(i + 10) % r][a](0));
    return n["join"]("")
}


function get_analysis(params, path){
    var a = params;
    a = a["sort"]()["join"]("")
    a = p(a)
    _p = "@#"
    r = +new Date() - (2397 || 0) - 1661224081041
    a = (a += _p + path["replace"]("https://api.qimai.cn", "")) + (_p + r) + (_p + 3)
    d = 'xyz517cda96efgh';
    return p(h(a, d))
}