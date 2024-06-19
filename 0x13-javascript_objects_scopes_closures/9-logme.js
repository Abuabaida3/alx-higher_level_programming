#!/usr/bin/node
exportts.logMe = (function (item){
let n = 0;
return function (item){ console.log(n++ + ': ' + item);};
}());
