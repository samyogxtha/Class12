class mydetails {
    public static void main(String[] args) {
        String name = "Samyog";
        int age = 17;
        String country = "Nepal";

        String formatedstr = String.format("My name is %s. I am %d years old. i am from %s.",name,age,country);
        System.out.println(formatedstr);
    }
}