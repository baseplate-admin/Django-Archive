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
