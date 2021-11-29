package com.project_euler_problems;

class Main {

    public static void main(String[] args) {
        int n3 = 999/3;
        int n5 = 999/5;
        int n15 = 999/15;
        System.out.println(problem_1.solution(n3, n5, n15));
    }
}
public class problem_1 {

    private static int sum_to_n(int n){
        return n * (n + 1) / 2;
    }

    public static int solution(int n3, int n5, int n15){
        return 3 * sum_to_n(n3) + 5 * sum_to_n(n5) - 15 * sum_to_n(n15);
    }
}
