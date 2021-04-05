import java.util.Arrays;
import java.util.Comparator;

class Solution {
    public int[] solution(int n, int[] passenger, int[][] train) {
        int[] answer = new int[2];

        Arrays.sort(train, new Comparator<int[]>() {
            @Override
                public int compare(int[] o1, int[] o2) {
                    if(o1[0] == o2[0]) {
                        return o1[1] - o2[1];
                    }else {
                        return o1[0] - o2[0];
                    }
            }
        });

        int i = 0;
        int j = 0;
        int[] check_train_length = new int[100001];
        check_train_length[1] = passenger[0];
        int k = 0;
        for(i=0;i<train.length;i++)
        {
            k = 0;
            k = check_train_length[train[i][0]] + passenger[train[i][1]-1];

            if(k >= check_train_length[train[i][1]])
            {
                check_train_length[train[i][1]] = k;
            }
        }

        for(i=1;i<=n;i++)
        {
            if(answer[1] <= check_train_length[i])
            {
                answer[0] = i;
                answer[1] = check_train_length[i];
            }
        }

        return answer;
    }
}