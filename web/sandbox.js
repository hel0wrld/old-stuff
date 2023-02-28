// object

let user = {
    name: "hedo",
    loc: "bangladesh",
    age: "good enough",
    interests: ['chess', 'gayming', 'anime'],
    ph: 453353,
    login: function() {
        console.log('user logged in');
    }
};

console.log(user);
console.log(user.name);
console.log(typeof user);
user.login();

console.log('hi there ${user.name}')