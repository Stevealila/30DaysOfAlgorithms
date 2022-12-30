/*
    Question: Leetcode 682
    Link: https://leetcode.com/problems/baseball-game/

    This implementation applies the Stack Data Structure.

    Runs in 0(n).
*/

const baseballGame = ops => {
    let stack = []

    for (let i = 0; i < ops.length; i++) {
        // track the tip of the stack
        let lastIndex = stack.length - 1
        // modify the stack depending on the given operator
        switch (ops[i]) {
            case "+": 
                if (stack.length >= 2) 
                    stack.push(stack[lastIndex] + stack[lastIndex-1])
                break;
            
            case "D": 
                stack.push(stack[lastIndex] * 2)
                break;

            case "C":
                stack.pop()
                break;
        
            default: 
                let x = parseInt(ops[i])
                stack.push(x)
                break;
        }            
    }
        
    // return the elements' sum if the stack is not empty
    if (!stack.length) return 0
    return stack.reduce((total, n) => total + n)

}


let ops = ["5","2","C","D","+"]
console.log(baseballGame(ops)) // 30

ops = ["5","-2","4","C","D","9","+","+"]
console.log(baseballGame(ops)) // 27

ops = ["1","C"]
console.log(baseballGame(ops)) // 0
