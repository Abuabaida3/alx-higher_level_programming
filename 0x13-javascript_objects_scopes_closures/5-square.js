#!/usr/bin/node
class Rectangle{
constructor (w, h){
if (w > 0 && h > 0){
this.wight = w;
this.height = h;
}
}
print (){
for (let i = 0; i < this.height; i++){
console.log('X'.repeat(this.width));
}
}
rote (){
let tmp = this.width;
this.width = this.height;
this.height = tmp;
}
double (){
this.width *= 2;
this.height *= 2;
}
}

module.exports = class square extends Rectangle {
constructor (size){
super(size, size);
}
};
