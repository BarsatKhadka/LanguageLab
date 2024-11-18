import java.util.List;
import java.util.Arrays;
import java.util.stream.Collectors;

class java8{
    public static void main(String[] args) {

        //Basic Filtering and mapping
        // List<Integer> list  = Arrays.asList(5,10,15,35,20);
        // List<Integer> filteredList = list.stream().filter(i -> i%2 ==0).collect(Collectors.toList());
        // List<Integer> mappedList = list.stream().map(i -> i*2).toList();
        // System.out.println(filteredList);
        // System.out.println(mappedList);

        //Select only passed student
        List<Integer> score  = Arrays.asList(5,10,15,35,20);
        List<Integer> failedList = score.stream().filter(i -> i <15).collect(Collectors.toList());
        List<Integer> GraceMarks = failedList.stream().map(i -> i+5).toList();
        
        //count
        Long numberOfFailedStudent = failedList.stream().count();
        System.out.println(numberOfFailedStudent);





        
    }
}