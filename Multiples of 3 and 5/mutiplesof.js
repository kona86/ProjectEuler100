
function mutiplesof(a,b,to) {
    var list = []
    var result = null
    while (--to) {
            if (to == 0) break
            if (  (to % a) == 0 ) list.push(to)
            if ((to % b )== 0) list.push(to)
        }
    result = list.reduce((a,b)=>a+b)
    return result
    }

var threeand5 = mutiplesof(3,5,1e3)
console.log(threeand5) 