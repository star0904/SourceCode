const CryptoJs = require('crypto-js');


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
proxy_array = ['window', 'document', 'location', 'navigator', 'history', 'screen']



window = global;

location = {
    "ancestorOrigins": {},
    "href": "https://flight.qunar.com/site/oneway_list.htm?searchDepartureAirport=%E6%B7%B1%E5%9C%B3&searchArrivalAirport=%E9%87%8D%E5%BA%86&searchDepartureTime=2025-08-31&searchArrivalTime=2025-09-06&nextNDays=0&startSearch=true&fromCode=SZX&toCode=CKG&from=flight_dom_search&lowestPrice=null",
    "origin": "https://flight.qunar.com",
    "protocol": "https:",
    "host": "flight.qunar.com",
    "hostname": "flight.qunar.com",
    "port": "",
    "pathname": "/site/oneway_list.htm",
    "search": "?searchDepartureAirport=%E6%B7%B1%E5%9C%B3&searchArrivalAirport=%E9%87%8D%E5%BA%86&searchDepartureTime=2025-08-31&searchArrivalTime=2025-09-06&nextNDays=0&startSearch=true&fromCode=SZX&toCode=CKG&from=flight_dom_search&lowestPrice=null",
    "hash": ""
}



get_enviroment(proxy_array)



function encryptFunction() {
    return [function (e) {
        var t = CryptoJs.SHA1(e).toString();
        return CryptoJs.MD5(t).toString()
    }
        , function (e) {
            var t = CryptoJs.MD5(e).toString();
            return CryptoJs.SHA1(t).toString()
        }
    ]
}


function encrypt() {
    var t = "dbd2ea68-0ef5-456e-bcfa-e57c71c2a562" // QN48
        , n = Date.now()
        , r = n % 2;
    return encryptFunction()[r](t + n)
}




(function (_0x3751ae, _0x4fc16a) {
    var _0x32e533 = _0x40dc
        , _0x574b2d = _0x3751ae();
    while (!![]) {
        try {
            var _0xb9d3d1 = parseInt(_0x32e533(0x13b)) / 0x1 * (-parseInt(_0x32e533(0x165)) / 0x2) + parseInt(_0x32e533(0x168)) / 0x3 * (parseInt(_0x32e533(0x135)) / 0x4) + -parseInt(_0x32e533(0x161)) / 0x5 + parseInt(_0x32e533(0x15f)) / 0x6 * (parseInt(_0x32e533(0x12f)) / 0x7) + parseInt(_0x32e533(0x13e)) / 0x8 * (parseInt(_0x32e533(0x14f)) / 0x9) + -parseInt(_0x32e533(0x153)) / 0xa * (parseInt(_0x32e533(0x150)) / 0xb) + parseInt(_0x32e533(0x163)) / 0xc;
            if (_0xb9d3d1 === _0x4fc16a)
                break;
            else
                _0x574b2d['push'](_0x574b2d['shift']());
        } catch (_0x5877ee) {
            _0x574b2d['push'](_0x574b2d['shift']());
        }
    }
}(_0x4778, 0x22b5d));
function _0x4778() {
    var _0x4c99dc = ['ndGWmdvXy0PRwfu', 'DhLWzq', 'mJqYoda4zgPlzMzq', 'C2XPy2u', 'ntCXmZHJqvfqwhy', 'yLbHCMfT', 'BNvSBa', 'mZz2ANHnB1e', 'ndC1m1zTDhviDq', 'CMfUzg9TtNvT', 'Dg9mB3DLCKnHC2u', 'y1jewvq', 'A2v5qxjYyxK', 'DgfbC3q', 'mZi4ndHXEKPiwxC', 'sLnptG', 'zMXHDfrVtwfW', 'y2fSBa', 'DgLTzw91Da', 'CgLJy29SB1q', 'n1fLDgzpCW', 'C2LNBG', 'BM93', 'nJm2mhnkAuvfAq', 'txDQrLe', 'D3L3r0W', 'ywPHEa', 'C3rYAw5N', 'BgvUz3rO', 'ue9tva', 'DxjS', 'Aw5JBhvKzxm', 'Bg9NAw5FCMvNAxn0zxjFCgm', 'uxflBhu', 'vgD2DgO', 'B2jQzwn0', 'ChjVDg90ExbL', '6k+35lYG5ywL5y+c5PwW5BM25lIu5PIV5A+56lgH5zoM', 't0vqswe', 'Bg9NAw5FDg91y2G', 'ndu5EwjPExPH', 'ndC0oty5EKLWwu1n', 'ANvUzv92', 'thLTswC', 'mtburhzfqKe', 'Dg9tDhjPBMC', 'Ahr0Chm6lY9WAwnJB2XVzMuUCxvUyxiUy29Tl2zLl2rLzI9HCgKVChjLtg9Hzc9IzwXSyq', 'AxnwmG', 'BuHkrfy', 'ChvZAa', 'y0HOCLy', 'C3rYAw5NAwz5', 'zgf0yq', 'C2LNBMf0DxjL', 'zfjxqMC', 'Bg9NAw5FCMvNAxn0zxjFDg91y2G', 'mJa4mKzYD3j4tG', 'zgf0yvr5Cgu'];
    _0x4778 = function () {
        return _0x4c99dc;
    }
        ;
    return _0x4778();
}
function _0x40dc(_0xc17c18, _0x245eae) {
    var _0x4778d0 = _0x4778();
    return _0x40dc = function (_0x40dc48, _0x49b7bc) {
        _0x40dc48 = _0x40dc48 - 0x12f;
        var _0x481a74 = _0x4778d0[_0x40dc48];
        if (_0x40dc['MjVqfC'] === undefined) {
            var _0x28814c = function (_0x503150) {
                var _0x4f10d7 = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789+/=';
                var _0x2726ec = ''
                    , _0x91a51d = '';
                for (var _0x290a49 = 0x0, _0x4ec81e, _0x4cef7b, _0xe7ee33 = 0x0; _0x4cef7b = _0x503150['charAt'](_0xe7ee33++); ~_0x4cef7b && (_0x4ec81e = _0x290a49 % 0x4 ? _0x4ec81e * 0x40 + _0x4cef7b : _0x4cef7b,
                    _0x290a49++ % 0x4) ? _0x2726ec += String['fromCharCode'](0xff & _0x4ec81e >> (-0x2 * _0x290a49 & 0x6)) : 0x0) {
                    _0x4cef7b = _0x4f10d7['indexOf'](_0x4cef7b);
                }
                for (var _0x39063c = 0x0, _0x54f56c = _0x2726ec['length']; _0x39063c < _0x54f56c; _0x39063c++) {
                    _0x91a51d += '%' + ('00' + _0x2726ec['charCodeAt'](_0x39063c)['toString'](0x10))['slice'](-0x2);
                }
                return decodeURIComponent(_0x91a51d);
            };
            _0x40dc['CFneUc'] = _0x28814c,
                _0xc17c18 = arguments,
                _0x40dc['MjVqfC'] = !![];
        }
        var _0x21b99e = _0x4778d0[0x0]
            , _0xdf637a = _0x40dc48 + _0x21b99e
            , _0x497011 = _0xc17c18[_0xdf637a];
        return !_0x497011 ? (_0x481a74 = _0x40dc['CFneUc'](_0x481a74),
            _0xc17c18[_0xdf637a] = _0x481a74) : _0x481a74 = _0x497011,
            _0x481a74;
    }
        ,
        _0x40dc(_0xc17c18, _0x245eae);
}
function _0x12ca1f(_0x2b46d7) {
    var _0x2d6ef8 = _0x40dc
    var _0x4bcdb8 = _0x2d6ef8
        , _0x2d0544 = []
        , _0x1d8f00 = ''
        , _0xc890ae = Object['keys'](_0x2b46d7)
        , _0x295e29 = _0xc890ae[_0x4bcdb8(0x143)];
    if ([_0x4bcdb8(0x14e), _0x4bcdb8(0x15e), _0x4bcdb8(0x147)]['includes'](window[_0x4bcdb8(0x13a)])) {
        if (_0x4bcdb8(0x15d) === _0x4bcdb8(0x15d))
            for (var _0x3f9e57 = 0x0; _0x3f9e57 < _0x295e29; _0x3f9e57++) {
                if ('coDNX' !== _0x4bcdb8(0x149)) {
                    var _0x3b30ad = _0x2b46d7[_0xc890ae[_0x3f9e57]]
                        , _0x29fb1e = _0x3de0d7(_0x3b30ad);
                    _0x29fb1e !== '' && ([_0x4bcdb8(0x14e), _0x4bcdb8(0x15e)]['includes'](window['piccoloT']) && (_0x29fb1e = decodeURIComponent(_0x29fb1e)),
                        _0x1d8f00 += _0x29fb1e,
                        _0x2d0544[_0x4bcdb8(0x158)](_0xc890ae[_0x3f9e57]));
                } else
                    _0x1962d4 = _0x20fd55(_0x2d3a88);
            }
        else {
            if (!_0x29b5ea || _0x5f4472(_0x4f175c) !== _0x4bcdb8(0x14a))
                return _0x4bcdb8(0x14c);
            var _0x55c47c = _0x4bd712(_0x57bf20)
                , _0x3570c9 = _0x4fcd4b()
                , _0x29cfbd = _0x11087e[_0x4bcdb8(0x137)](_0x3570c9, {})
                , _0x5172de = _0x15bd09(_0x4c44c9['stringify'](_0x29cfbd), _0x19137b)
                , _0x3ac873 = _0x58766a()
                , _0x533fde = _0x55c47c['bParam'] + _0x5172de + _0x3ac873 + _0xaeeacc[_0x4bcdb8(0x15a)](_0x55c47c[_0x4bcdb8(0x133)])
                , _0xfcea8b = _0x2ffd13[_0x4bcdb8(0x15c)](_0x533fde)
                , _0x5bf390 = _0x3f5465[_0x4bcdb8(0x151)] + '##' + _0xfcea8b + '##' + _0x5172de + '##' + _0x3ac873 + '##' + _0x55c47c[_0x4bcdb8(0x133)];
            return _0x5bf390;
        }
    } else {
        if (_0x4bcdb8(0x134) === _0x4bcdb8(0x148))
            return _0x4b5846[_0x4bcdb8(0x14b)][_0x4bcdb8(0x154)][_0x4bcdb8(0x138)](_0x1055b8)[_0x4bcdb8(0x164)](0x8, -0x1)['toLowerCase']();
        else
            _0x1d8f00 = JSON[_0x4bcdb8(0x15a)](_0x2b46d7),
                _0x2d0544 = _0xc890ae;
    }
    var _0x56de19 = {};
    return _0x56de19[_0x4bcdb8(0x166)] = _0x1d8f00,
        _0x56de19[_0x4bcdb8(0x133)] = _0x2d0544,
        _0x56de19;
}



function _0x3190() {
    var _0x181871 = ['nhbQAuHfsW', 'mta5odC5v1nND3Dd', 'mJmXmZbxv2XQzg8', 'ndi4odLpwg5cwhO', 'mZmZuhjYzK5m', 'mJGWmty4qwHfsfvO', 'mti4mtK0mg9qAg90qq', 'mtG0tgfsshDf', 'CMfUzg9T', 'AM9PBG', 'mta0nZzjwLvqyLm', 'mdeYmZq1nJC4oufcq0rfrKDisuPlte1ot1bruLnuvvzxwfLAywjJzgvMz2HPAMTSBw5VChfYC3r1DND4ExO', 'mtmWofb3Evv6zG', 'otbACeT4uwK', 'nda3nZK1mNjMAg9KAq'];
    _0x3190 = function () {
        return _0x181871;
    }
        ;
    return _0x3190();
}
(function (_0xf21621, _0x28c112) {
    var _0x5d31c5 = _0x2444
        , _0xbf7319 = _0xf21621();
    while (!![]) {
        try {
            var _0x41cc05 = -parseInt(_0x5d31c5(0x99)) / 0x1 + parseInt(_0x5d31c5(0x9b)) / 0x2 * (-parseInt(_0x5d31c5(0x9e)) / 0x3) + parseInt(_0x5d31c5(0xa3)) / 0x4 * (-parseInt(_0x5d31c5(0x9a)) / 0x5) + parseInt(_0x5d31c5(0xa1)) / 0x6 * (parseInt(_0x5d31c5(0xa4)) / 0x7) + parseInt(_0x5d31c5(0xa2)) / 0x8 + parseInt(_0x5d31c5(0x98)) / 0x9 * (parseInt(_0x5d31c5(0x96)) / 0xa) + -parseInt(_0x5d31c5(0x97)) / 0xb * (-parseInt(_0x5d31c5(0xa0)) / 0xc);
            if (_0x41cc05 === _0x28c112)
                break;
            else
                _0xbf7319['push'](_0xbf7319['shift']());
        } catch (_0x369176) {
            _0xbf7319['push'](_0xbf7319['shift']());
        }
    }
}(_0x3190, 0x6127f))

function _0x2444(_0x52bcdf, _0x3c5ad2) {
    var _0x319098 = _0x3190();
    return _0x2444 = function (_0x244431, _0x367c7f) {
        _0x244431 = _0x244431 - 0x96;
        var _0x23de38 = _0x319098[_0x244431];
        if (_0x2444['kSXvlV'] === undefined) {
            var _0x26f68c = function (_0x715400) {
                var _0x5d3687 = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789+/=';
                var _0x33e693 = ''
                    , _0x48492b = '';
                for (var _0x5b2484 = 0x0, _0x4bf0e0, _0x380c9f, _0x4a83d0 = 0x0; _0x380c9f = _0x715400['charAt'](_0x4a83d0++); ~_0x380c9f && (_0x4bf0e0 = _0x5b2484 % 0x4 ? _0x4bf0e0 * 0x40 + _0x380c9f : _0x380c9f,
                    _0x5b2484++ % 0x4) ? _0x33e693 += String['fromCharCode'](0xff & _0x4bf0e0 >> (-0x2 * _0x5b2484 & 0x6)) : 0x0) {
                    _0x380c9f = _0x5d3687['indexOf'](_0x380c9f);
                }
                for (var _0x3aedf9 = 0x0, _0x35d5a3 = _0x33e693['length']; _0x3aedf9 < _0x35d5a3; _0x3aedf9++) {
                    _0x48492b += '%' + ('00' + _0x33e693['charCodeAt'](_0x3aedf9)['toString'](0x10))['slice'](-0x2);
                }
                return decodeURIComponent(_0x48492b);
            };
            _0x2444['ZohWFX'] = _0x26f68c,
                _0x52bcdf = arguments,
                _0x2444['kSXvlV'] = !![];
        }
        var _0x53d072 = _0x319098[0x0]
            , _0x57f9cb = _0x244431 + _0x53d072
            , _0x2931f4 = _0x52bcdf[_0x57f9cb];
        return !_0x2931f4 ? (_0x23de38 = _0x2444['ZohWFX'](_0x23de38),
            _0x52bcdf[_0x57f9cb] = _0x23de38) : _0x23de38 = _0x2931f4,
            _0x23de38;
    }
        ,
        _0x2444(_0x52bcdf, _0x3c5ad2);
}

function uuid(_0x50614e, _0x193365) {
    var _0x55072b = _0x2444, _0x291b6f = _0x55072b(0x9f)['split'](''), _0x3b6aca = [], _0x5c0cea;
    _0x193365 = _0x193365 || _0x291b6f['length'];
    if (_0x50614e) {
        for (_0x5c0cea = 0x0; _0x5c0cea < _0x50614e; _0x5c0cea++)
            _0x3b6aca[_0x5c0cea] = _0x291b6f[0x0 | Math['random']() * _0x193365];
    } else {
        var _0x5ded7e;
        _0x3b6aca[0x8] = _0x3b6aca[0xd] = _0x3b6aca[0x12] = _0x3b6aca[0x17] = '-',
            _0x3b6aca[0xe] = '4';
        for (_0x5c0cea = 0x0; _0x5c0cea < 0x24; _0x5c0cea++) {
            !_0x3b6aca[_0x5c0cea] && (_0x5ded7e = 0x0 | Math[_0x55072b(0x9c)]() * 0x10,
                _0x3b6aca[_0x5c0cea] = _0x291b6f[_0x5c0cea == 0x13 ? _0x5ded7e & 0x3 | 0x8 : _0x5ded7e]);
        }
    }
    return _0x3b6aca[_0x55072b(0x9d)]('');
}

function getPiccolo() {
    var _0x257a4a = uuid(16, 16)
        , _0x3ef6cc = Math.floor(Math.random() * (9999 - 1000) + 1000)
        , _0x139d93 = Date.now()
        , _0x5e4cbe = _0x3ef6cc + '##' + _0x257a4a + '##' + _0x139d93;
    return _0x5e4cbe;
}



function to2bin(_0x4f6971) {
    var _0x329c68 = _0xc021;
    return padStart(_0x4f6971[_0x329c68(0x190)]()[_0x329c68(0x188)](0x2), 0x8, '0');
}
function padStart(_0x3b4d43, _0x2997b2, _0x1c5fab) {
    var _0x48b2b5 = _0xc021;
    return _0x2997b2 = _0x2997b2 >> 0x0,
        _0x1c5fab = String(typeof _0x1c5fab !== _0x48b2b5(0x18e) ? _0x1c5fab : '\x20'),
        _0x3b4d43[_0x48b2b5(0x177)] > _0x2997b2 ? String(_0x3b4d43) : (_0x2997b2 = _0x2997b2 - _0x3b4d43['length'],
            _0x2997b2 > _0x1c5fab[_0x48b2b5(0x177)] && (_0x1c5fab += _0x1c5fab[_0x48b2b5(0x172)](_0x2997b2 / _0x1c5fab[_0x48b2b5(0x177)])),
            _0x1c5fab['slice'](0x0, _0x2997b2) + String(_0x3b4d43));
}

function _0x2e81() {
    var _0x4ee16f = ['BgvUz3rO', 'CdvnmdjtvuH0l2rVzW', 'm0njr0rsAfr2na', 'C3bSAwnL', 'zxjHv3e', 'mtK2nteYodbvze5My0W', 'ndq2mJaZmwHMvefPra', 'Bg9JyxrPB24', 'mtC5odbOyLrsCw8', 'otiZotflA2TmzLq', 'AM9PBG', 'rvG3vLDHCuPP', 'y1Dzv3C', 'Aw5JBhvKzxm', 'ChvZAa', 'CMvWBgfJzq', 'tMjLBMi', 'Dg9tDhjPBMC', 'DK9JEu0', 'y3LMAI05A1blDq', 'C3bSAxq', 'mtb4tKXyrvO', 'ueXvr20', 'Dw5KzwzPBMvK', 'nNbVEeLPrq', 'y2HHCKnVzgvbDa', 'qJzgmvLYtM0Rt0e9C3C', 'C2XPy2u', 'AhjLzG', 'mtm0ntjNv0vbwKK', 'nZGZAK1Kywj4', 'mti2nZm2mg9Ltu96AG', 'BJH4yMvmBhPr', 'CMvWzwf0', 'mZHgEencvfy', 'CxvUyxi', 'BwfW', 'ndq1mdG5nNL4yLzIyW'];
    _0x2e81 = function () {
        return _0x4ee16f;
    }
        ;
    return _0x2e81();
}
(function (_0x14fb97, _0x54b7ca) {
    var _0x51285e = _0xc021
        , _0xe5a8d = _0x14fb97();
    while (!![]) {
        try {
            var _0x8e35c3 = parseInt(_0x51285e(0x194)) / 0x1 + -parseInt(_0x51285e(0x173)) / 0x2 * (parseInt(_0x51285e(0x180)) / 0x3) + parseInt(_0x51285e(0x170)) / 0x4 * (-parseInt(_0x51285e(0x18c)) / 0x5) + -parseInt(_0x51285e(0x18f)) / 0x6 * (parseInt(_0x51285e(0x17d)) / 0x7) + parseInt(_0x51285e(0x176)) / 0x8 + parseInt(_0x51285e(0x16f)) / 0x9 * (-parseInt(_0x51285e(0x17f)) / 0xa) + parseInt(_0x51285e(0x17c)) / 0xb;
            if (_0x8e35c3 === _0x54b7ca)
                break;
            else
                _0xe5a8d['push'](_0xe5a8d['shift']());
        } catch (_0xf327ec) {
            _0xe5a8d['push'](_0xe5a8d['shift']());
        }
    }
}(_0x2e81, 0x53e3c));
function _0xc021(_0x420ae7, _0x482d8b) {
    var _0x2e812d = _0x2e81();
    return _0xc021 = function (_0xc021e8, _0x4d8289) {
        _0xc021e8 = _0xc021e8 - 0x16f;
        var _0x31f65f = _0x2e812d[_0xc021e8];
        if (_0xc021['dwhqZh'] === undefined) {
            var _0x12f2e4 = function (_0x5a2eed) {
                var _0x343c38 = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789+/=';
                var _0x29edd4 = ''
                    , _0x707e06 = '';
                for (var _0x4e41d3 = 0x0, _0x56afb5, _0x223273, _0x45fb95 = 0x0; _0x223273 = _0x5a2eed['charAt'](_0x45fb95++); ~_0x223273 && (_0x56afb5 = _0x4e41d3 % 0x4 ? _0x56afb5 * 0x40 + _0x223273 : _0x223273,
                    _0x4e41d3++ % 0x4) ? _0x29edd4 += String['fromCharCode'](0xff & _0x56afb5 >> (-0x2 * _0x4e41d3 & 0x6)) : 0x0) {
                    _0x223273 = _0x343c38['indexOf'](_0x223273);
                }
                for (var _0x3ac583 = 0x0, _0x5e5f37 = _0x29edd4['length']; _0x3ac583 < _0x5e5f37; _0x3ac583++) {
                    _0x707e06 += '%' + ('00' + _0x29edd4['charCodeAt'](_0x3ac583)['toString'](0x10))['slice'](-0x2);
                }
                return decodeURIComponent(_0x707e06);
            };
            _0xc021['fxiZfV'] = _0x12f2e4,
                _0x420ae7 = arguments,
                _0xc021['dwhqZh'] = !![];
        }
        var _0x483f20 = _0x2e812d[0x0]
            , _0x5a1333 = _0xc021e8 + _0x483f20
            , _0xe6a3bd = _0x420ae7[_0x5a1333];
        return !_0xe6a3bd ? (_0x31f65f = _0xc021['fxiZfV'](_0x31f65f),
            _0x420ae7[_0x5a1333] = _0x31f65f) : _0x31f65f = _0xe6a3bd,
            _0x31f65f;
    }
        ,
        _0xc021(_0x420ae7, _0x482d8b);
}

function enhanceBase64(_0x443872, _0x205991) {
    var _0x8358cb = _0xc021
        , _0x596e9f = [_0x8358cb(0x174), 'tujia']
        , _0x23c0ba = _0x8358cb(0x191)
        , _0x598c2f = _0x8358cb(0x171)
        , _0x5f3ad7 = _0x8358cb(0x178)
        , _0x1d0299 = _0x8358cb(0x18a)
        , _0x18cf85 = _0x8358cb(0x182)
        , _0x40ee2b = _0x8358cb(0x179)
        , _0x365647 = _0x205991[_0x8358cb(0x181)]('') + (_0x23c0ba + _0x598c2f + _0x5f3ad7 + _0x1d0299 + _0x18cf85 + _0x40ee2b);
    _0x365647 = (_0x23c0ba + _0x598c2f + _0x5f3ad7 + _0x1d0299 + _0x18cf85 + _0x40ee2b)[_0x8358cb(0x18b)](''),
        _0x443872 = encodeURIComponent(_0x443872);
    while (_0x443872[_0x8358cb(0x177)] % 0x3 !== 0x0) {
        _0x443872 += '\x20';
    }
    var _0x57c566 = _0x443872[_0x8358cb(0x18b)]('')[_0x8358cb(0x175)](function (_0x46831c) {
        var _0x323dc3 = _0x8358cb;
        return _0x323dc3(0x17b) !== _0x323dc3(0x189) ? to2bin(_0x46831c) : (_0x544685 = _0x3d3f65 - _0x20e007['length'],
            _0xf9806e > _0x1829f9[_0x323dc3(0x177)] && (_0x4a0e93 += _0x514775[_0x323dc3(0x172)](_0xbf9cd / _0x10f423['length'])),
            _0x5262bc[_0x323dc3(0x192)](0x0, _0x2fc45f) + _0x25fb6c(_0x3bcf77));
    })
        , _0x240e9c = [];
    while (_0x57c566[_0x8358cb(0x177)]) {
        var _0x3d60e6 = _0x57c566[_0x8358cb(0x17a)](0x0, 0x3);
        _0x240e9c['push'](_0x3d60e6);
    }
    var _0x2488cd = ''
        , _0x460c5b = !_0x596e9f['some'](function (_0x450294) {
            var _0x40ceb6 = _0x8358cb;
            return window[_0x40ceb6(0x17e)][_0x40ceb6(0x193)][_0x40ceb6(0x184)](_0x450294);
        });
    for (var _0x406ec8 = 0x0; _0x406ec8 < _0x240e9c[_0x8358cb(0x177)]; _0x406ec8++) {
        if ('cWYWw' !== _0x8358cb(0x183)) {
            _0x2ee7a9 = _0x3e8e50 ? _0x56c068 : _0x275653[_0x8358cb(0x186)](/\d/g, function (_0x18a73e) {
                return _0x18a73e === '1' ? 0x0 : 0x1;
            });
            var _0x19689d = _0xcf07d5(_0x4e3f8a(_0x1237a1, 0x8, '0'), 0x2);
            return _0x23b7f8[_0x19689d];
        } else {
            var _0x3d60e6 = _0x240e9c[_0x406ec8]
                , _0x55f27f = _0x3d60e6[_0x8358cb(0x181)]('')[_0x8358cb(0x18b)]('')
                , _0x5ec71f = [];
            while (_0x55f27f[_0x8358cb(0x177)]) {
                _0x8358cb(0x187) === _0x8358cb(0x18d) ? _0x343c38 += '\x20' : _0x5ec71f[_0x8358cb(0x185)](_0x55f27f['splice'](0x0, 0x6)['join'](''));
            }
            _0x5ec71f = _0x5ec71f['map'](function (_0xf33d8b) {
                _0xf33d8b = _0x460c5b ? _0xf33d8b : _0xf33d8b['replace'](/\d/g, function (_0x28f6e2) {
                    return _0x28f6e2 === '1' ? 0x0 : 0x1;
                });
                var _0x586bf0 = parseInt(padStart(_0xf33d8b, 0x8, '0'), 0x2);
                return _0x365647[_0x586bf0];
            }),
                _0x2488cd += _0x5ec71f[_0x8358cb(0x181)]('');
        }
    }
    return _0x2488cd;
}



function _0x38b4(_0x423233, _0x5eea3c) {
    var _0x18a1dc = _0x18a1();
    return _0x38b4 = function (_0x38b4fe, _0x51fe9e) {
        _0x38b4fe = _0x38b4fe - 0x15b;
        var _0x5c175f = _0x18a1dc[_0x38b4fe];
        if (_0x38b4['baOyYE'] === undefined) {
            var _0x2d5055 = function (_0x58030c) {
                var _0x5ddd40 = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789+/=';
                var _0x288edb = ''
                    , _0xa2d57d = '';
                for (var _0x473b66 = 0x0, _0x1f40e7, _0x4e41b2, _0x5bc9a0 = 0x0; _0x4e41b2 = _0x58030c['charAt'](_0x5bc9a0++); ~_0x4e41b2 && (_0x1f40e7 = _0x473b66 % 0x4 ? _0x1f40e7 * 0x40 + _0x4e41b2 : _0x4e41b2,
                    _0x473b66++ % 0x4) ? _0x288edb += String['fromCharCode'](0xff & _0x1f40e7 >> (-0x2 * _0x473b66 & 0x6)) : 0x0) {
                    _0x4e41b2 = _0x5ddd40['indexOf'](_0x4e41b2);
                }
                for (var _0x45b374 = 0x0, _0x4331d3 = _0x288edb['length']; _0x45b374 < _0x4331d3; _0x45b374++) {
                    _0xa2d57d += '%' + ('00' + _0x288edb['charCodeAt'](_0x45b374)['toString'](0x10))['slice'](-0x2);
                }
                return decodeURIComponent(_0xa2d57d);
            };
            _0x38b4['IomBlH'] = _0x2d5055,
                _0x423233 = arguments,
                _0x38b4['baOyYE'] = !![];
        }
        var _0x5a6d91 = _0x18a1dc[0x0]
            , _0x5e11b7 = _0x38b4fe + _0x5a6d91
            , _0x1a7b9a = _0x423233[_0x5e11b7];
        return !_0x1a7b9a ? (_0x5c175f = _0x38b4['IomBlH'](_0x5c175f),
            _0x423233[_0x5e11b7] = _0x5c175f) : _0x5c175f = _0x1a7b9a,
            _0x5c175f;
    }
        ,
        _0x38b4(_0x423233, _0x5eea3c);
}
(function (_0x5a98bb, _0x1bec85) {
    var _0x14f663 = _0x38b4
        , _0x2471ad = _0x5a98bb();
    while (!![]) {
        try {
            var _0x10202c = parseInt(_0x14f663(0x168)) / 0x1 + parseInt(_0x14f663(0x15f)) / 0x2 + -parseInt(_0x14f663(0x163)) / 0x3 + -parseInt(_0x14f663(0x166)) / 0x4 + -parseInt(_0x14f663(0x165)) / 0x5 + parseInt(_0x14f663(0x164)) / 0x6 * (-parseInt(_0x14f663(0x15c)) / 0x7) + -parseInt(_0x14f663(0x161)) / 0x8 * (-parseInt(_0x14f663(0x160)) / 0x9);
            if (_0x10202c === _0x1bec85)
                break;
            else
                _0x2471ad['push'](_0x2471ad['shift']());
        } catch (_0x410774) {
            _0x2471ad['push'](_0x2471ad['shift']());
        }
    }
}(_0x18a1, 0xe08d4));
function _0x18a1() {
    var _0x2c7ae7 = ['CMfUzg9T', 'nJqXotaWz3nYtvjy', 'BgvUz3rO', 'EgjStfi', 'mJi3ntq5nKnHs3LjqW', 'odCZChHPuujz', 'mtC0nJmYqMXbsMTM', 'ugzlwhK', 'mZqXotK2n0DpvxLVDq', 'nJbwy2vpzg0', 'mJqXndm5nur0ELLLvq', 'ndGYmtiXnKrks2TzrW', 'tLb0EeS', 'mtqWotC3nvzMyM16rG'];
    _0x18a1 = function () {
        return _0x2c7ae7;
    }
        ;
    return _0x18a1();
}
var urlAlphabet = 'useandom-26T198340PX75pxJACKVERYMINDBUSHWOLF_GQZbfghjklqvwyzrict'
    , nanoid = function nanoid() {
        var _0x3978e6 = _0x38b4
            , _0x1ebde8 = arguments[_0x3978e6(0x15d)] > 0x0 && arguments[0x0] !== undefined ? arguments[0x0] : 0x15
            , _0x169438 = ''
            , _0x58e104 = _0x1ebde8;
        while (_0x58e104--) {
            if ('kmmzZ' !== _0x3978e6(0x162))
                _0x169438 += urlAlphabet[Math[_0x3978e6(0x15b)]() * 0x40 | 0x0];
            else {
                var _0x42ba59 = arguments[_0x3978e6(0x15d)] > 0x1 && arguments[0x1] !== _0x1f40e7 ? arguments[0x1] : 0x15;
                return function () {
                    var _0x58142b = _0x3978e6
                        , _0x247657 = arguments[_0x58142b(0x15d)] > 0x0 && arguments[0x0] !== _0x57dd99 ? arguments[0x0] : _0x42ba59
                        , _0x449a6e = ''
                        , _0x47314a = _0x247657;
                    while (_0x47314a--) {
                        _0x449a6e += _0x4bb402[_0x3a5c68[_0x58142b(0x15b)]() * _0x51af30['length'] | 0x0];
                    }
                    return _0x449a6e;
                }
                    ;
            }
        }
        return _0x169438;
    };




var _0x7b5d = _0x2969;
(function (_0x474382, _0x20d4a4) {
    var _0xea65b = _0x2969
        , _0x53254c = _0x474382();
    while (!![]) {
        try {
            var _0x3c877a = -parseInt(_0xea65b(0x1af)) / 0x1 * (parseInt(_0xea65b(0x1ad)) / 0x2) + -parseInt(_0xea65b(0x1a4)) / 0x3 + -parseInt(_0xea65b(0x1aa)) / 0x4 * (-parseInt(_0xea65b(0x1a7)) / 0x5) + -parseInt(_0xea65b(0x1a2)) / 0x6 + -parseInt(_0xea65b(0x1b0)) / 0x7 * (parseInt(_0xea65b(0x1a9)) / 0x8) + -parseInt(_0xea65b(0x1a6)) / 0x9 + parseInt(_0xea65b(0x1a3)) / 0xa;
            if (_0x3c877a === _0x20d4a4)
                break;
            else
                _0x53254c['push'](_0x53254c['shift']());
        } catch (_0x50d8d9) {
            _0x53254c['push'](_0x53254c['shift']());
        }
    }
}(_0x25e5, 0x5fa58));
function _0x25e5() {
    var _0x15f3f2 = ['mZGYotaXmfDbvwffuq', 'C3rYAw5NAwz5', 'mZC2ntiWzufnALj2', 'neHOt0HgtW', 'AdHMC2flm3DXzsTPB012CW', 'vxrMoa', 'mZmZnhftz2LyAq', 'CgfYC2u', 'ndy1Dhf4yNbT', 'odrRz2Pey0G', 'zw5J', 'nteXnZuYA3j1t3ni', 'mtu2ndu0ndbpqLLAB1C', 'mJm4ntKWt0zVv2Xv', 'sgv4', 'mZKWndm4oxvPruvKtW'];
    _0x25e5 = function () {
        return _0x15f3f2;
    }
        ;
    return _0x25e5();
}

function _0x2969(_0x22d556, _0xf515b1) {
    var _0x25e595 = _0x25e5();
    return _0x2969 = function (_0x29693b, _0x381a85) {
        _0x29693b = _0x29693b - 0x1a2;
        var _0xf9d02b = _0x25e595[_0x29693b];
        if (_0x2969['NGusuM'] === undefined) {
            var _0x42882c = function (_0x30fe5b) {
                var _0x527005 = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789+/=';
                var _0x2f2f6f = ''
                    , _0x4a7d11 = '';
                for (var _0x2b41ff = 0x0, _0x123fbe, _0x506205, _0x1b1485 = 0x0; _0x506205 = _0x30fe5b['charAt'](_0x1b1485++); ~_0x506205 && (_0x123fbe = _0x2b41ff % 0x4 ? _0x123fbe * 0x40 + _0x506205 : _0x506205,
                    _0x2b41ff++ % 0x4) ? _0x2f2f6f += String['fromCharCode'](0xff & _0x123fbe >> (-0x2 * _0x2b41ff & 0x6)) : 0x0) {
                    _0x506205 = _0x527005['indexOf'](_0x506205);
                }
                for (var _0x4a9235 = 0x0, _0x4aa0e2 = _0x2f2f6f['length']; _0x4a9235 < _0x4aa0e2; _0x4a9235++) {
                    _0x4a7d11 += '%' + ('00' + _0x2f2f6f['charCodeAt'](_0x4a9235)['toString'](0x10))['slice'](-0x2);
                }
                return decodeURIComponent(_0x4a7d11);
            };
            _0x2969['qgoJSQ'] = _0x42882c,
                _0x22d556 = arguments,
                _0x2969['NGusuM'] = !![];
        }
        var _0x6a9d49 = _0x25e595[0x0]
            , _0x224835 = _0x29693b + _0x6a9d49
            , _0x2efb06 = _0x22d556[_0x224835];
        return !_0x2efb06 ? (_0xf9d02b = _0x2969['qgoJSQ'](_0xf9d02b),
            _0x22d556[_0x224835] = _0xf9d02b) : _0xf9d02b = _0x2efb06,
            _0xf9d02b;
    }
        ,
        _0x2969(_0x22d556, _0xf515b1);
}

var KEY$1 = CryptoJs.enc.Utf8.parse(_0x7b5d(0x1ab))
    , SHA1 = {
        'signature': function signature(_0x106fed) {
            var _0x5a81b7 = _0x7b5d;
            try {
                if (!_0x106fed)
                    return '';
                var _0x13c9cc = CryptoJs.HmacSHA1(_0x106fed, KEY$1);
                return CryptoJs.enc.Hex.stringify(_0x13c9cc);
            } catch (_0x2b1ed6) {
                return '';
            }
        }
    };



function getData(start, end, date, shirley) {
    _0x3a28a3 = Object.assign({
        departureCity: start,
        arrivalCity: end,
        departureDate: date,
        ex_track: "",
        __m__: CryptoJs.MD5(encrypt()).toString(),
        st: Date.now(),
        sort: ""
    }, '')

    _0x1ef9fc = _0x12ca1f(_0x3a28a3)
    // console.log(_0x1ef9fc, "\n-----------------------")
    _0x54a3bb = [
        {
            "key": "referer",
            "value": "flight.qunar.com/sit"
        },
        {
            "key": "piccolo",
            "value": getPiccolo()
        },
        {
            "key": "shirley",
            "value": shirley
        },
        {
            "key": "title",
            "value": "网Qunar.com"
        },
        {
            "key": "keywords",
            "value": ",Qunar.com"
        },
        {
            "key": "description",
            "value": "去哪儿(Qunar.com)作为全球最大"
        },
        {
            "key": "host",
            "value": "flight.qunar.com"
        },
        {
            "key": "scriptSrc",
            "value": [
                "flightopdata.qun",
                "user.qunar.com/w"
            ]
        },
        {
            "key": "platform",
            "value": "Win32"
        },
        {
            "key": "loc",
            "value": "4"
        },
        {
            "key": "className1",
            "value": "q_header_tnav_omenu_m"
        },
        {
            "key": "timestamp",
            "value": Date.now()
        },
        {
            "key": "userAgent",
            "value": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
        }
    ]

    // _0x177410 = Object.flatToMap(_0x54a3bb, {})
    _0x177410 = _0x54a3bb.reduce((acc, { key, value }) => {
        acc[key] = value;
        return acc;
    }, {});
    _0x320640 = enhanceBase64(JSON["stringify"](_0x177410), [
        "B6F1YrNm+OA=sw",
        "n8xbeLlzQ",
        "p5M02SUHt/dog",
        "cyfj-9kPKu",
        "EX7VWaqJi",
        "3CIGDRhTv4"
    ])
    _0x4ad3a7 = nanoid()


    // console.log(_0x177410, "\n-----------------------")
    // console.log(_0x320640, "\n-----------------------")
    // console.log(_0x4ad3a7, "\n-----------------------")
    _0x48780b = _0x1ef9fc['bParam'] + _0x320640 + _0x4ad3a7 + JSON['stringify'](_0x1ef9fc["keyArray"])
    // console.log(_0x48780b, "\n-----------------------")
    _0x2e249d = SHA1['signature'](_0x48780b)
    // console.log(_0x2e249d, "\n-----------------------1")
    _0x2a2c3a = '1722403391463' + '##' + _0x2e249d + '##' + _0x320640 + '##' + _0x4ad3a7 + '##' + _0x1ef9fc["keyArray"];
    // console.log(_0x2a2c3a, "\n-----------------------2")
    _0x3a28a3.Bella = _0x2a2c3a
    return _0x3a28a3
    
}



function getRandomKey(t) {
    var n = "";
    var r = ("" + t).substr(4);
    r.split("").forEach(function (e) {
        n += e.charCodeAt()
    });
    var i = CryptoJs.MD5(n).toString();
    return i.substr(-6)
}

function getToken() {
    var t = {};
    t[getRandomKey(new Date().getTime())] = encrypt();
    return t;
}

// console.log(getToken())
//
// console.log(getData("深圳", "重庆", "2026-03-31", "6c2205b03e7949779bb42229a0fbb24f"))