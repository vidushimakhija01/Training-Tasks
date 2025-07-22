let user = {
    firstname: "hello",
    bio: {
        address: "world",
        pincode: 578364,
        marks: [
            {
                subject: "abc",
                value: 67,
            },
            {
                subject: "def",
                value: 34,
            },
            {
                subject: "xyz",
                value: 78,
            },
        ],
    },
    lang: ['hindi', 'english']
}
console.log(Object.values(user.lang))
let sum = 0;
for (let x of user.bio.marks) {
    console.log(x);
    if (x.value >= 50)
        sum += x.value;
}
console.log(sum)

//Print that element of array which occurs only once
let arr = [2,2,4]
let arrObj = {}
for (let i in arr){
    if (!(arr[i] in arrObj))
        arrObj[arr[i]] = 1;
    else arrObj[arr[i]]++;
}
console.log(arrObj)
let x = Object.entries(arrObj)
x.forEach((y) => {
    if (y[1] === 1)
        console.log(Number(y[0]));
})

