const sm2 = require('sm-crypto').sm2



function m(e) {
    var t = {}
        , n = ["signData", "encData", "extra"];
    for (var i in e)
        e.hasOwnProperty(i) && !n.includes(i) && null != e[i] && (t[i] = e[i]);
    return t
}

function p(e) {
    var t = new Array
        , n = 0;
    for (var i in e)
        t[n] = i,
            n++;
    var r = [].concat(t).sort()
        , o = {};
    for (var a in r)
        o[r[a]] = e[r[a]];
    return o
}

function v(e) {
    var t = [];
    for (var n in e)
        if (e.hasOwnProperty(n) && (e[n] || "".concat(e[n])))
            if ("data" === n) {
                var i = Object.assign({}, e[n]);
                for (var r in i) {
                    if ("number" != typeof i[r] && "boolean" != typeof i[r] || (i[r] = "" + i[r]),
                    Array.isArray(i[r]) && !i[r].length && delete i[r],
                    Array.isArray(i[r]) && i[r].length > 0)
                        for (var o = 0; o < i[r].length; o++)
                            i[r][o] = p(i[r][o]);
                    null != i[r] && i[r] || delete i[r]
                }
                var a = p(i);
                t.push("".concat(n, "=").concat(JSON.stringify(a)))
            } else
                t.push("".concat(n, "=").concat(e[n]));
    return t.push("key=".concat(c)),
        t.join("&")
}


function A(e) {
    var t, n, i = new Array;
    t = e.length;
    for (var r = 0; r < t; r++)
        (n = e.charCodeAt(r)) >= 65536 && n <= 1114111 ? (i.push(n >> 18 & 7 | 240),
            i.push(n >> 12 & 63 | 128),
            i.push(n >> 6 & 63 | 128),
            i.push(63 & n | 128)) : n >= 2048 && n <= 65535 ? (i.push(n >> 12 & 15 | 224),
            i.push(n >> 6 & 63 | 128),
            i.push(63 & n | 128)) : n >= 128 && n <= 2047 ? (i.push(n >> 6 & 31 | 192),
            i.push(63 & n | 128)) : i.push(255 & n);
    return i
}


function b(t, n) {
    var i = 16 - parseInt(n.length % 16);
    n = n.concat(new Array(i).fill(i));
    var r = sm4.encrypt(n, t);
    return r
}

function y(e, t) {
    return A(b(A(e.substr(0, 16)), A(t)).toUpperCase().substr(0, 16))
}


l = {
    appCode: "T98HPCGN5ZVVQBS8LZQNOAEXVI9GYHKQ",
    version: "1.0.0",
    appSecret: "NMVFVILMKT13GEMD3BKPKCTBOQBPZR2P",
    publicKey: "BEKaw3Qtc31LG/hTPHFPlriKuAn/nzTWl8LiRxLw4iQiSUIyuglptFxNkdCiNXcXvkqTH79Rh/A2sEFU6hjeK3k=",
    privateKey: "AJxKNdmspMaPGj+onJNoQ0cgWk2E3CYFWKBJhpcJrAtC",
    publicKeyType: "base64",
    privateKeyType: "base64"
}
    , u = l.appCode
    , c = l.appSecret
    , h = l.publicKey
    , d = l.privateKey;
s = Math.ceil((new Date).getTime() / 1e3)
signData = function (data) {
    var n = m(data)
        , i = p(n);
    i.data = p(i.data);
    var r = v(i)
        , a = sm2.doSignature(r, "009c4a35d9aca4c68f1a3fa89c93684347205a4d84dc260558a049869709ac0b42", {
        hash: !0
    });
    return new Buffer.from(a, "hex").toString("base64")
}

encData = function (data) {
    for (var t = data.data && JSON.stringify(data.data), n = "", i = 0; i < t.length; i++) {
        var r = t.charAt(i)
            , o = t.charCodeAt(i);
        n += o > 127 ? "\\u" + o.toString(16).padStart(4, "0") : r
    }
    var a = A(n);
    data.appCode && data.appCode !== u && (u = data.appCode);
    var s = y(u, c)
        , l = b(s, a);
    return l.toUpperCase()
}

//
// data = {
//     "data": {
//         "keyWords": "",
//         "drugType": "",
//         "pageNo": 2,
//         "pageSize": 10,
//         "medListCodg": "X"
//     },
//     "appCode": "T98HPCGN5ZVVQBS8LZQNOAEXVI9GYHKQ",
//     "version": "1.0.0",
//     "encType": "SM4",
//     "signType": "SM2",
//     "timestamp": 1739624111,
//     "signData": "nX4xYA0HdLhjs9SZ1bQZyGj73BFGbuFjpiH2v3H98DruatNf2RFovho3XPesbXYpbIrvJkTXOXjiAUyKAIZOCQ=="
// }
// console.log(encData(data))