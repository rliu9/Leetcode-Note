class Solution {
    public String intToRoman(int num) {
        HashMap<Integer, String> map = new HashMap<Integer,String>();
        map.put(1000, "M");
        map.put(900, "CM");
        map.put(500, "D");
        map.put(400, "CD");
        map.put(100, "C");
        map.put(90, "XC");
        map.put(50, "L");
        map.put(40, "XL");
        map.put(10, "X");
        map.put(9, "IX");
        map.put(8, "VIII");
        map.put(7, "VII");
        map.put(6, "VI");
        map.put(5, "V");
        map.put(4, "IV");
        map.put(3, "III");
        map.put(2, "II");
        map.put(1, "I");
        String s = "";
        List<Integer> keys = new ArrayList<Integer>(map.keySet());
        Collections.sort(keys, Collections.reverseOrder());
        for (int value:keys){
            int amount = num / value;
            s += map.get(value).repeat(amount);
            num -= amount*value;
        }
        return s;
    }
}