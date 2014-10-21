function() { // On Stalkers
	var values = {
		gender: this.gender
	};
	emit(this.stalker_id, values);
}