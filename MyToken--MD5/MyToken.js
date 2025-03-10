const CryptoJs = require('crypto-js')


function MyToken(){
    t = Date.now().toString()
    let code = CryptoJs.MD5(t + "9527" + t.substr(0, 6)).toString()
    return {
        'code': code,
        'timestamp': t
    }
}
