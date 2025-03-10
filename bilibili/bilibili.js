const CryptoJs = require('crypto-js')


function formatImgByLocalParams(V) {
        // F || (F = {});
        const {imgKey: Q, subKey: Y} = {
            "imgKey": "7cd084941338484aae1ad9425b84077c",
            "subKey": "4932caff0ff746eab6f01bf08b70ac45"
        };
        if (Q && Y) {
        const z = 'ea1db124af3c7062474693fa704f4ff8',
            J = Math.round(Date.now() / 1e3),
            X = Object.assign({}, V, {
                wts: J
            })
          , H = Object.keys(X).sort()
          , ee = []
          , q = /[!'()*]/g;
        for (let le = 0; le < H.length; le++) {
            const ae = H[le];
            let ce = X[ae];
            ce && typeof ce == "string" && (ce = ce.replace(q, "")),
            ce != null && ee.push(`${encodeURIComponent(ae)}=${encodeURIComponent(ce)}`)
        }
        const L = ee.join("&");
            console.log(L)
        return {
            w_rid: CryptoJs.MD5(L + z).toString(),
            wts: J.toString()
        }
    }
}
