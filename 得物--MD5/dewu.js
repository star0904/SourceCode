const CryptoJs = require('crypto-js');


function p(e) {
    return CryptoJs.MD5("".concat(e ? Object.keys(e).sort().reduce(function (t, n) {
        return "".concat(t).concat(n).concat(e[n])
    }, "") : "", "048a9c4943398714b356a696503d2d36")).toString()
}

function get_sign() {
    t = {
        "pageNum": 1,
        "pageSize": 20
    }
    return p(t)
}