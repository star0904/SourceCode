const CrytoJs = require('crypto-js');

function hmacSha512(val, key){
    return CrytoJs.HmacSHA512(val, key).toString()
}

a = {
    "default": {
        "n": 20,
        "codes": {
            "0": "W",
            "1": "l",
            "2": "k",
            "3": "B",
            "4": "Q",
            "5": "g",
            "6": "f",
            "7": "i",
            "8": "i",
            "9": "r",
            "10": "v",
            "11": "6",
            "12": "A",
            "13": "K",
            "14": "N",
            "15": "k",
            "16": "4",
            "17": "L",
            "18": "1",
            "19": "8"
        }
    }
}

function O() {
    for (var e = (arguments.length > 0 && void 0 !== arguments[0] ? arguments[0] : "/").toLowerCase(), t = e + e, n = "", i = 0; i < t.length; ++i) {
        var o = t[i].charCodeAt() % a.default.n;
        n += a.default.codes[o]
    }
    return n
}

function o() {
    var e = arguments.length > 1 && void 0 !== arguments[1] ? arguments[1] : {}
      , t = (arguments.length > 0 && void 0 !== arguments[0] ? arguments[0] : "/").toLowerCase()
      , n = JSON.stringify(e).toLowerCase();
    return hmacSha512(t + n, O(t)).toLowerCase().substr(8, 20)
}


function r() {
    var e = arguments.length > 1 && void 0 !== arguments[1] ? arguments[1] : {}
      , t = arguments.length > 2 && void 0 !== arguments[2] ? arguments[2] : ""
      , n = (arguments.length > 0 && void 0 !== arguments[0] ? arguments[0] : "/").toLowerCase()
      , i = JSON.stringify(e).toLowerCase();
    return hmacSha512(n + "pathString" + i + t, O(n))
}


function qcc(url, data){
    return {
        key: o(url, data),
        value: r(url, data, "9c2663dea27b078adbacc43f1cd024e0")
    }
}