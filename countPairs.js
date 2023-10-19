function compareSum(i,j,target){
    return i+j<target
}
function increment(i,j,target,c){
    if(compareSum(i,j,target)) c++
    return c
}
function secondIteration(i,nums,target,c){
    for(let j=i+1; j<nums.length; j++) c=increment(nums[i],nums[j],target,c)
    return c
}
function firstIteration(nums,target,c){
    for(let i=0;i<nums.length;i++) c=secondIteration(i,nums,target,c)
    return c
}
/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var countPairs = function(nums, target) {
    let count=0;
    return firstIteration(nums,target,count)
};

