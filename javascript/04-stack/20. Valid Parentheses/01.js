// Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

// An input string is valid if:

// Open brackets must be closed by the same type of brackets.
// Open brackets must be closed in the correct order.

/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
    let current, stack = []
    for (let i = 0; i < s.length; i++) {
        current = s[i]
        if (current === '{' || current === '[' || current === '('){
            stack.push(current)
        }
        else if (current === '}'){
            if (stack.pop() !== '{'){
                return false
            }
        }
        else if (current === ']'){
            if (stack.pop() !== ']'){
                return false
            }
        }
        else if (current === ')'){
            if (stack.pop() !== ')'){
                return false
            }
        }
    }
    return stack.length == 0
};