function(key, values) {
	
	// Result 1. {country_codes: ["...", "..."]} or 2. {gender: "...", country_codes: ["...", "..."]}
	var result = {};

  	// Values is an array of values of all the objects with the same key  :P 
    values.forEach(function(value) {
    	// Value is a single object

    	// 1. Value = {country_code = "..."}
    	if ("country_code" in value) {
    		if(!("country_codes" in result)) {
    			result.country_codes = [];	
    		}
    		result.country_codes.push(value['country_code']);
    	// 2. Value = {country_codes = ["...", "..."]}	
    	} else if ("country_codes" in value) { 
    		if(!("country_codes" in result)) {
    			result.country_codes = [];
    		}
    		result.country_codes.push.apply(result.country_codes, value.country_codes);
	    }
		// 3. Value = {gender: "..."}
    	// } else if ("gender" in value) {
    	// 	result.gender = value.gender;
    	// }
    });
    return result;
}
