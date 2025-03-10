window = global;


let n = require('./out.js');
let c = n('b85c');
u = n("6821")
l = n.n(u)



function encrypted(e){
    e._ts = (new Date).getTime() - 9999;
    var t, n = Object.keys(e), i = "", o = Object(c["a"])(n.sort());
    for (o.s(); !(t = o.n()).done; ) {
        var a = t.value;
        void 0 !== e[a] && null !== e[a] && (i += "".concat(a, "=").concat(e[a], ","))
    }
    return {"signature": l()(i),
        "_ts": e._ts
    }
}
