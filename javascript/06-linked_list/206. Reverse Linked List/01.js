// // Question:
// Reverse a singly linked list.

// // Example:
// Input: 1->2->3->4->5->NULL
// Output: 5->4->3->2->1->NULL

/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var reverseList = function(head) {
    let prev = null
    
    while (head != null) {
        let current = head.next
        head.next = prev
        prev = head
        head = current
    }
    return prev
};