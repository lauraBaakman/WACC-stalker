function(key, values) {
    var result = {};
    values.forEach(function(value) {
        var field;
        for (field in value) {
            if (value.hasOwnProperty(field)) {
                result[field] = value[field];
            }
        }
    });
    return result;
}