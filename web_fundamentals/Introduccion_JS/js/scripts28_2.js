    // 1. Creating objects with an object literal
    const personLiteral = {
    firstName: 'Alice',        // property: first name of the person
    lastName: 'Johnson',       // property: last name of the person
    age: 30,                   // property: age of the person
    // method: returns the full name by using `this` to refer to this object
    getFullName() {
        return `${this.firstName} ${this.lastName}`;
    }
    };

    console.log(personLiteral);               // { firstName: 'Alice', lastName: 'Johnson', age: 30, getFullName: [Function: getFullName] } :contentReference[oaicite:0]{index=0}
    console.log(personLiteral.getFullName()); // "Alice Johnson" :contentReference[oaicite:1]{index=1}

    // 2. Creating objects with the Object constructor
    const personConstructor = new Object();  // create an empty object using the Object constructor
    personConstructor.firstName = 'Bob';      // add property: firstName
    personConstructor.lastName = 'Smith';     // add property: lastName
    personConstructor.age = 25;               // add property: age

    // method: define on the object instance directly
    personConstructor.getFullName = function() {
    return `${this.firstName} ${this.lastName}`;
    };

    console.log(personConstructor);               // { firstName: 'Bob', lastName: 'Smith', age: 25, getFullName: [Function] } :contentReference[oaicite:2]{index=2}
    console.log(personConstructor.getFullName()); // "Bob Smith" :contentReference[oaicite:3]{index=3}

    // 3. Constructor function pattern (pre-ES6 "class" style)
    function PersonConstructor(firstName, lastName, age) {
    this.firstName = firstName; // instance property
    this.lastName  = lastName;  // instance property
    this.age       = age;       // instance property
    }
    // prototype method: shared by all instances
    PersonConstructor.prototype.getFullName = function() {
    return `${this.firstName} ${this.lastName}`;
    };

    const charlie = new PersonConstructor('Charlie', 'Brown', 40);
    console.log(charlie);               // PersonConstructor { firstName: 'Charlie', lastName: 'Brown', age: 40 } :contentReference[oaicite:4]{index=4}
    console.log(charlie.getFullName()); // "Charlie Brown" :contentReference[oaicite:5]{index=5}

    // 4. Comparing prototype chains
    console.log(Object.getPrototypeOf(personLiteral) === Object.prototype);      // true :contentReference[oaicite:6]{index=6}
    console.log(Object.getPrototypeOf(personConstructor) === Object.prototype); // true :contentReference[oaicite:7]{index=7}
    console.log(PersonConstructor.prototype.isPrototypeOf(charlie));            // true :contentReference[oaicite:8]{index=8}
