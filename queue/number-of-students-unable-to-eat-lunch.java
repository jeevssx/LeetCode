class Solution {
    public int countStudents(int[] students, int[] sandwiches) {
        Stack<Integer> newStack = new Stack<>();
        Queue<Integer> newQueue = new LinkedList<>();

        for (int i = 0; i < students.length; i++) {
            newStack.push(sandwiches[sandwiches.length-i-1]);
            newQueue.offer(students[i]);
        }

        int hungryStudents = 0;
        while(true){
            if (newQueue.peek() == newStack.peek()) {

                hungryStudents = 0;

                newStack.pop();
                newQueue.poll();
            }
            else {

                hungryStudents++;
                newQueue.offer(newQueue.poll());
                
            }

            if (hungryStudents == newQueue.size()) {
                break;
            }
        }
        return hungryStudents;
        
    }
}