#!/usr/bin/node
const x = process.argv.slice(2);
if (x[0] === undefined) {
  console.log('No argument');
} else {
  console.log(x[0]);
}
