#!/usr/bin/node

const lenargs = process.argv.length;
if (lenargs <= 3) {
  console.log(0);
} else {
  const nums = [];
  for (let i = 2; i < lenargs; i++) {
    nums[i - 2] = parseInt(process.argv[i]);
  }
  nums.sort();
  console.log(nums[lenargs - 4]);
}
