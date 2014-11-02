function() {
	var values = {
		country_code: this.location['country_code']
	};

	emit(this.stalker_id, values);
}