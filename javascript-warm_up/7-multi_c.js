#!/usr/bin/node
const a = process.argv.slice(2);
if (isNaN(Number(a[0]))) {
  console.log('Missing number of occurrences');
} else {
  for (let b = 0; b < Number(a[0]); b++) {
    console.log('C is fun');
  }
}
