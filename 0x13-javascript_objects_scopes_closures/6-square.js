#!/usr/bin/node
const oldSquare = require('./5-square');
module.exports = class Square extends oldSqusre {
chaprint (c){
if (c === undefined) c = 'X';
for (let i = 0; i < this.height; i++){
console.log(c.repeat(this.wight));
}
}
};
