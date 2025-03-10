const CryptoJS = require("crypto-js");

function AesDecrypt(text) {
    var n = CryptoJS.enc.Utf8.parse("QV1f3nHn2qm7i3xrj3Y9K9imDdGTjTu9")
      , r = CryptoJS.AES.decrypt(text, n, {
        mode: CryptoJS.mode.ECB,
        padding: CryptoJS.pad.Pkcs7
    })
      , i = r.toString(CryptoJS.enc.Utf8)
      , s = JSON.parse(i);
    return s.data.data;
}


function decryptData(text){
    return AesDecrypt(text);
}