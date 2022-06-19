/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public boolean hasCycle(ListNode head) {
        if (head == null || head.next == null) {
            return false;
        }
        ListNode dummy = new ListNode();
        ListNode front = head;
        while (head.next.next != null) {
            if (head == head.next) {
                return true;
            }
            if (head.next.next == dummy) {
                return true;
            }
            head = head.next;
            front.next = dummy;
            front = head;
        }
        return false;
    }
    
    //public hasCycleHelper(z)
}