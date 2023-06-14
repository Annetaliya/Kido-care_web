/*let url= ('https://api.rcpch.ac.uk/growth/v1/uk-who/calculation')

let options = {
    methods: 'get'
};
let request = new Request(url, options)
fetch(request).then(response => {
    if (!response.ok) {
        throw new Error('Error occured');
    }
    return response.json();
}).then(data => {
    console.log(data);
}).catch(error => {
    console.log('error', error.message);
});
xhr.onload = function () {
    const serverResponse = document.getElementById("serverResponse");
    serverResponse.innerHTML = this.responseText;
};

xhr.open('https://api.rcpch.ac.uk/growth/v1/uk-who/calculation');
xhr.setRequestHeader("content-type", "application/x-www-form-urlencoded");
xhr.send