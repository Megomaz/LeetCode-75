class Solution {
    public boolean uniqueOccurrences(int[] arr) {
        Set<Integer> set = new HashSet<>();
        Map<Integer,Integer> hashmap = new HashMap<>();

        for (int num: arr){
            hashmap.put(num, hashmap.getOrDefault(num,0) + 1);
        }

        for (int num: hashmap.values()){
            if (set.contains(num)){
                return false;
            }
            set.add(num);
        }
        return true;
    }
}