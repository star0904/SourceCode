
//搜索 sign可以找到
//传统XHR找位置也可以
//256加密 64位


const CryptoJS = require('crypto-js')
function run(val){
    return CryptoJS.HmacSHA256(val, 'abfc8f9dcf8c3f3d8aa294ac5f2cf2cc7767e5592590f39c3f503271dd68562b').toString();
}

