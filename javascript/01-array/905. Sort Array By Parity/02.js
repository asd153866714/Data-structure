var sortArrayByParity = function (A) {

    let B = new Array()
    if (A.length >= 2){
        A.forEach((a) => {
             a%2==0  ? B.unshift(a) : B.push(a) 
        })
        return B
    }
    return A
};

sortArrayByParity([1, 2, 3, 4])