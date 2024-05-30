const apiEndpoint = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';

$.ajax({
	type: 'GET',
	url: apiEndpoint,
	success: (data) => {
		$('div#character').text(data.name)
	}
})