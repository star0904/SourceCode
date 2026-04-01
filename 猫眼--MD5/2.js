window = global;

(function (exports, require, module) {
        "use strict";

        function _interopRequireDefault(e) {
            return e && e.__esModule ? e : {
                default: e
            }
        }

        function _0x5ec0(e, t) {
            var r = _0x3a2b();
            return (_0x5ec0 = function (e, t) {
                    return e -= 251,
                        r[e]
                }
            )(e, t)
        }

        window.getQueryKey = function getQueryKey(e) {
            var t = e.query
                , r = e.headers
                , n = void 0 === r ? {} : r
                , a = e.method
                , s = void 0 === a ? "GET" : a
                , o = e.ua
                , u = e.timeStamp
                , i = _0x5ec0
                , d = {
                method: s,
                timeStamp: u || +new Date,
                "User-Agent": btoa("" + "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"),
                index: Math[i(259)](1e3 * Math[i(253)]() + 1),
                channelId: 40009,
                sVersion: 2,
                key: i(270)
            }
                , c = Object[i(260)](d).reduce(function (e, t) {
                var r = i;
                return e = 0 === d[t] || d[t] ? e + "&" + t + "=" + d[t] : e + "&" + t + r(254)
            }, "")[i(271)](1)
                , f = void 0;
            try {
                f = (0,
                    _jsMd2.default)(c[i(269)](/\s+/g, " ")).toString()
            } catch (e) {
                console.log(i(252), e)
            }
            return d.signKey = f,
                delete d[i(251)],
                delete d.key,
                {
                    finalQuery: _extends({}, t, d),
                    finalHeaders: _extends({}, n, {
                        signKey: f
                    }),
                    signKey: f
                }
        }

        function _0x3a2b() {
            var e = ["80hLgZPi", "10938120Oqmcds", "btoa", "userAgent", "804811nlntFe", "2585358GVcSNa", "2738538eYUjeG", "13373xdWcLL", "replace", "A013F70DB97834C0A5492378BD76C53A", "slice", "method", "error", "random", "=''", "548WwYBRt", "9254088oEFLMS", "118hfsyEC", "30445WALNJs", "floor", "keys"];
            return (_0x3a2b = function () {
                    return e
                }
            )()
        }

        Object.defineProperty(exports, "__esModule", {
            value: !0
        });
        var _extends = Object.assign || function (e) {
            for (var t = 1; t < arguments.length; t++) {
                var r = arguments[t];
                for (var n in r)
                    Object.prototype.hasOwnProperty.call(r, n) && (e[n] = r[n])
            }
            return e
        }
            , _jsMd = require('crypto-js').MD5
            , _jsMd2 = _interopRequireDefault(_jsMd)

        !function (e, t) {
            for (var r = _0x5ec0, n = e(); [];)
                try {
                    if (633601 === -parseInt(r(268)) / 1 * (-parseInt(r(257)) / 2) + -parseInt(r(266)) / 3 + parseInt(r(255)) / 4 * (-parseInt(r(258)) / 5) + parseInt(r(267)) / 6 + -parseInt(r(265)) / 7 * (-parseInt(r(261)) / 8) + parseInt(r(256)) / 9 + -parseInt(r(262)) / 10)
                        break;
                    n.push(n.shift())
                } catch (e) {
                    n.push(n.shift())
                }
        }(_0x3a2b),
            exports.default = {
                getQueryKey: getQueryKey
            },
            module.exports = exports.default;
    }
    //# sourceURL=/client/common/utils/veri.js
)({}, require, module)


function getParams(uuid) {
    arguments = {
        "query": {
            "showDate": undefined,
            "movieId": undefined,
            "orderType": 0,
            "uuid": uuid
        },
        "timeStamp": Date.now()
    }
    return window.getQueryKey(arguments)
}
