#!/usr/bin/node
const a = process.argv.slice(2);
if (a[0] === undefined) {
  console.log('undefined is undefined');
} else {
  if (a[1] === undefined) {
    console.log(a[0], 'is undefined');
  } else {
    console.log(a[0], 'is', a[1]);
  }
}
