function print() {
	console.log("Het werkt nog steeds!");
}

require(['jquery', 'app/main'], function($) {
    $('h1').text("Het werkt!");
    print();
});