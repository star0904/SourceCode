const CryptoJs = require('crypto-js')

function _0x5ec0(e, t) {
    var r = _0x3a2b();
    return (_0x5ec0 = function (e, t) {
            return e -= 251,
                r[e]
        }
    )(e, t)
}

function _0x3a2b() {
    var e = ["80hLgZPi", "10938120Oqmcds", "btoa", "userAgent", "804811nlntFe", "2585358GVcSNa", "2738538eYUjeG", "13373xdWcLL", "replace", "A013F70DB97834C0A5492378BD76C53A", "slice", "method", "error", "random", "=''", "548WwYBRt", "9254088oEFLMS", "118hfsyEC", "30445WALNJs", "floor", "keys"];
    return (_0x3a2b = function () {
            return e
        }
    )()
}

function getParams(uuid) {
    t = {
        movieId: undefined,
        orderType: 0,
        uuid: uuid,
        showDate: undefined
    }
    r = undefined
    n = void 0 === r ? {} : r

    d = {
        method: "GET",
        timeStamp: Date.now(),
        "User-Agent": btoa("" + "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"),
        index: Math.floor(1e3 * Math.random() + 1),
        channelId: 40009,
        sVersion: 2,
        key: 'A013F70DB97834C0A5492378BD76C53A'
    }


    c = Object.keys(d).reduce(function (e, t) {
        var r = _0x5ec0;
        return e = 0 === d[t] || d[t] ? e + "&" + t + "=" + d[t] : e + "&" + t + r(254)
    }, "").slice(1)


    f = CryptoJs.MD5(c.replace(/\s+/g, " ")).toString()

    return d.signKey = f,
        delete d.method,
        delete d.key,
        {
            finalQuery: Object.assign({}, t, d),
        }
}