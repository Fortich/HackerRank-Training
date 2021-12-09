import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.function.*;
import java.util.regex.*;
import java.util.stream.*;

import static java.util.stream.Collectors.joining;
import static java.util.stream.Collectors.toList;

class Result {

	/*
		Detect a cycle in a linked list. Note that the head pointer may be 'null' if the list is empty.

		A Node is defined as:
    	class Node {
        	int data;
        	Node next;
    	}
	*/

	boolean hasCycle(Node head) {

		boolean answer = false;
		Set<Node> nodesMemory = new HashSet();
		Node current = head;
		while (current != null) {
			if (nodesMemory.contains(current)) {
				answer = true;
				break;
			} else {
				nodesMemory.add(current);
			}
			current = current.next;
		}
		return answer;
	}
}
