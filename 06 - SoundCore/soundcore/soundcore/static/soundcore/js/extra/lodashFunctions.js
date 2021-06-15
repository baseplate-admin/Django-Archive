const addOrRemove = async (arr, val) => {
    if (!_.includes(arr, val)) {
        arr.push(val);
    } else {
        _.remove(arr, item => item === val);
    }
    //  console.log(arr);
}
const firstN = (obj, n) => {
    return _.chain(obj)
        .keys()
        .sort()
        .take(n)
        .reduce(function (memo, current) {
            memo[current] = obj[current];
            return memo;
        }, {})
        .value();
}
