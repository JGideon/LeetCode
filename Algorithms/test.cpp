// Test
struct ListNode {
	int val;
	struct ListNode *next;
};

struct ListNode* swapPairs(struct ListNode* head) {
	if (head || head->next) return head;
	struct ListNode *p1, *p2, *p3;
	p1=head;
	head=head->next;
	while ((p1)&&(p1->next)){
	    p2=p1->next;
	    p3=p1->next->next;
	    p2->next=p1;
	    if (p3 && (p3->next)) p1->next=p3->next;
	    else p1->next=p3;
	    p1=p3;
	}
	return head;
}

int main()
{
    test.c
	return 0;
}
